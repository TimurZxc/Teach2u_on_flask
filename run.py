from app import app
from gevent.pywsgi import WSGIServer

if __name__ == (__name__):
   # app.run(host="0.0.0.0", port=5000)
   http_server = WSGIServer(('', 5000), app)
   http_server.serve_forever()