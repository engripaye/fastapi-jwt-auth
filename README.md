---

# FastAPI JWT Authentication 🚀

A modern **authentication and authorization API** built with **FastAPI**, **JWT (JSON Web Tokens)**, and **SQLAlchemy**.
This project demonstrates secure user registration, login, token-based authentication, and role-based access control.

---

## 📌 Features

* 🔑 **User Authentication** with JWT (Access & Refresh Tokens)
* 👤 **User Registration & Login** endpoints
* 🔒 **Password Hashing** with `passlib`
* 🛡️ **Role-Based Access Control (RBAC)** support
* 🗄️ **SQLAlchemy ORM** for database interaction
* ⚡ Built on **FastAPI** (high-performance Python framework)
* 🧪 **Validation** with Pydantic

---

## 🛠️ Tech Stack

* **FastAPI** – Web framework
* **Uvicorn** – ASGI server
* **SQLAlchemy 2.0** – Database ORM
* **Passlib** – Password hashing
* **Python-JOSE** – JWT handling
* **Pydantic v2** – Data validation
* **dotenv** – Environment variable management

---

## 📂 Project Structure

```bash
fastapi-jwt-auth/
│── app/
│   ├── main.py          # Entry point
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # DB connection setup
│   ├── auth.py          # Authentication logic
│   └── utils.py         # Utility functions (hashing, token gen)
│
│── venv/                # Virtual environment
│── requirements.txt     # Project dependencies
│── .env                 # Environment variables
│── README.md            # Project documentation
```

---

## ⚙️ Installation

1️⃣ Clone the repository:

```bash
git clone https://github.com/engripaye/fastapi-jwt-auth.git
cd fastapi-jwt-auth
```

2️⃣ Create & activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

4️⃣ Set up environment variables:
Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./test.db
```

---

## ▶️ Running the Application

Start the FastAPI server with **Uvicorn**:

```bash
uvicorn app.main:app --reload
```

Your API will be available at:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

Interactive API docs:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔑 Example API Endpoints

| Method | Endpoint     | Description                    |
| ------ | ------------ | ------------------------------ |
| POST   | `/register`  | Register a new user            |
| POST   | `/token`     | Login & get JWT tokens         |
| GET    | `/users/me`  | Get current authenticated user |
| GET    | `/protected` | Example protected endpoint     |

---

## 🧪 Testing

You can test endpoints with **cURL** or **Postman**. Example login request:

```bash
curl -X POST "http://127.0.0.1:8000/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=testuser&password=testpassword"
```

---

## 🚀 Future Improvements

* ✅ OAuth2 Social Logins (Google, GitHub, etc.)
* ✅ Refresh Token Rotation
* ✅ Email Verification & Password Reset
* ✅ Docker & CI/CD Setup

---

## 📜 License

This project is licensed under the **MIT License**.

---
