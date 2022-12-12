from flask import Flask, render_template, request, session, url_for
from flask_mysqldb import MySQL
import re
 
 
app = Flask(__name__)
 
 
app.secret_key = 'your secret key'
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'bhargavi'
app.config['MYSQL_PASSWORD'] = 'Password!23'
app.config['MYSQL_DB'] = 'logins'
 
 
mysql = MySQL(app)
 
 
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'user_id' in request.form and 'password' in request.form:
        user_id = request.form['user_id']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE user_id = % s AND password = % s', (user_id, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('unique_id.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('indexindex1.html', msg = msg)
