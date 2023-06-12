Having fun with Flask & Flask-SQLAlchemy!


Starting a new Python environment:
    pipenv --python 3.8

( ...three point eight could be replaced with whatever version of Python you 
  wanted the app to run with)

Initialize the database with SQLAlchemy:
    flask db init

Generate a new migration after adding a new class:
    flask db revision --autogenerate -m 'name of model or change'

Run a migration:
    flask db upgrade


Enter the flask shell ( remember to be in that "server" directory ):
    flask shell

Once in the shell we can create new instances & save them, e.g.:
    c1 = Cat( name = 'Luke' )
    db.session.add( c1 )
    db.session.commit()  <- this is what commits the save to the database