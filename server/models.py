from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cat( db.Model ):
    __tablename__ = 'cats'

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String )
    bio = db.Column( db.String )

    def __repr__( self ):
        return f'<Cat id: {self.id} name: {self.name}>'