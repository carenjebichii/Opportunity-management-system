from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, login_required, logout_user
from . import auth
from .forms import LoginForm, RegistrationForm
from ..main.models import User


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash("Invalid username or password")
    return render_template("auth/login.html", form=form)


@auth.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        user.save()
        flash("Registration successfull")
        return redirect(url_for('auth.login'))
    return render_template("auth/register.html", form=form)

@auth.route("/logout",methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
