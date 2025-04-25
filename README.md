# Task Manager App — Full stack (Vue.js + Flask + MySQL)

![flask](https://img.shields.io/badge/flask-black?style=flat&logo=flask)
![vue](https://img.shields.io/badge/Vue-black?style=flat&logo=vue.js)
![python](https://img.shields.io/badge/python-black?style=flat&logo=python)


## 📚 Table of Contents

- [Project Overview](#project-overview)
  - [Frontend Features](#frontend-features)
  - [Authentication](#authentication)
  - [API Endpoints](#api-endpoints)
- [Installation & Setup](#installation--setup)
  - [Backend (Flask)](#backend-flask)
  - [Frontend (Vuejs)](#frontend-vuejs)
- [Running Tests](#running-tests)
  - [Backend (Pytest)](#backend-pytest)
  - [Frontend (Jest)](#frontend-jest) 
- [Deployment](#deployment)
- [Contributing](#contributing)

---

## Project Overview

A full stack task management web application. It features secure JWT authentication, a fully tested REST API, and a MySQL database.
Each user can sign up, log in, and manage their personal task list. The frontend consumes the backend's RESTful API.

| Layer        | Technology                |
|--------------|----------------------------|
| Frontend     | Vue.js, Vue Router, Vuex  |
| Backend      | Python, Flask, Flask-JWT-Extended |
| Database     | MySQL (via SQLAlchemy)    |
| Testing      | Pytest (backend), Jest (frontend) |
| Auth         | JSON Web Tokens (JWT)     |

### Frontend Features

- User-friendly dashboard
- Login / Register forms
- Create, edit, delete tasks
- Filter by deadline or status
- JWT authentication and token storage
- Vuex state management

### Authentication

- User registration, login & logout
- JWT access token management
- Secure routes requiring token
- Vuex store with token, user profile (name, email)

### API Endpoints

| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| POST   | `/api/auth/signup`   | Create a new user        |
| POST   | `/api/auth/login`    | Get JWT token or modify user infos            |
| GET    | `/api/tasks`         | Retrieve user's tasks    |
| POST   | `/api/tasks`         | Create a new task        |
| PUT    | `/api/tasks/<id>`    | Update a task            |
| DELETE | `/api/tasks/<id>`    | Delete a task            |

---

## Installation & Setup
### Backend (Flask)

Configure your .env file first.


```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python run.py
```

### Frontend (Vue.js)

```bash
cd frontend
npm install
npm run serve
```

## Running Tests
### Backend (Pytest)
```bash
cd backend
python -m pytest -vv
```

### Frontend (Jest)

```bash
cd frontend
npm run test
```

## Deployment
You can deploy this app to:

- Heroku or Render for backend (Flask)
- Netlify or Vercel for frontend (Vue.js)

Use CI/CD pipelines to automate the process.

## Contributing
Contributions are welcome! Feel free to open an issue or a pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes.
4. Push your branch: `git push origin feature-name`.
5. Create a pull request.