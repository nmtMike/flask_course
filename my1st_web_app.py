from flask import Flask

my_web_app = Flask(__name__)

@my_web_app.route('/')
def index():
    return '<h1>Hello there, this is my first web app using Flask !!!</h1>'

@my_web_app.route('/information')
def infomation():
    return '''<h1>This web app is based on:</h1>
    Python: 3.9.12 and Flask: 1.1.2
    '''

@my_web_app.route('/user/<name>')
def user(name):
    return """
    This page is for {}
    """.format(name.upper())

if __name__ == '__main__':
    my_web_app.run()