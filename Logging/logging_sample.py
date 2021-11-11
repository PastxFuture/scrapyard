# importing module
import logging
  
# Create and configure logger
logging.basicConfig(filename='test.log', 
                format='%(asctime)s : %(levelname)s : %(message)s', 
                datefmt='%Y-%m-%d %H:%M:%S')
  
# Creating an object
logger=logging.getLogger()
  
# Setting the threshold of logger to INFO
# Will ignore debug logging messages
logger.setLevel(logging.INFO)
  
# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")