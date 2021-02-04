#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")
#sys.path.append("/var/www/FlaskApp/")

from FlaskApp import app as application
