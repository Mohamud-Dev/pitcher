from flask import render_template, redirect, url_for
from . import main

@main.route('/')
def index():
    title="Welcome to PITCHER"
    return render_template('index.html', title=title)