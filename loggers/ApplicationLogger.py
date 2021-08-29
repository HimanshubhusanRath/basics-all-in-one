import logging

class LOG:

    def getLogger(modulename):
        # Define the logger
        logger = logging.getLogger(modulename)
        # Set log level
        logger.setLevel(logging.INFO)
        # Set file name
        file_handler = logging.FileHandler('log/'+modulename+'.log')
        file_formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(file_formatter)
        # Add filehandler to the logger
        logger.addHandler(file_handler)

        return logger
