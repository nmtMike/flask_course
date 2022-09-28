from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home_page.html')

@app.route('/report')
def user_check():
    UserName = request.args.get('UserName')

    requirements = []
    if not UserName[-1].isnumeric():
        requirements += ['Must have a numeric at the end']
    if UserName.isupper():
        requirements += ['At least a lower case letter']
    if UserName.islower():
        requirements += ['At least an upper case letter']

    if len(requirements) == 0:
        return render_template('result_right.html', UserName=UserName)
    else:
        return render_template('result_wrong.html',UserName=UserName, requirements=requirements)

if __name__ == '__main__':
    app.run()