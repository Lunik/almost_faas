'''
Author: Lunik
LICENCE: GPLv3

Description: This is an function example that returns a Flask Blueprint
'''

from flask import Blueprint

bp = Blueprint('function', __name__)

@bp.route('/')
def index():
  '''
  Hello World function
  '''
  return 'Hello World!'

@bp.route('/<name>')
def hello(name):
  '''
  Hello function with a name
  '''
  return f"Hello {name}!"
