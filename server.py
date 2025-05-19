from bottle import get, run, static_file

@get('/<loc>')
def chant(loc):
	return static_file(loc, root='db/')

run(host='localhost', port=40081)
