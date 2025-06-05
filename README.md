```markdown
# 📁 Files Management System API

A RESTful **File Management System** built with **Django** and **Django REST Framework (DRF)**. This backend allows users to upload files, organize them into folders, and navigate a structured file system hierarchy — all through API endpoints.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![DRF](https://img.shields.io/badge/DRF-3.14-orange)

---

## 🧩 Features

- 📂 Create and manage folders
- 📎 Upload files into specific folders
- 📁 Nested folder hierarchy support
- 🧾 List files and folders
- ✅ Token-based authentication for API access
- 👨‍💼 Admin interface for managing resources

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: Token-based (via DRF's default token auth)
- **Database**: SQLite (default, customizable)
- **Others**: DRF serializers, class-based views

---

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/kadour22/files_managments_system.git
   cd files_managments_system
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**:

   ```bash
   python manage.py runserver
   ```

---

## 🔑 Authentication

This API uses **Token Authentication**.

- Obtain token:
  ```
  POST /api/token-auth/
  ```

Include the token in headers for authorized requests:

```
Authorization: Token <your_token>
```

---

## 📂 API Overview (Examples)

| Method | Endpoint               | Description                  |
|--------|------------------------|------------------------------|
| POST   | `/api/token-auth/`     | Get user auth token          |
| GET    | `/api/folders/`        | List all folders             |
| POST   | `/api/folders/`        | Create a new folder          |
| GET    | `/api/files/`          | List all uploaded files      |
| POST   | `/api/files/`          | Upload a file to a folder    |

> Use DRF's browsable interface or Postman to explore the full API.

---

## 🖼️ Admin Panel

Access the Django admin interface:

```
http://127.0.0.1:8000/admin/
```

Use the credentials of the superuser created earlier.

---

## 🧾 Folder Structure

```
files_managments_system/
├── files_app/          # Core app for file & folder logic
│   ├── models.py       # Folder and File models
│   ├── serializers.py  # DRF serializers
│   ├── views.py        # API views
│   └── urls.py         # API URL patterns
├── files_managments_system/  # Django project settings
├── manage.py
└── requirements.txt
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Kadour22**

- GitHub: [@kadour22](https://github.com/kadour22)

