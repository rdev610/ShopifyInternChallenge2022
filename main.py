
#imports the create app method from __init__.py whihc is stored in the websire folder    
from website import create_app 

#creates web application
app = create_app()

if __name__ == '__main__':
   app.run(debug=False)
    