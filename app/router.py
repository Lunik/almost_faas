'''
Author: Lunik
LICENCE: GPLv3

Description: This file define the core of the application
'''

import os

from flask import Flask

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

  loader.load(
    app=app,
    function_handler=FUNCTION_HANDLER,
    path=FUNCTION_PATH,
    methods=FUNCTION_METHODS,
  )

  return app
