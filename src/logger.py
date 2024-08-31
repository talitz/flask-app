import logging
import sys


def setup_logger():
    """Sets up the logger with a specified format and level."""

    # Create a root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)  # Set the logging level

    # Create a stream handler for stdout
    stream_handler = logging.StreamHandler(sys.stdout)

    # Create and set a formatter for the stream handler
    log_formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    stream_handler.setFormatter(log_formatter)

    # Add the handler to the root logger
    root_logger.addHandler(stream_handler)


if __name__ == "__main__":
    setup_logger()
