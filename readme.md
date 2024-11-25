# EventManager

EventManager is a Django-based application for managing events and event signups.

## Prerequisites

- Python 3.12
- pip (Python package installer)
- Virtual environment (optional but recommended)

## Project Management

- Anu -> Filter Functions, Filter Site
- Jacob -> Auth Function, nessesary Sites
- Paul -> Event CRUD Functions, Sites

- [Design File](https://www.figma.com/design/3lYgoCyFllLugdj6BnF5iQ/Event-System-Python?node-id=0-1&node-type=canvas&t=MxmIjfFcAuDilQHE-0)

For every functions you should create an seperate App (for example for the Auth an Auth App or the Filter an FilterApp)

#### Create an App

To create a new app in Django, follow these steps:

1. **Create the app:**

   Navigate to your project directory and run the following command:

   ```sh
   python manage.py startapp <app_name>
   ```

   Replace `<app_name>` with the name of your app.

2. **Add the app to your project:**

   Open the `settings.py` file in your project directory and add your new app to the `INSTALLED_APPS` list:

   ```python
   INSTALLED_APPS = [
       ...
       '<app_name>',
   ]
   ```

3. **Create views and templates:**

   Define your views in the `views.py` file and create corresponding templates in the `templates` directory of your app. For example:

   ```python
   from django.shortcuts import render
   from .models import Event

   def event_list(request):
       events = Event.objects.all()
       return render(request, 'event_list.html', {'events': events})
   ```

   Create a template file `event_list.html` in the `templates` directory:

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>Event List</title>
     </head>
     <body>
       <h1>Events</h1>
       <ul>
         {% for event in events %}
         <li>{{ event.name }} - {{ event.date }} - {{ event.location }}</li>
         {% endfor %}
       </ul>
     </body>
   </html>
   ```

4. **Configure URLs:**

   Create a `urls.py` file in your app directory and define the URL patterns for your views:

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('events/', views.event_list, name='event_list'),
   ]
   ```

   Include your app's URLs in the project's `urls.py` file:

   ```python
   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('<app_name>.urls')),
   ]
   ```

By following these steps, you can create and configure a new app in your Django project.

## Installation

1. **Clone the repository:**

   ```sh
   git clone <repository-url>
   cd EventManager
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv env
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```sh
     .\env\Scripts\activate
     ```

   - On macOS and Linux:

     ```sh
     source env/bin/activate
     ```

4. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

5. **Apply database migrations:**

   ```sh
   python manage.py migrate
   ```

6. **Create a superuser (admin user):**

   ```sh
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

## Running the Application

1. **Start the development server:**

   ```sh
   python manage.py runserver
   ```

2. **Access the application:**

   Open your web browser and go to [http://127.0.0.1:8000/](http://_vscodecontentref_/0).

3. **Access the admin interface:**

   Open your web browser and go to [http://127.0.0.1:8000/admin/](http://_vscodecontentref_/1) and log in with the superuser credentials you created earlier.

## Running Tests

To run the tests, use the following command:

```sh
python manage.py test
```
