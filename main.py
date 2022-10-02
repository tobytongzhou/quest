from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/marker/')
def marker():
    return render_template('marker_ar.html')


@app.route('/location/')
def location():
    return render_template('location.html')


if __name__ == '__main__':
    app.run(host="192.168.86.218", port=5001, debug=True)
