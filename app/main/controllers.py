from flask import Blueprint, render_template, redirect, url_for,flash
from flask_login import current_user, login_required

from app.main.models import Account, Stage, Opportunity

from . import main
from .forms import AccountForm


@main.route("/")
@login_required
def index():
    return render_template("index.html")


@main.route("/user/<username>", methods=["GET"])
def user(username):
    return redirect(url_for('main.index'))


@main.route("/accounts", methods=['GET', 'POST'])
def accounts():
    accounts = Account.query.all()
    return render_template("accounts.html", accounts=accounts)

@main.route("/create-accounts",methods=['GET','POST'])
def create_account():
    form = AccountForm()
    if form.validate_on_submit():
        if Account.query.filter_by(name=form.name.data).first():
            flash("The account with than name already exists please try again")
            return redirect(url_for('main.create-accounts'))
        account = Account(name=form.name.data)
        account.save()
        flash("Account created successfully")
        return redirect(url_for('main.accounts'))
    return render_template("create-account.html", form=form)

