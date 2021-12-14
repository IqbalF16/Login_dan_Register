from flask import Flask, render_template, redirect, url_for, request

from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'pdam'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/daftar')
def my_form():
    return render_template('.html')

@app.route('/', methods=['GET', 'POST'])
def Authenticate():

	username = request.form['u']
	password = request.form['p']
	cursor = mysql.connect().cursor()
	cursor.execute("select * from user where username='" + username + "' and password='" + password + "'")
	data = cursor.fetchone()
	if data is None:
		return "Username atau password anda salah"
	else:
		return "login berhasil"

if __name__ == '__main__':
    app.run()




