'''
Author: Lunik
LICENCE: GPLv3

Description: This file define the core of the application
'''

import os

from flask import Flask, Blueprint

from loader import FunctionLoader

FUNCTION_FOLDER = os.environ.get('FUNCTION_FOLDER', '/functions')
FUNCTION_HANDLER = os.environ.get('FUNCTION_HANDLER', 'function:handler')
FUNCTION_PATH = os.environ.get('FUNCTION_PATH', '/')
FUNCTION_METHODS = os.environ.get('FUNCTION_METHODS', 'GET,POST').split(',')

def create_app():
  '''
  Create and return the Flask application
  '''
  app = Flask(__name__)

  @app.route('/healthz')
  def health():
    return 'OK'

  loader = FunctionLoader(function_folder=FUNCTION_FOLDER)

  user_function = loader.load(function_handler=FUNCTION_HANDLER)

  # if user_function is a Blueprint, register it
  if isinstance(user_function, Blueprint):
    app.register_blueprint(user_function)

  # if user_function is a function, register it
  elif callable(user_function):
    app.add_url_rule(FUNCTION_PATH, "index", user_function, methods=FUNCTION_METHODS)

  else:
    raise TypeError(f"Handler '{FUNCTION_HANDLER}' reference an unknown type: '{type(user_function)}'")

  return app
