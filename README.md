Flask MySQL Authentication App

A simple Flask web application that demonstrates user authentication (login and logout) with session management and flash messages. The app connects to a MySQL database using the PyMySQL driver. This project serves as a basic template for implementing user login functionality in Flask with a database backend.
Features
User Authentication: Users can log in and log out using a username and password. Session management keeps users logged in across requests.
Sessions: Utilizes Flask session to store user data (e.g., user ID) after login, allowing page access control for authenticated users.
Flash Messages: Provides feedback messages (using flask.flash) for events like login success, login failure, and logout.
MySQL Database Integration: Uses a MySQL database to store user credentials and other data, connected through the PyMySQL client library.
Environment Configuration: Supports configuration via environment variables (using a .env file for convenience), including database credentials and secret keys.
Technologies Used
Python 3.x – Programming language for the project
Flask – Python micro web framework used to create the web application
PyMySQL – MySQL database connector for Python (pure Python MySQL client)
MySQL – Relational database management system for storing user data
HTML/CSS (Jinja2 templates) – For front-end structure and styling of the web pages
Optional: python-dotenv – To load environment variables from a .env file (if not using Flask's built-in loading)
Setup Instructions
Follow these steps to set up and run the Flask application on your local machine:
Clone the Repository: Clone this repository to your local machine using Git or download the ZIP.

git clone https://github.com/anandamurti/flask-login-app.git
cd flask-login-app
Create Virtual Environment (Optional): It’s recommended to use a Python virtual environment for project dependencies.

python3 -m venv venv
source venv/bin/activate   # On Windows use "venv\Scripts\activate"
Install Dependencies: Install the required Python packages using pip.

pip install -r requirements.txt

This will install Flask, PyMySQL, and any other dependencies listed.
Configure the Database: Ensure you have MySQL installed and running. Create a new MySQL database and a user with appropriate privileges for this app. For example, via MySQL CLI or a tool like phpMyAdmin:

CREATE DATABASE flask_app_db;
CREATE USER 'flask_user'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON flask_app_db.* TO 'flask_user'@'localhost';
FLUSH PRIVILEGES;
Replace flask_app_db, flask_user, and secure_password with your database name, MySQL username, and a strong password.
Environment Variables: Set up your environment variables for configuration. You can create a .env file in the project root (see the Configuration section below for an example structure). At minimum, define the following in the environment or .env:
Flask settings: FLASK_APP, FLASK_ENV, and a SECRET_KEY for sessions.
Database settings: DB_HOST, DB_USER, DB_PASSWORD, DB_NAME (and optionally DB_PORT if not default).
Run Database Migrations (if any): If this project includes a database migration or setup script (such as an SQL file to create tables), run that to initialize the database. For example, you might import a .sql schema or use Flask CLI commands. (If the project uses a simple script to create tables, run that script. Otherwise, ensure the users table is created in the database.)
Run the Application: Start the Flask development server.

flask run
Make sure the environment variable FLASK_APP is set to the entry-point of the app (e.g., app.py). You can also run the app directly with Python:

python app.py
This will start the server at http://127.0.0.1:5000/ by default.
Access the App: Open your web browser and navigate to http://127.0.0.1:5000/. You should see the home page or login page of the application. Try logging in with credentials that exist in your MySQL database (or create a test user directly in the database to test).
Configuration
The application uses environment variables for configuration. An example .env file is shown below. You should create a file named .env (or configure these variables in your OS) with your own settings:

# .env example for Flask MySQL Authentication App

# Flask settings
FLASK_APP=app.py
FLASK_ENV=development   # use 'production' in a production environment
SECRET_KEY=your_secret_key_here   # replace with a strong secret key

# MySQL database credentials
DB_HOST=localhost
DB_PORT=3306
DB_USER=flask_user
DB_PASSWORD=secure_password
DB_NAME=flask_app_db
SECRET_KEY: Used by Flask to sign session cookies and for security. Generate a random complex string for production.
DB_HOST/DB_PORT: Host and port where your MySQL server is running. (3306 is the default MySQL port.)
DB_USER/DB_PASSWORD: The MySQL username and password for the account that has access to the database.
DB_NAME: Name of the MySQL database to use for the app.
Ensure this .env file is kept secret (do not commit it to version control) since it contains sensitive credentials. The application will load these variables at runtime to configure the database connection and other settings.

Project Structure
Below is a simplified overview of the project structure (directories and files):

flask-auth-app/
├── app.py               # Main Flask application file (routes and app setup)
├── auth.py              # (Optional) Module for authentication functions (if used)
├── static/              # Static files (CSS, JS, images)
│   └── ...             
├── templates/           # HTML templates for the Flask app
│   ├── base.html        # Base template with common layout
│   ├── login.html       # Login page template
│   └── dashboard.html   # Example protected page (shown after login)
├── requirements.txt     # Python dependencies for the project
├── .env.example         # Example environment variables file (if provided)
└── README.md            # Project documentation (this file)

Note: The actual file names and structure may vary. For instance, all routes and logic might be in app.py for a simple app, or separated into multiple modules (such as auth.py for authentication-related functions). The templates folder contains Jinja2 HTML templates for pages like login and any other pages (e.g., a dashboard or home page). The static folder would hold any static assets like CSS or JavaScript files.

Author
Developed by Ananda Murti. Feel free to contact me or open an issue on GitHub for any questions or feedback regarding this project.
