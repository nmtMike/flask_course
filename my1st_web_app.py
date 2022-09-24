from flask import Flask

my_web_app = Flask(__name__)

@my_web_app.route('/')
def index():
    return '<h1>Hello there, this is my first web app using Flask !!!</h1>'

if __name__ == '__main__':
    my_web_app.run()