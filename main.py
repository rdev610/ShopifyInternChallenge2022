#from flask import Flask

#app = Flask(__name__)

#@app.route("/")
#def index():
  #  return "Hello World!"
    
from website import create_app

#creates web application
app = create_app()

if __name__ == '__main__':
   app.run(debug=False)
    