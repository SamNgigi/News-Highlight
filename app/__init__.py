from flask import Flask
from .config import DevConfig
# from flask_bootstrap import Bootstrap
"""
Initializing our app

'instance_relative_config=True' allows us to connect to
the instance folder when the app is created
"""

app = Flask(__name__, instance_relative_config=True)

# Setting up Configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extension
# bootstrap = Bootstrap(app)

from app import views
