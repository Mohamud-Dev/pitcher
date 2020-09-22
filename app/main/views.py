from flask import render_template, redirect, url_for
from . import main
from flask_login import login_required

@main.route('/')
def index():
    title="Welcome to PITCHER"
    return render_template('index.html', title=title)


@main.route('/pitches/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):