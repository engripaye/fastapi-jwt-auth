---

# User Auth System (JWT Tokens) 🔑

A lightweight **authentication system** built with **FastAPI**, featuring **secure JWT-based authentication**, **password hashing**, and **protected endpoints**.

## 🚀 Features

* **User Signup & Login**
* **Password hashing** with [Passlib](https://passlib.readthedocs.io/)
* **JWT Authentication** using [python-jose](https://python-jose.readthedocs.io/)
* **Secure API endpoints** protected with OAuth2 + JWT tokens
* **Dependency injection** for cleaner and testable code

## 🛠️ Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/) – Web framework
* [Uvicorn](https://www.uvicorn.org/) – ASGI server
* [SQLAlchemy](https://www.sqlalchemy.org/) – ORM for database operations
* [Alembic](https://alembic.sqlalchemy.org/) – Database migrations
* [Pydantic](https://docs.pydantic.dev/) – Data validation
* [Passlib](https://passlib.readthedocs.io/) – Password hashing
* [Python-JOSE](https://python-jose.readthedocs.io/) – JWT tokens

## 📂 Project Structure

```
.
├── app
│   ├── main.py          # Entry point
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── auth.py          # Authentication logic (JWT, OAuth2)
│   ├── database.py      # DB setup and session management
│   └── routes
│       └── users.py     # Signup/Login endpoints
├── alembic/             # Migrations
├── .env                 # Environment variables
├── requirements.txt     # Dependencies
└── README.md
```

## ⚡ Installation & Setup

1. **Clone the repo**

```bash
git clone https://github.com/your-username/user-auth-system.git
cd user-auth-system
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set environment variables**
   Create a `.env` file in the root folder:

```env
DATABASE_URL=sqlite:///./auth.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. **Run database migrations**

```bash
alembic upgrade head
```

6. **Start the server**

```bash
uvicorn app.main:app --reload
```

## 🔑 Usage

* **Signup** → `POST /users/signup`
* **Login** → `POST /users/login`
* **Protected Endpoint** → Include `Authorization: Bearer <token>` in headers

## 📖 API Docs

Once the server is running, access interactive API docs:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

## 📜 License

This project is licensed under the **MIT License**.

---

Would you like me to also create a **requirements.txt** snippet inside the README so users can quickly see dependencies without opening the file?
