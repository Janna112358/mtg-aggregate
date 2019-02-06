from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
    home_url = url_for('home')
    return render_template('home.html', home_url=home_url)

@app.route('/hello')
@app.route('/hello/<name>')
def say_hello(name=None):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    home_url = url_for('home')
    return render_template('404.html', home_url=home_url), 404

with app.test_request_context():
    print(url_for('home'))
    print(url_for('say_hello'))
    print(url_for('static', filename='some_text.txt'))
