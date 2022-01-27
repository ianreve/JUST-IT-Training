import logging  # import logging

# set the logging levels
logging.basicConfig(filename="LogFile1.log", level=logging.DEBUG)


logging.critical("Critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")
