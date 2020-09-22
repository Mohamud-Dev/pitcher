from flask import render_template, redirect, url_for,abort
from . import main
from flask_login import login_required
from ..models import User

@main.route('/')
def index():
    title="Welcome to PITCHER"
    return render_template('index.html', title=title)


@main.route('/pitches/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    return render_template('comments.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
