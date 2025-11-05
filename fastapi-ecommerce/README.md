# E-commerce API

High-performance e-commerce backend built with FastAPI. Includes product management, shopping cart, order processing, and user authentication.

## Features

- FastAPI with async support
- PostgreSQL database integration
- JWT-based authentication
- Product CRUD operations
- Shopping cart and order management
- Stock management
- Automatic API documentation (Swagger/OpenAPI)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up PostgreSQL database:
```bash
createdb ecommerce
```

3. Configure environment variables:
```
DATABASE_URI=postgresql://user:password@localhost/ecommerce
SECRET_KEY=your-secret-key
```

4. Run the application:
```bash
python main.py
```

Or with uvicorn:
```bash
uvicorn main:app --reload --port 8001
```

## API Endpoints

### Authentication
- `POST /api/users/register` - Register a new user
- `POST /api/users/login` - Login and get JWT token

### Products
- `GET /api/products` - Get all products (with optional category filter)
- `POST /api/products` - Create a new product (protected)
- `GET /api/products/{id}` - Get a specific product

### Orders
- `POST /api/orders` - Create a new order (protected)
- `GET /api/orders` - Get user's orders (protected)
- `GET /api/orders/{id}` - Get a specific order (protected)

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8001/docs`
- ReDoc: `http://localhost:8001/redoc`

## Usage Example

```bash
# Register
curl -X POST http://localhost:8001/api/users/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "username": "user", "password": "pass123"}'

# Login
curl -X POST http://localhost:8001/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "pass123"}'

# Create product
curl -X POST http://localhost:8001/api/products \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"name": "Laptop", "description": "High-performance laptop", "price": 999.99, "stock": 10, "category": "Electronics"}'

# Create order
curl -X POST http://localhost:8001/api/orders \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"items": [{"product_id": 1, "quantity": 2}]}'
```



