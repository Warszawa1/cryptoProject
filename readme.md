# CryptoConverter

 A simple Flask Web App to convert EUR to crypto, crypto to crypto or crypto to EUR.
<hr>

- These instructions should get you a copy of the project up and running on you local machine for development or testing.

* PREREQUISITES
  - Python3
  - SQLite3
  - virtualenv
<hr>
  
* INSTALLING
  - Set up a separate Virtual Environment for the repository.
    - virtualenv env
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
    -     OR
    - python -m flask run
<hr> 
    
* DEPLOYMENT
  - Deployment needs to be done on a WSGI Server
    --- https://wsgi.readthedocs.io/en/latest/servers.html
    
    
![Screenshot 2022-05-10 at 22 39 03](https://user-images.githubusercontent.com/48474962/167936083-845bcbb0-d6b7-4e22-8972-cbf6d58d01ed.png)
![Screenshot 2022-05-05 at 12 38 49](https://user-images.githubusercontent.com/48474962/167936163-1fafcb3a-029e-4fa5-9971-3871f8b963ee.png)
![Screenshot 2022-05-11 at 21 54 38](https://user-images.githubusercontent.com/48474962/167936188-22b9658f-894d-4628-a5dd-46c39199a015.png)


