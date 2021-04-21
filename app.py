import mysql.connector
from flask import Flask, flash
from flask import request, render_template, redirect, url_for
from database import *
import smtplib

app = Flask(__name__)

@app.route("/")
def home_page():

	return render_template('main_menu.html')

@app.route("/search", methods=["POST", "GET"])
def search_page():
	status = None
	if request.method == "POST" and status == None:
		major = request.form["major"]
		country = request.form["country"]
		price = request.form["price"]

		universities = search_universities(country, major, price)
		#print(universities)
		if universities != []:
			'''
			import base64
			from PIL import Image
			import io

			mydb = mysql.connector.connect(
						host='192.168.0.23',
						user='pi',
						passwd='1234',
						database='Test',
					)

			cursor = mydb.cursor()
			query = 'SELECT picture FROM Universities WHERE ID=22'
			cursor.execute(query)
			data = cursor.fetchall()

			image = data[0][0]


			b64 = base64.b64encode(image)

			#image = base64.b64decode(Image.open(io.BytesIO(binary_data)))
			'''
			import os
			PEOPLE_FOLDER = os.path.join('static', 'pictures')
			app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
			full_filename = []
			files = []
			status = True
			#for x in universities:
				#files.append(x + ".png")

			#	data = x[0] + ".png"

			#	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], data)
			#	files.append(full_filename)
				#files.append("C:\Programing 2.0\vs code\python\our_site\static\pictures\x[0] + ".png")
			#print(files)
			#full = os.path.join(app.config['UPLOAD_FOLDER'], files[0])
			#full_filename.append(full)
			#universities.append(files)
			i = 0
			for x in universities:
				data = x[0] + ".png"

				full_filename = os.path.join(app.config['UPLOAD_FOLDER'], data)
				#files.append(full_filename)
				universities[i] =list(universities[i])
				universities[i].append(full_filename)
				print(universities[i])
				i=i+1

			print("\n\n\n")
			names = []
			for x in universities:
				names.append(x[0])
			print("\n\n\n")
			
			return render_template('result.html', text1 = universities, user_image=full_filename, text2 = "..\static\pictures\a.png", files = files, names = names)

		if request.method == "POST" and status == True:
			selected_uni =request.form["select_uni"]
			print(selected_uni)
		else:
			return render_template('result.html')
	return render_template('search.html')

@app.route("/contact", methods=["POST", "GET"])
def contact_page():
    email = "and.met.ezh@gmail.com"
    message = "We like your website so much !"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("service.official.uni.finder@gmail.com", "#e27d60#e27d60")
    server.sendmail("service.official.uni.finder@gmail.com", email, message)

    return render_template('contact.html')

@app.route("/result", methods=["POST", "GET"])
def result_page():
	print(universities)
	return render_template('result.html')

@app.route("/about", methods=["POST", "GET"])
def about_page():
	return render_template('about.html')




@app.route('/login', methods=["POST", "GET"])
def log_in_page():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		print(email, password)
		result = log_in(email, password)
		if result == None:
			flash("Incoreect info")
		else:
			return render_template("main_menu.html")
	return render_template('login.html')



@app.route('/signup', methods=["POST", "GET"])
def sign_up_page():
	if request.method == 'POST':
		username = request.form.get('username')
		email = request.form.get('email')
		password = request.form.get('password')
		result = sign_up(username, email, password)
		if result == True:
			flash('You were successfully logged in', category='error')
			return redirect(url_for('log_in_page'))
		else:
			flash('Incorrect information', category='error')

	return render_template('signup.html')


@app.route('/logout', methods=["POST", "GET"])
def log_out_page():
	flash("something")
	return render_template('login.html')

@app.route('/profile')
def profile_page():
	print("losogo dete")
	return render_template('profile.html')

@app.route('/add')
def add_favourite():
	print("losogo dete")

	return redirect(url_for('profile_page'))


if __name__ == "__main__":
	app.secret_key = 'key123'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(debug=True)