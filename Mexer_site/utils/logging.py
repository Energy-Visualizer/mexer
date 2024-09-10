####################################################################
# logging.py includes all functions related to logging
# 
# It is 2 lines. It gives developers a logger to use called LOGGER.
#
# The logging format is defined in Mexer_meta/settings.py
#
# Use: LOGGER.info("message"), LOGGER.warn("message"), etc.
# It is built on python's native logging system, so it can use those functions
#
# Authors:
#       Kenny Howes - kmh67@calvin.edu
#       Edom Maru - eam43@calvin.edu 
#####################
import logging

LOGGER = logging.getLogger("Mexer_default")