from app import app
import os

if __name__ == (__name__):
   port = int(os.environ.get('PORT', 5000)) 
   app.run(host='0.0.0.0', port=port)