from flask import render_template, redirect, url_for,abort
from . import main
from flask_login import login_required
from ..models import User, Pitches, Comment
from .forms import PitchForm

@main.route('/')
def index():
    title="Welcome to PITCHER"
    pitch = Pitches.query.filter_by().first()
    pickuplines = Pitches.query.filter_by(category="pickuplines")
    interviewpitch = Pitches.query.filter_by(category = "interviewpitch")
    promotionpitch = Pitches.query.filter_by(category = "promotionpitch")
    productpitch = Pitches.query.filter_by(category = "productpitch")
    

    return render_template('categories.html', title=title,pitch = pitch, pickuplines=pickuplines, interviewpitch= interviewpitch, promotionpitch = promotionpitch, productpitch = productpitch)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required

def new_pitch():
    form = PitchForm
    if form.validate_on_submit():
        pitch = form.pitch.data
        owner = current_user
        category = form.category.data

        new_pitch = Pitch(owner_id =current_user._get_current_object().id,pitch=pitch,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
  

    return render_template('pitch.html',form=form)

@main.route('/pitches/pitch_categories/')
def categories():
    product = Pitch.query.filter_by(category="product pitch").all()
    promotion = Pitch.query.filter_by(category="promotion pitch").all()
    pickupline = Pitch.query.filter_by(category="pickupline pitch").all()
    interview = Pitch.query.filter_by(category="interview pitch").all()
    return render_template('categories.html',pickup=pickupline,interview=interview,product=product,promotion=promotion)


@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()
        flash('your comment has been added', 'hurray')


        return redirect(url_for('.new_comment', pitch_id= pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comments.html', form = form,comment = all_comments )
