from flask import *
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from classes.forms import RegistrationForm

app = Flask("__app__")
app.config['SECRET_KEY'] = 'a551d32359baf371b9095f28d45347c8b8621830'
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
	return user.fetch_userid(int(user_id))

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
		user1 = User(request.form['username'], hashed, request.form['email'], 'default.jpg')
		user1.upload()
		flash(f'Account created for {form.username.data}! Now log in', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Registration', form=form)

app.run(debug=True)    