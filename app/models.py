from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email = db.Column(db.String(255),unique = True,nullable = False)
    password = db.Column(db.String(255),nullable = False)
    pitches_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    pass_secure = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f'User {self.username}' 

class Pitches(db.Model):
    __tablename__= 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    downvotes = db.Column(db.Integer, default=int(0))
    upvotes = db.Column(db.Integer, default=int(0))
    users = db.relationship('User',backref = 'pitches',lazy="dynamic")
    

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitches.query.order_by(pitch_id=id).desc().all()
        return pitches
    
    def __repr__(self):
        return f'User {self.pitch}'


class Comment(db.Model):
	""" This model handles the Comment model that will be mapped to the database"""

	__tablename__='comments'

	id = db.Column(db.Integer,primary_key=True)
	pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'),nullable=False)
    description = db.Column(db.Text)

	def __repr__(self):
		return f"Comment : id: {self.id} comment: {self.description}"

class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    upvote = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()


    def add_upvotes(cls,id):
        upvote_pitch = Upvote(user = current_user, pitch_id=id)
        upvote_pitch.save_upvotes()

    
    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote

    @classmethod
    def get_all_upvotes(cls,pitch_id):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'



class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    downvote = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()


    def add_downvotes(cls,id):
        downvote_pitch = Downvote(user = current_user, pitch_id=id)
        downvote_pitch.save_downvotes()

    
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote

    @classmethod
    def get_all_downvotes(cls,pitch_id):
        downvote = Downvote.query.order_by('id').all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'