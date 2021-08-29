####################   1. MODULE IMPORT    ####################

# Importing function from another python file from the same folder
from helperfunctions1 import helper1
# Importing function from another python file available under another folder

from helpers import helperfunction2
from helpers.helperfunction2 import helper2


# helper1()

# helperfunction2.helper2()
### OR
#helper2()

####################   2. LOGGER IMPLEMENTATION    ####################
from loggers.ApplicationLogger import LOG
logger = LOG.getLogger('mainmodule')
logger.info("Main Class is executing")

###################    3. DATABASE OPERATIONS      ####################
from database import SQLite
SQLite.test()