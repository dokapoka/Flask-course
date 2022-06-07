from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def render_name():
    name = request.args['name']
    return render_template('hello.html', name=name)