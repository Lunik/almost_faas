'''
Author: Lunik
LICENCE: GPLv3

Description: This is an function example that return a response from a library
'''

from lib.message import greeting

def handler():
  '''
  This function returns a response from a library
  '''
  return greeting("Space man")
