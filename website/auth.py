from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		if len(username) == 0:
			flash('Username cannot empty.', category='error')
		elif len(password) == 0:
			flash('Password cannot empty.', category='error')
		else:
			# log in user
			flash('Successfully logged in!')
	return render_template('login.html', text="Test")

@auth.route('/sign_up', methods=['GET','POST'])
def sign_up():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		confirm_password = request.form.get('confirm-password')
		api_token = request.form.get('api-token')
		domain = request.form.get('domain')
		if len(username) == 0:
			flash('Username cannot empty.', category='error')
		elif len(password) == 0:
			flash('Password cannot empty.', category='error')
		elif password != confirm_password:
			flash('Passwords must match.', category='error')
		elif len(api_token) == 0:
			flash('API token cannot empty.', category='error')
		elif len(domain) == 0:
			flash('Organization domain cannot empty.', category='error')
		else:
			new_user = User(username=username, password=generate_password_hash(password, method='sha256'), api_token=api_token, domain=domain)
			db.session.add(new_user)
			db.session.commit()
			flash('Account created!', category='success')
			return redirect(url_for('pages.home'))
			
	return render_template('sign_up.html')

@auth.route('/logout')
def logout():
	return '<h1>Logout</h1>'
