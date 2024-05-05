from flask import Flask, render_template

hello_flask = Flask(__name__, static_folder = 'static')
@hello_flask.route('/')
def home():
    return render_template('home.html')
if __name__ == '__main__':
    hello_flask.run(debug=True)