from flask import Flask, request
from flask_migrate import Migrate

from models import db, Cat

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///catsmeow.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False
migrate = Migrate( app, db )

db.init_app( app )





@app.route( '/potatos', methods = [ 'GET', 'POST' ] )
def potato():
    if request.method == 'GET':
        return "we get potato world!\n"

    elif request.method == 'POST':
        return "make a new potato!"


if __name__ == '__main__':
    app.run( port = 5555, debug = True )