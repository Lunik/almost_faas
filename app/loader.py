'''
Author: Lunik
LICENCE: GPLv3

Description: This class is responsible for loading the function handler
'''

import sys
import importlib

from flask import Blueprint

class FunctionLoader:
  '''
  This class is responsible for loading the function handler
  '''

  def __init__(self, function_folder):
    self.function_folder = function_folder
    sys.path.append(self.function_folder)

  def _import_handler(self, function_handler):
    '''
    Import the function handler
    '''
    module_name, function_name = function_handler.split(':')
    module = importlib.import_module(module_name)
    handler = getattr(module, function_name)
    return handler

  def load(self, app, function_handler, path, methods):
    '''
    Load the function handler in the app
    '''
    user_function = self._import_handler(function_handler)

    # if user_function is a Blueprint, register it
    if isinstance(user_function, Blueprint):
      app.register_blueprint(user_function)

    # if user_function is a function, register it
    elif callable(user_function):
      app.add_url_rule(path, "index", user_function, methods=methods)

    else:
      raise TypeError(
        f"Handler '{function_handler}' reference an unknown type: '{type(user_function)}'"
      )
