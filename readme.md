# EventManager

EventManager is a Django-based application for managing events and event signups.

## Project Structure

```
EventManager/
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── events/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── searchbox/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── EventManager/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3
├── requirements.txt
└── readme.md
```

## Prerequisites

- Python 3.12
- pip (Python package installer)
- Virtual environment (optional but recommended)

## Installation

### Clone the repository:

```sh
git clone <repository-url>
cd EventManager
```

### Create a virtual environment:

```sh
python -m venv env
```

### Activate the virtual environment:

On Windows:

```sh
.\env\Scripts\activate
```

On macOS and Linux:

```sh
source env/bin/activate
```

### Install the required packages:

```sh
pip install -r requirements.txt
```

### Apply database migrations:

```sh
python manage.py migrate
```

### Seed the Database:

```sh
python manage.py seed
```

## Running the Application

### Start the development server:

```sh
python manage.py runserver
```

### Access the application:

Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Access the admin interface:

Open your web browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the superuser credentials you created earlier.
