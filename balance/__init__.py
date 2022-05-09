from flask import Flask

app = Flask(__name__)
app.secret_key = 'superSafeSecretKey'

FLASK_APP=app
FLASK_ENV='development'

from balance import routes