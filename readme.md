# CryptoConverter

 A simple Flask Web App to convert EUR to crypto, crypto to crypto or crypto to EUR.
<hr>

- These instructions should get you a copy of the project up and running on you local machine for development or testing.

* PREREQUISITES
  - Python3
  - virtualenv
<hr>
  
* INSTALLING
  - Activate the Virtual Environment
    - env/bin/activate (for Linux)
    - env/Scripts/activate (for Windows)
  
  - Navigate to the project folder and run:
    - pip install -r requirements.txt
  
  - Make sure the Environment Variable FLASK_APP is set to app.py:
    - export FLASK_APP=app (for Linux)
    - set FLASK_APP=app (for Windows)
  
  - Run the application using:
    - flask run 
<hr> 
    
* DEPLOYMENT
  - Deployment needs to be done on a WSGI Server
    --- https://wsgi.readthedocs.io/en/latest/servers.html