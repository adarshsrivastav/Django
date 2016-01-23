import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
x,y= (BASE_DIR + '/templates/',BASE_DIR + '/articles/' + '/templates/')
print "current path is %s" % BASE_DIR
print "current path is %s" % x
print "current path is %s" % y