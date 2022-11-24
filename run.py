from app import app
import os

if __name__ == (__name__):
   port = int(os.getenv('PORT'))
   app.run(host='0.0.0.0', port=port)
   
