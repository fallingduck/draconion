import bottle
from bottle import route, error, view, static_file, template, redirect, response, run
import json


bottle.TEMPLATE_PATH = ['./posts/', './static/content/', './static/templates/']


@route('/raw/<filepath:path>')
def serve_raw(filepath):
    return static_file(filepath, root='./static')

@route('/favicon.ico')
def favicon():
    return static_file('resources/favicon.ico', root='./static')

@route('/')
@view('archive')
def serve_index():
    with open('./index.json', 'r') as f:
        return json.load(f)

@route('/feed.xml')
@view('rss')
def feed():
    response.content_type = 'application/xml'
    with open('./index.json', 'r') as f:
        return json.load(f)

@route('/<page>')
@route('/<page>/')
def serve_page(page):
    if page == 'archive':
        redirect('/')
    return template(page)

@error(401)
@error(403)
@error(404)
@error(500)
def server_error(error):
    return template('error')


run(debug=True, quiet=True, host='localhost', port=3030)

