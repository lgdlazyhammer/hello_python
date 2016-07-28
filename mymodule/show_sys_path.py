#!my test module

import sys

foo = 'this is the search path of current environment: '
def showpath():
	return foo , sys.path
	
	