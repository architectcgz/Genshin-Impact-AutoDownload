from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('page_1.html')


if __name__ == '__main__':
    app.run(host='192.168.191.126', port=5000)
