# Contacts API with Authentication and Advanced Features

A robust RESTful API for managing contacts with support for authentication,
authorization (JWT), email verification, CORS, avatar uploads via Cloudinary,
rate limiting, and user-specific contact access.

## 📦 Tech Stack

- **FastAPI** — modern, fast (high-performance) web framework for building APIs.
- **SQLAlchemy Async** — asynchronous ORM for database interactions.
- **Alembic** — database migrations tool.
- **PostgreSQL** — relational database system.
- **Pydantic** — data validation and settings management.
- **Poetry** — Python dependency management and packaging.
- **Docker & Docker Compose** — containerization and orchestration.
- **Cloudinary** — cloud-based image and video management for avatar uploads.
- **JWT (JSON Web Tokens)** — secure user authentication and authorization.
- **Redis** — caching and rate limiting backend.

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/goit-pythonweb-hw-10.git
cd goit-pythonweb-hw-10
```

### 2. Install Dependencies

Ensure Poetry is installed, then run:

```bash
poetry install
```

### 3. Configure Environment Variables

Create a `.env` file in the project root (see next section for details).

### 4. Run the Application

**Locally with Poetry:**

```bash
poetry run uvicorn main:app --reload
```

**Or with Docker Compose:**

```bash
docker-compose up --build
```

---

## ⚙️ Environment Variables Configuration

Create a `.env` file in the root directory with the following variables:

```env
DB_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/contacts_db
SECRET_KEY=your_jwt_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

REDIS_URL=redis://localhost:6379/0

BACKEND_CORS_ORIGINS=http://localhost,http://localhost:8000
```

- `DB_URL`: Database connection string.
- `SECRET_KEY`, `ALGORITHM`, `ACCESS_TOKEN_EXPIRE_MINUTES`: JWT configuration.
- Cloudinary credentials for avatar uploads.
- Redis URL for caching and rate limiting.
- CORS allowed origins.

---

## 🔍 Features Overview

- **User Authentication & Authorization**: Register and login users with JWT
  tokens. Access tokens must be included in `Authorization` headers
  (`Bearer <token>`) to access protected endpoints.
- **Email Verification**: Users receive verification emails upon registration.
  Only verified users can access protected resources.
- **Contacts Management**: CRUD operations on contacts. Each user can only
  access and manage their own contacts.
- **Avatar Uploads**: Users can upload avatars for contacts, stored and served
  via Cloudinary.
- **Rate Limiting**: API requests are rate-limited per user/IP using Redis to
  prevent abuse.
- **CORS Support**: Configurable cross-origin resource sharing to allow frontend
  apps to interact securely.
- **Data Validation and Security**: Unique email and phone validation, password
  hashing, and secure token handling.

---

## 📘 API Documentation

Once the application is running, access the interactive API docs at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📂 Project Structure

```
goit-pythonweb-hw-10/
│
├── src/
│   ├── api/               # Route handlers and endpoints
│   ├── conf/              # Configuration and settings
│   ├── database/          # Database models and async session
│   ├── repository/        # Database access logic
│   ├── services/          # Business logic and utilities
│   ├── schemas.py         # Pydantic models for request/response validation
│   └── core/              # Security, authentication, and rate limiting
│
├── migrations/            # Alembic migrations
├── tests/                 # Automated tests
├── .env                   # Environment variables file
├── main.py                # FastAPI application entry point
├── Dockerfile             # Dockerfile for containerization
├── docker-compose.yml     # Docker Compose configuration
└── README.md              # This file
```
