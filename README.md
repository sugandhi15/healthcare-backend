# Healthcare Management Backend System

A secure and scalable RESTful backend for managing healthcare records, built with Django, Django REST Framework, PostgreSQL, and JSON Web Token (JWT) authentication.

---

📄 **API Documentation:** [View Complete API Documentation](https://documenter.getpostman.com/view/37031551/2sBXqRkxD6)

## Features

- User Registration and Login
- JWT Authentication (Access and Refresh Tokens)
- Patient CRUD APIs
- Doctor CRUD APIs
- Patient–Doctor Mapping APIs
- PostgreSQL Database Integration
- Serializer Validation and Error Handling
- Environment Variable Configuration
- RESTful API Design

---

## Tech Stack

- Python 3.11+
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- Neon (Cloud-hosted PostgreSQL)
- Postman

---

## Project Structure

```text
healthcare/
│── healthcare/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│── accounts/
│── patients/
│── doctors/
│── mappings/
│
│── manage.py
│── requirements.txt
│── .env
│── README.md
```

---

## API Modules

### Authentication APIs

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/auth/refresh/`

### Patient APIs

- `POST /api/patients/`
- `GET /api/patients/`
- `GET /api/patients/<id>/`
- `PUT /api/patients/<id>/`
- `PATCH /api/patients/<id>/`
- `DELETE /api/patients/<id>/`

### Doctor APIs

- `POST /api/doctors/`
- `GET /api/doctors/`
- `GET /api/doctors/<id>/`
- `PUT /api/doctors/<id>/`
- `PATCH /api/doctors/<id>/`
- `DELETE /api/doctors/<id>/`

### Mapping APIs

- `POST /api/mappings/`
- `GET /api/mappings/`
- `GET /api/mappings/<patient_id>/`
- `DELETE /api/mappings/delete/<mapping_id>/`

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd healthcare
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` File

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-neon-postgresql-url
```

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

---

## Authentication

After successful login, the API returns access and refresh tokens:

```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

Use the access token in the request header:

```http
Authorization: Bearer <access_token>
```

---

## Error Handling and Validation

The API includes:

- Serializer-based validation
- Email validation
- Unique constraint checks
- Custom validations (age, password, experience)
- Authentication and permission handling
- Standard HTTP status codes

### Common HTTP Status Codes

- `200 OK`
- `201 Created`
- `204 No Content`
- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`
- `404 Not Found`

---

## Database Models

- **User** – Custom user model with name and email
- **Patient** – Stores patient information created by users
- **Doctor** – Stores doctor details
- **PatientDoctorMapping** – Many-to-many relationship between patients and doctors

---

## Testing

All API endpoints can be tested using Postman or any REST API client.

---

## Deployment Notes

The project is configured to work with Neon for cloud-hosted PostgreSQL, but it can be deployed to any environment that supports Django and PostgreSQL.

---

## Author

**Sugandhi Bansal**  
Backend Developer | Django | Python | PostgreSQL | REST APIs | Blockchain Enthusiast
```