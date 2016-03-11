from eve import Eve
from flask import Flask, send_from_directory, render_template

app = Eve(__name__, static_url_path='', static_folder='static')


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static/bower_components/', path)


if __name__ == '__main__':
    app.run(debug=True)
