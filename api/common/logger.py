import logging

# Logging
formatter = logging.Formatter("[%(asctime)-15s] %(levelname)-7s %(filename)s:%(funcName)s:%(lineno)d %(message)s")
log = logging.getLogger()
log.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)