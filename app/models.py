from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from datetime import datetime




class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch = db.relationship('Pitch', backref='user',lazy='dynamic')
    comments = db.relationship('Comment',backref = 'user',lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
            return check_password_hash(self.pass_secure, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Pitch(UserMixin,db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    text=db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_category = db.Column(db.String(255))
    posted_at = db.Column(db.DateTime,index=True,default=datetime.utcnow())
    comments = db.relationship('Comment',backref='post',lazy='dynamic')

    def save_pitch(self):
             db.session.add(self)
             db.session.commit()
               

    def get_pitches(self):
              pitches = Pitch.query.all()
              return pitches
              

    def get_pitches(self):
             pitch = Pitch.query.filter_by(id)
             return pitch

    def display_user(self):
            if Pitch.user_id == User.id:
                    return User.username

                        

               

        
                

            
                   



        



        
        


   

           
           

    
            
            

     


  

   




  





                        



    
   

  

   

   



















   




