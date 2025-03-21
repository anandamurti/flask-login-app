import os
import pymysql
from flask import Flask, flash, redirect, render_template, request, session, url_for

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.secret_key = "30644188fd9f065dba1c40ccfca634ed"

# Logging configuration
log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'error.log')
handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("Successfully logged in")
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = "Incorrect username and password"
            app.logger.warning("Incorrect username and password for user (%s)",
                               request.form.get('username'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


def valid_login(username, password):
    # Retrieve database configuration from environment variables
    MYSQL_DATABASE_HOST = os.environ.get('localhost')
    MYSQL_DATABASE_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_DATABASE_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Hmpyjv347&')
    MYSQL_DATABASE_DB = 'my_flask_app'

    # Establish a database connection
    conn = pymysql.connect(
        host=MYSQL_DATABASE_HOST,
        user=MYSQL_DATABASE_USER,
        password=MYSQL_DATABASE_PASSWORD,
        db=MYSQL_DATABASE_DB
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username ='%s' AND password = '%s'" % (username, password))
    data = cursor.fetchone()

    if data:
        return True

    try:
        with conn.cursor() as cursor:
            # Execute a query to check for matching username and password
            sql = "SELECT * FROM user WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            return data is not None
    finally:
        conn.close()



if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=5000)
