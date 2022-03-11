from .import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

'''
this decorator modifies the load_user funtion by passing user id that queries and 
gets a user with that Id
'''
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))



class Quotes:
    def __init__(self,author,id,quote):
        self.id=id
        self.author=author
        self.quote=quote

class User(db.Model,UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError("You can't read the password attribute")

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        self.pass_secure = generate_password_hash(password)


    def __repr__(self):
        return f'User{self.username}'