from flask import render_template, redirect, url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitches, Comment, Upvote, Downvote
from .forms import PitchForm, CommentForm
from .. import db

@main.route('/')
def index():
    title="Welcome to PITCHER"
    pitch = Pitches.query.filter_by().first()
    pickuplines = Pitches.query.filter_by(category="pickuplines")
    interviewpitch = Pitches.query.filter_by(category = "interviewpitch")
    promotionpitch = Pitches.query.filter_by(category = "promotionpitch")
    productpitch = Pitches.query.filter_by(category = "productpitch")
    upvotes = Upvote.get_all_upvotes(pitch_id=Pitches.id)

    return render_template('categories.html', title=title,pitch = pitch,upvotes=upvotes, pickuplines=pickuplines, interviewpitch= interviewpitch, promotionpitch = promotionpitch, productpitch = productpitch)



@main.route('/profile/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required

def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = form.pitch.data
        owner_id = current_user
        title = form.title.data
        category = form.category.data
        new_pitch = Pitches(owner_id =current_user._get_current_object().id,pitch=pitch,category=category,title=title)
        new_pitch.save_pitch()

        return redirect(url_for('main.index'))
    return render_template('pitch.html',form=form)



@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitches.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()
       


        return redirect(url_for('.new_comment', pitch_id= pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comments.html', form = form,comment = all_comments )

@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
@login_required
def upvote(pitch_id):
    pitch = Pitches.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Upvote.query.filter_by(pitch_id= pitch_id)
    
    if Upvote.query.filter(Upvote.user_id==user.id,Upvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_upvote = Upvote(pitch_id=pitch_id, user = current_user)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))



@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(pitch_id):
    pitch = Pitches.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id= pitch_id)
    
    if Downvote.query.filter(Downvote.user_id==user.id,Downvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_downvote = Downvote(pitch_id=pitch_id, user = current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index'))