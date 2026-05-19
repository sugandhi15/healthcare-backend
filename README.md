Healthcare Management Backend System

A secure and scalable RESTful backend for managing healthcare records, built with Django, Django REST Framework, PostgreSQL, and JSON Web Token authentication.

Features
User Registration and Login
JWT Authentication (Access and Refresh Tokens)
Patient CRUD APIs
Doctor CRUD APIs
Patient–Doctor Mapping APIs
PostgreSQL Database Integration
Serializer Validation and Error Handling
Environment Variable Configuration
RESTful API Design
Tech Stack
Python 3.11+
Django
Django REST Framework
PostgreSQL
Simple JWT
Neon (cloud-hosted PostgreSQL)
Postman
Project Structure
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
API Modules
Authentication APIs
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/refresh/
Patient APIs
POST /api/patients/
GET /api/patients/
GET /api/patients/<id>/
PUT /api/patients/<id>/
PATCH /api/patients/<id>/
DELETE /api/patients/<id>/
Doctor APIs
POST /api/doctors/
GET /api/doctors/
GET /api/doctors/<id>/
PUT /api/doctors/<id>/
PATCH /api/doctors/<id>/
DELETE /api/doctors/<id>/
Mapping APIs
POST /api/mappings/
GET /api/mappings/
GET /api/mappings/<patient_id>/
DELETE /api/mappings/delete/<mapping_id>/
Installation and Setup
1. Clone the Repository
git clone <repository-url>
cd healthcare
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment
Windows (PowerShell)
venv\Scripts\Activate.ps1
Windows (Command Prompt)
venv\Scripts\activate
Linux/macOS
source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Create .env File
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-neon-postgresql-url
6. Apply Migrations
python manage.py makemigrations
python manage.py migrate
7. Run the Development Server
python manage.py runserver
Authentication

Login returns access and refresh tokens:

{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}

Use the access token in the Authorization header:

Authorization: Bearer <access_token>
Error Handling and Validation

The API includes:

Serializer-based validation
Email validation
Unique constraint checks
Custom validations (age, password, experience)
Authentication and permission handling
Standard HTTP status codes

Common status codes:

200 OK
201 Created
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
Database Models
User – Custom user model with name and email
Patient – Stores patient information created by users
Doctor – Stores doctor details
PatientDoctorMapping – Many-to-many relationship between patients and doctors
Testing

All endpoints can be tested using Postman or similar API clients.

Deployment Notes

The project is configured to work with Neon for cloud-hosted PostgreSQL, but can be deployed to any environment that supports Django and PostgreSQL.

Author

Sugandhi Bansal
Backend Developer | Django | Python | PostgreSQL | REST APIs | Blockchain Enthusiast