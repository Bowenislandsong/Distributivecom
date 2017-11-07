# Medusa File grab
# Created By Bowen Song Oct 13, 2017
# Library dedicated to Medusa project
# Use under the guidiance of GNU 3.0

import sys
import logging
from thread import *

# function for grabing and downloading all the files 
def grabfromserver(servername, password, ):
	dir_path = os.path.dirname(os.path.realpath(__file__))