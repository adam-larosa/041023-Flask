from flask import Flask, request
from flask_migrate import Migrate

from models import db, Cat

import ipdb

app = Flask( __name__ )



app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///catsmeow.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False


migrate = Migrate( app, db )

db.init_app( app )





@app.route( '/cats', methods = [ 'GET', 'POST' ] )
def cats():
    if request.method == 'GET':
        catlist = Cat.query.all() # <- this list of objects ( i.e. instances ) 
                                  #    needs to become a list of dictionaries 
                                  #    before we can turn it into json.
        new_list = []
        for cat in catlist:
            cat_dict = {
                "id": cat.id,
                "name": cat.name,
                "bio": cat.bio,
            }
            new_list.append( cat_dict )

        return new_list

    elif request.method == 'POST':
        data = request.get_json()
        new_cat = Cat( name = data['name'], bio = data[ 'bio' ] )
        
        db.session.add( new_cat )
        db.session.commit()
        
        cat_dict = {
            "id": new_cat.id,
            "name": new_cat.name,
            "bio": new_cat.bio
        }
        return cat_dict


if __name__ == '__main__':
    app.run( port = 5555, debug = True )