from flask import render_template, redirect, url_for,abort
from . import main
from flask_login import login_required
from ..models import User, Pitches, Comment

@main.route('/')
def index():
    title="Welcome to PITCHER"
    pitch = Pitches.query.filter_by().first()
    pickuplines = Pitches.query.filter_by(category="pickuplines")
    interviewpitch = Pitches.query.filter_by(category = "interviewpitch")
    promotionpitch = Pitches.query.filter_by(category = "promotionpitch")
    productpitch = Pitches.query.filter_by(category = "productpitch")
    

    return render_template('index.html', title=title,pitch = pitch, pickuplines=pickuplines, interviewpitch= interviewpitch, promotionpitch = promotionpitch, productpitch = productpitch)


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
        description = form.description.data
        owner = current_user._get_current_object()
        category = form.category.data

        pitch = Pitch(description=form.description.data, owner=current_user._get_current_object(),category=form.category.data)
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
    return render_template('categories.html',pickup=pickupline,interview=interview,product=product,promotion=promotion)



