from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name pass it to home.html using the home function/route in app.py.

	static_folder='static'  # Name of directory for static files
)


username = "Noamgarti"
password = "Pinetwork31415"
facebook_friends=["Yuval","Roei","Omar", "George","Bob"]


@app.route('/',methods = ['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		if username == request.form['username'] and password == request.form['password']: 
			return render_template('home.html',facebook_friends = facebook_friends)
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/friend_exists/<string:friend>',methods = ['GET','POST'])  # '/' for the default page
def friend_exists(friend):
	if friend in facebook_friends:
		return render_template('friend_exists.html')
	else:
		return 'FALSE'








if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
  debug=True
	)