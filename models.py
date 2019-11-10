from werkzeug import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), index=True, nullable=True)
    email = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash , password)

    def getJsonData(self):
        return {
            "name": self.name,
            "email": self.email
        }