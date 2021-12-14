from flask import Flask, render_template, redirect, url_for, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'py_iqbal'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
con=mysql.connect()
cursor=con.cursor()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def Authenticate():

	username = request.form['u']
	password = request.form['p']
	cursor.execute("select * from user where username='" + username + "' and password='" + password + "'")
	data = cursor.fetchone()
	print(data)
	if data is None:
		return render_template('index.html', alert('username atau password anda salah'))
	else:
		return redirect('/penjualan1')

@app.route('/penjualan1')
def penjualan1():
    return render_template('penjualan.html')

@app.route('/daftar')
def daftar():
    return render_template('formulir_pendaftaran.html')


@app.route('/register',methods=['POST'])
def register():
	name = request.form['name']
	username = request.form['username']
	password = request.form['password']
	cursor.execute("insert into user values ('',%s,%s,%s)",(name,username,password))
	con.commit()
	return redirect('/')

@app.route('/penjualan',methods=['POST'])
def penjualan():
	barang = request.form['barang']
	harga_jual = request.form['harga_jual']
	stok = request.form['stok']
	cursor.execute("insert into penjualan values ('',%s,%s,%s)",(barang,harga_jual,stok))
	con.commit()
	return "successfully registered"

if __name__ == '__main__':
    app.run()
