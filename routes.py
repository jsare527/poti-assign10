from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template()

@app.route('/links')
def links():
    return render_template()

if __name__ == '__main__':
    app.run()