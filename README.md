# ALX Travel App API
The alxtravelapp project is a real-world Django application that serves as the foundation for a travel listing platform. This milestone focuses on setting up the initial project structure, configuring a robust database, and integrating tools to ensure API documentation and maintainable configurations.

## Project Structure
The project is organized into several key directories and files:
```bash
alxtravelapp/
    ├── alx_travel_app/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── development.py
    │   │   └── production.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── listings/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    ├── docs/
    │   └── api_documentation.md
    ├── .gitignore
    ├── .env.example
    ├── .env
    │
    └── requirement.txt

```

## Key Features
- **Django Framework**: Utilizes Django for rapid development and clean, pragmatic design.
- **MySQL Database**: Configured to use MySQL for robust data management.
- **Environment Variables**: Uses `django-environ` to manage sensitive settings and configurations.
- **API Documentation**: Integrated tools for generating and maintaining API documentation.
- **Swagger Integration**: Set up Swagger using `drf-yasg` for interactive API documentation.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone
    cd alxtravelapp
    ```
2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install Dependencies**:
    ```bash
    pip install -r requirement.txt
    ```
4. **Configure Environment Variables**:
Create a `.env` file in the root directory and populate it with the necessary environment variables. You can refer to the `.env.example` file for guidance.
5. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```
6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
7. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/swagger` to see the application in action.
