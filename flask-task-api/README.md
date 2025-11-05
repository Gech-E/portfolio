# Task Management API

A robust RESTful API built with Flask and PostgreSQL for managing tasks, users, and projects.

## Features

- User authentication with JWT tokens
- CRUD operations for tasks
- User registration and login
- Role-based access control
- Task filtering by status and priority
- PostgreSQL database integration

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up PostgreSQL database:
```bash
createdb taskdb
```

3. Configure environment variables (create `.env` file):
```
SECRET_KEY=your-secret-key
DATABASE_URI=postgresql://user:password@localhost/taskdb
JWT_SECRET_KEY=your-jwt-secret-key
```

4. Run the application:
```bash
python app.py
```

## API Endpoints

### Authentication
- `POST /api/register` - Register a new user
- `POST /api/login` - Login and get JWT token
- `GET /api/users/me` - Get current user info (protected)

### Tasks
- `GET /api/tasks` - Get all tasks (protected)
- `POST /api/tasks` - Create a new task (protected)
- `GET /api/tasks/<id>` - Get a specific task (protected)
- `PUT /api/tasks/<id>` - Update a task (protected)
- `DELETE /api/tasks/<id>` - Delete a task (protected)

## Usage Example

```bash
# Register a user
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "email": "john@example.com", "password": "password123"}'

# Login
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "password123"}'

# Create a task (use token from login)
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"title": "Complete project", "description": "Finish the portfolio", "priority": "high"}'
```



