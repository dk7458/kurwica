





#!/usr/bin/env python3

import os
import logging
import logging.config
import configparser

def setup_logging(config_path=None):
    """
    Setup logging configuration.

    :param config_path: Path to the logging configuration file. If None, uses default path.
    """
    if not config_path:
        # Use default path
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'conf', 'logging.conf')

    if not os.path.exists(config_path):
        logging.basicConfig(level=logging.INFO)
        print(f"Warning: Logging configuration file not found at {config_path}. Using basic logging setup.")
        return

    try:
        # Read the logging config
        config = configparser.ConfigParser()
        config.read(config_path)

        # Create log directory if it doesn't exist
        log_dir = os.path.dirname(os.path.join(os.path.dirname(__file__), '..', '..', 'logs'))
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        # Apply logging configuration
        logging.config.fileConfig(config_path)
        logging.getLogger("kurwica").info("Logging setup completed")
    except Exception as e:
        print(f"Error setting up logging: {e}")
        logging.basicConfig(level=logging.INFO)



