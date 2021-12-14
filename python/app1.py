from flask import Flask, render_template, redirect, request
from flaskext.mysql import MySQL

app = Flask(_name_)
mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'pdam'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        details = request.form
        name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    cursor.execute("insert into user values ('',%s,%s,%s)",(name,username,password))
    conn.commit()
        # return 'success'
    return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)