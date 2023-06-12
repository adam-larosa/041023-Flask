from flask import Flask

app = Flask( __name__ )

@app.route( '/potato' )
def potato():
    return "potato world!\n"


if __name__ == '__main__':
    app.run( port = 5555, debug = True )