from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email = db.Column(db.String(255),unique = True,nullable = False)
    password = db.Column(db.String(255),nullable = False)
    pitches_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    pass_secure = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

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
    
    
    def __repr__(self):
        return f'User {self.pitch}'


class Comment(db.Model):
	""" This model handles the Comment model that will be mapped to the database"""

	__tablename__='comments'
	id = db.Column(db.Integer,primary_key=True)
	body = db.Column(db.Text)
	owner_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
	pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'),
        nullable=False)

	def __repr__(self):
		return f"Comment : id: {self.id} comment: {self.body}"

