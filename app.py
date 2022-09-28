from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/ar/')
def hello():
    return render_template('marker_ar.html')


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port=9000, debug=True, ssl_context='adhoc')
    # 192.168.86.218