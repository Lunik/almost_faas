'''
Author: Lunik
LICENCE: GPLv3

Description: This class is responsible for loading the function handler
'''

import sys
import importlib

class FunctionLoader:
  '''
  This class is responsible for loading the function handler
  '''

  def __init__(self, function_folder):
    self.function_folder = function_folder
    sys.path.append(self.function_folder)

  def load(self, function_handler):
    '''
    Load and return the function handler
    '''
    module_name, function_name = function_handler.split(':')
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)
    return function
