from app import app

if __name__ == (__name__):
   # app.run(host="0.0.0.0")
   from waitress import serve
   serve(app, listen='*:8080')