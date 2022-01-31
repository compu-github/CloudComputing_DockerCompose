from bottle import route, run, template
import redis

host='redis-server'
r = redis.Redis(host=host, port=6379, db=0)
r.set('visits', 0)

@route('/')
def index():
    visits = int(r.get('visits'))
    visits = visits + 1
    r.set('visits', visits)
    return template('<b>Hello, number of visits is {{visits}}</b>!', visits=visits)
    
run(host='0.0.0.0', port=8081)
    
