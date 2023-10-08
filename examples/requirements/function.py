'''
Author: Lunik
LICENCE: GPLv3

Description: This is an function example that returns a string rendered by cowsay
'''
import cowsay

def handler():
  '''
  This function returns a string rendered by cowsay
  '''
  output = cowsay.get_output_string('cow', 'Hello World')
  output = output.replace('\n', '<br>').replace(' ', '&nbsp;&nbsp;')

  return output
