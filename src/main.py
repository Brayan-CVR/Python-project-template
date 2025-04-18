#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main module of the Project.

This project serves as a template for building a more elaborate routine with specific functionalities.
By default this project includes the utils module, where functions are defined to relaunch the instance
of a logger and print the general aspects of the python version.
"""

# Custom imports
from python_information import print_details_about_python
from utils.logger_control import start_logger, get_logger

# Star logger
start_logger()
logger = get_logger(__name__)


def main_process() -> bool:
    """_summary_

    Returns:
        bool: _description_
    """
    try:
        # Main logic for this routine.
        logger.info("Running main process.\n")
        print_details_about_python(detailed=4)
        return True
    except Exception as e:
        logger.error(e)
        return False


if __name__ == "__main__":
    # Start the main execution process
    if main_process():
        logger.info("Successful execution.\n")
    else:
        logger.error("Failed execution.\n")
