from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cat( db.Model ):
    __tablename__ = 'cats'

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String )
    bio = db.Column( db.String )

    created_at = db.Column( db.DateTime, server_default = db.func.now() )
    updated_at = db.Column( db.DateTime, onupdate = db.func.now() )



    def __repr__( self ):
        return f'<Cat id: {self.id} name: {self.name}>'