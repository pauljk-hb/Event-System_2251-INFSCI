# EventManager

EventManager is a Django-based application for managing events and event signups.

## Prerequisites

- Python 3.12
- pip (Python package installer)
- Virtual environment (optional but recommended)

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

---------In the moment we are just here!!!!!!!---------

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
