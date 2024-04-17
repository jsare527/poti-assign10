from flask import Flask, render_template
import time

app = Flask(__name__)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.route('/')
def home():
    arr = []
    with open('entries.txt', 'r') as f:
        for line in f.readlines():
            timestamp, title, entry = line.strip().split('|')
            timestamp = time.ctime((int(timestamp)))
            arr.append([timestamp, title, entry])
    return render_template('home.html', data=arr)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/links')
def links():
    return render_template('links.html')

if __name__ == '__main__':
    app.run()