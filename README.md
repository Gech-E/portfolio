# Professional Portfolio Website

A modern, responsive portfolio website showcasing full-stack development, AI/ML, and data science projects. Built with React frontend and FastAPI backend.

## 🚀 Features

- **Modern React Frontend**: Beautiful, responsive UI with animations
- **FastAPI Backend**: RESTful API for portfolio data
- **Multiple Projects**: Complete projects in separate folders
- **Professional Design**: Clean, modern UI with Tailwind CSS
- **Contact Integration**: Easy contact form and social links

## 📁 Project Structure

```
portfolio/
├── src/                    # React frontend source
│   ├── components/         # React components
│   └── pages/              # Page components
├── backend/                # FastAPI backend
├── flask-task-api/         # Flask project (Task Management API)
├── fastapi-ecommerce/     # FastAPI project (E-commerce API)
├── ml-image-classification/# AI/ML project (Image Classification)
└── data-science-sales/     # Data Science project (Sales Analytics)
```

## 🛠️ Technologies

### Frontend
- React 18
- React Router
- Tailwind CSS
- Framer Motion (animations)
- Vite (build tool)

### Backend
- FastAPI
- PostgreSQL (ready for integration)

### Projects
- **Flask**: Task Management API with JWT authentication
- **FastAPI**: E-commerce API with async support
- **TensorFlow/Keras**: CNN for image classification
- **Pandas/Scikit-learn**: Sales analytics and predictions

## 📦 Installation

### Frontend Setup

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend runs on `http://localhost:3000`

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python main.py
```

Backend runs on `http://localhost:8000`

API documentation available at `http://localhost:8000/docs`

## 🎯 Projects

### 1. Flask Task Management API
**Location**: `flask-task-api/`

RESTful API for task management with:
- User authentication (JWT)
- CRUD operations for tasks
- PostgreSQL database integration
- Role-based access control

**Setup**:
```bash
cd flask-task-api
pip install -r requirements.txt
python app.py
```

### 2. FastAPI E-commerce API
**Location**: `fastapi-ecommerce/`

High-performance e-commerce backend with:
- Async/await support
- Product and order management
- JWT authentication
- Auto-generated API documentation

**Setup**:
```bash
cd fastapi-ecommerce
pip install -r requirements.txt
python main.py
```

### 3. ML Image Classification
**Location**: `ml-image-classification/`

CNN model for image classification:
- Trained on CIFAR-10 dataset
- Data augmentation
- Model evaluation and visualization
- Prediction script

**Setup**:
```bash
cd ml-image-classification
pip install -r requirements.txt
python train_model.py
```

### 4. Data Science Sales Analytics
**Location**: `data-science-sales/`

Comprehensive sales analysis with:
- Exploratory data analysis
- Interactive visualizations
- Predictive modeling
- Business insights

**Setup**:
```bash
cd data-science-sales
pip install -r requirements.txt
python analyze_sales.py
```

## 📝 Contact

- **Email**: getachewekubay8@gmail.com
- **LinkedIn**: [https://www.linkedin.com/in/getachew99](https://www.linkedin.com/in/getachew99)
- **GitHub**: [https://github.com/Gech-E](https://github.com/Gech-E)

## 🎨 Customization

### Update Personal Information

1. **Contact Info**: Edit `src/pages/Contact.jsx` and `src/pages/Home.jsx`
2. **About Section**: Edit `src/pages/About.jsx`
3. **Projects**: Edit `src/pages/Projects.jsx` and `backend/main.py`

### Styling

- Tailwind config: `tailwind.config.js`
- Global styles: `src/index.css`
- Color scheme: Update primary colors in Tailwind config

## 📄 License

This project is open source and available for personal use.

## 🙏 Acknowledgments

Built with modern web technologies and best practices for a professional portfolio showcase.

---

**Developer**: Getachew Ekubay  
**Role**: Full Stack Developer | AI/ML Engineer | Data Scientist

