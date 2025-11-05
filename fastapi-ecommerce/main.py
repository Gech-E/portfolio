from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import os
import jwt

app = FastAPI(
    title="E-commerce API",
    description="High-performance e-commerce backend with FastAPI",
    version="1.0.0"
)

# Database setup
DATABASE_URL = os.environ.get(
    'DATABASE_URI',
    'postgresql://user:password@localhost/ecommerce'
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
security = HTTPBearer()


# Database Models
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    orders = relationship("Order", back_populates="user")


class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer, default=0)
    category = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    order_items = relationship("OrderItem", back_populates="product")


class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_amount = Column(Float)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    price = Column(Float)
    
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")


# Create tables
Base.metadata.create_all(bind=engine)


# Pydantic Models
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category: str


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    category: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]


class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float
    
    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    created_at: datetime
    items: List[OrderItemResponse]
    
    class Config:
        from_attributes = True


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Auth dependency
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return user
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")


# Routes
@app.get("/")
async def root():
    return {"message": "E-commerce API is running"}


@app.post("/api/users/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")
    
    # Create user (in production, hash the password)
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=user.password  # Should be hashed in production
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/api/users/login")
async def login_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or db_user.hashed_password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = jwt.encode({"sub": db_user.id}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}


@app.get("/api/products", response_model=List[ProductResponse])
async def get_products(skip: int = 0, limit: int = 100, category: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category)
    products = query.offset(skip).limit(limit).all()
    return products


@app.post("/api/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.get("/api/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/api/orders", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    total_amount = 0.0
    order_items = []
    
    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
        if product.stock < item.quantity:
            raise HTTPException(status_code=400, detail=f"Insufficient stock for product {product.name}")
        
        item_total = product.price * item.quantity
        total_amount += item_total
        
        order_items.append(OrderItem(
            product_id=item.product_id,
            quantity=item.quantity,
            price=product.price
        ))
    
    db_order = Order(
        user_id=current_user.id,
        total_amount=total_amount,
        status="pending"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    for item in order_items:
        item.order_id = db_order.id
        db.add(item)
        # Update stock
        product = db.query(Product).filter(Product.id == item.product_id).first()
        product.stock -= item.quantity
    
    db.commit()
    db.refresh(db_order)
    
    return db_order


@app.get("/api/orders", response_model=List[OrderResponse])
async def get_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    orders = db.query(Order).filter(Order.user_id == current_user.id).all()
    return orders


@app.get("/api/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == current_user.id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)



