from flask import render_template
from app import app

#  Views


@app.route('/')
def index():
    """
    Function that returns the index page and its data
    """
    test_args = 'Working!'
    return render_template('index.html', test_param=test_args)
