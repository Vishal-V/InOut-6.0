from flask import *
from classes.User import User
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from classes.forms import RegistrationForm, LoginForm, PostForm
from flask_bcrypt import Bcrypt
import tensorflow as tf

app = Flask("__app__")
app.config['SECRET_KEY'] = 'a551d32359baf371b9095f28d45347c8b8621830'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.fetch_userid(int(user_id))

@app.route("/login", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Check if password hashes match
        user = User.fetch(form.email.data)

        if user:
            validate = bcrypt.check_password_hash(user.password, form.password.data)
            if validate:
                login_user(user)
                return redirect(url_for('profile'))
            else:
                flash(f'Password incorrect. Login unsuccessful', 'danger')
                return redirect(url_for('login'))

        else:
            flash(f'User does not exist', 'danger')
            return redirect(url_for('register'))
    else:
        return render_template("login.html", title='Login', form=form)


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


@app.route("/profile", methods=['GET', 'POST'])
# @login_required
def profile():
	form = PostForm()
	if form.validate_on_submit():
		url = ''
		now = datetime.datetime.now().strftime("%H:%M %d-%m-%y")
		post = Post(current_user.username, form.title.data, form.content.data, now, url, current_user.profile_pic)
		post.upload()
		socketio.emit("newPost", include_self=True)
		return redirect(url_for('home'))

	return render_template('post.html', title='Post', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

app.run(debug=True)    