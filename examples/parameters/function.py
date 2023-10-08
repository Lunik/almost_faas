'''
Author: Lunik
LICENCE: GPLv3

Description: This is an function example that returns the request parameters
'''

from flask import request

def handler():
  '''
  This function returns the request parameters
  '''
  return request.args
