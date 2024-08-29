import logging
import os

from src.app import logger


def get_relative_db_path(db_path):
    # Get the directory of the current script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the relative path to the database file
    db_path = os.path.join(base_dir, db_path)
    logging.getLogger().info("DATABASE path is {}".format(db_path))
    return db_path
