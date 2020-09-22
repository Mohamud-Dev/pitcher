from flask import render_template, redirect, url_for,abort
from . import main
from flask_login import login_required
from ..models import User, Pitches

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

@main.route('/pitches/new/<int:id>', methods = ['GET','POST'])
@login_required

def new_pitch(self, id):
    form = PitchForm
    if form.validate_on_submit():
        pitch = form.description.data
        owner = current_user._get_current_object()
        category = form.category.data

        pitch = Pitch(pitch=form.pitch.data, owner=current_user._get_current_object(),category=form.category.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.home'))
    pitches = Pitch.query.order_by(Pitch.all())

    return render_template('pitch.html',form=form, pitches=pitches)

@main.route('/pitches/pitch_categories/')
def categories():
    product = Pitch.query.filter_by(category="product pitch").all()
    promotion = Pitch.query.filter_by(category="promotion pitch").all()
    pickupline = Pitch.query.filter_by(category="pickupline pitch").all()
    interview = Pitch.query.filter_by(category="interview pitch").all()
    return render_template('home.html',pickup=pickupline,interview=interview,product=product,promotion=promotion)


