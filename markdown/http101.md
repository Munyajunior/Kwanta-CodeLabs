# 🌐 Networking Series \[Lesson 1] — Understanding HTTP Methods

_📡 Powered by KwantaBit CodeLab_

---

## 💡 What is HTTP?

**HTTP (HyperText Transfer Protocol)** is the foundation of data exchange on the web.
Every time you **open a website**, **submit a form**, or **use an app**, you’re using **HTTP requests and responses** behind the scenes.

---

## 🚦 HTTP Methods – The Core Verbs of the Web

HTTP methods define **what action** you want to perform on a resource.

### 🔹 1. **GET**

- 📥 _Retrieve_ data from the server
- ✅ Safe and idempotent (doesn’t change anything)
- 🔍 Used in browsers, fetch(), axios, etc.

```bash
GET /users
```

### 🔹 2. **POST**

- 📤 _Create_ a new resource on the server
- 🔄 Changes state (e.g., saving to DB)

```bash
POST /register
```

### 🔹 3. **PUT**

- 🔁 _Replace_ an existing resource completely

```bash
PUT /users/3
```

### 🔹 4. **PATCH**

- ✏️ _Update_ part of a resource (partial update)

```bash
PATCH /users/3
```

### 🔹 5. **DELETE**

- 🗑️ _Remove_ a resource

```bash
DELETE /users/3
```

---

## 🧑🏽‍💻 Real-World Usage in Services & Apps

| App Feature   | HTTP Method        | Example            |
| ------------- | ------------------ | ------------------ |
| View Profile  | `GET /profile`     | Read data          |
| Sign Up       | `POST /register`   | Create account     |
| Edit Settings | `PATCH /settings`  | Partial update     |
| Save Document | `PUT /docs/12`     | Full overwrite     |
| Delete Post   | `DELETE /posts/10` | Remove from server |

> ⚠️ Choosing the right method improves **performance**, **security**, and **predictability**.

---

## ⚙️ FastAPI & HTTP Methods — Modern API Design

FastAPI is a **Python web framework** for building APIs that are:

- 🔥 Super fast (using ASGI + Starlette)
- 🧠 Intuitive (thanks to Python type hints)
- ⚡ Asynchronous-ready
- 📃 Auto-generates Swagger docs

### ✅ Sample FastAPI Code:

```python
from fastapi import FastAPI

app = FastAPI()

# GET - Read data
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

# POST - Create new user
@app.post("/users/")
def create_user(user: dict):
    return {"msg": "User created", "data": user}

# PUT - Full update
@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    return {"msg": "User updated", "id": user_id}

# PATCH - Partial update
@app.patch("/users/{user_id}")
def partial_update(user_id: int, user: dict):
    return {"msg": "Partially updated"}

# DELETE - Remove
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"msg": "User deleted"}
```

---

## 📈 Why FastAPI is Perfect for High-Performance APIs

✅ **Async/Await** support — handle thousands of requests concurrently
✅ **Automatic validation** — thanks to Pydantic models
✅ **Interactive API Docs** — Swagger UI (open `/docs`)
✅ **Schema enforcement** — avoid breaking frontend/backend sync
✅ **Built-in security features** — OAuth2, JWT, etc.

---

## 🧪 Test With cURL or Postman

```bash
curl -X GET http://localhost:8000/users/5
curl -X POST http://localhost:8000/users/ -H "Content-Type: application/json" -d '{"name": "Khalid"}'
```

---

## 🛡 Tips for Better HTTP API Design

- Use `GET` only for fetching — never for actions like delete or save
- Use `POST` for creating, `PUT/PATCH` for updating
- Send proper **status codes** (`200`, `201`, `404`, `500`, etc.)
- Add rate limits and authentication to protect routes

---

## 🚀 Next in the Networking Series

1. ✅ HTTP Methods – Concepts + FastAPI Usage
2. 📡 HTTP Headers, Cookies & Caching
3. 🔐 REST vs. GraphQL
4. 🧩 WebSockets, Streaming & Real-time APIs
5. 🛠️ Build a Chat API (Async) with FastAPI

---

📲 _This is how modern APIs are built. It all starts with knowing your HTTP verbs._
📌 _Save this post. Practice these methods. Tomorrow we go deeper._

\#KwantaBit #FastAPI #Networking #HTTP #WebDev #Backend #CodeLab #RESTfulAPI #KwantaBitCodeLab
