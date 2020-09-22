from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email = db.Column(db.String(255),unique = True,nullable = False)
    password = db.Column(db.String(255),nullable = False)
    pitches_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    pass_secure = db.Column(db.String(255))

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
    time = db.Column(db.String(255))
    users = db.relationship('User',backref = 'pitches',lazy="dynamic")
    
    
    def __repr__(self):
        return f'User {self.name}'

