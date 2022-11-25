from app import app
import os

if __name__ == (__name__):
<<<<<<< HEAD
   port = int(os.environ.get('PORT', 5000)) 
   app.run(host='0.0.0.0', port=port)
=======
   port = int(os.getenv('PORT'))
   app.run(host='0.0.0.0', port=port)
   
>>>>>>> 04414a463124c9291eea3acc8c85653cc9cfb2a8
