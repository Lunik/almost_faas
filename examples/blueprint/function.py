'''
Author: Lunik
LICENCE: GPLv3

Description: This is an function example that returns a Flask Blueprint
'''

from flask import Blueprint

bp = Blueprint('function', __name__)

@bp.route('/')
def index():
  return 'Hello World!'

@bp.route('/<name>')
def hello(name):
  return 'Hello %s!' % name