from bottle import run, route, template, debug


@route('/')
def index():
    return '<h1>Welcome to PyMongo Text with Bottle Framework</h1>Author: <h3>Araja Jyothi Babu</h3>'


@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{ name }}</b>!', name=name)


@route('/bye/<name>')
def bye(name):
    return template('<h2>Bye Mr. {{ name }} !</h2>', name=name)

debug(True)
run(host='localhost', port=5656)