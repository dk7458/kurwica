





#!/usr/bin/env python3

import os
import configparser
import logging

def load_config(config_path=None):
    """
    Load the configuration file.

    :param config_path: Path to the configuration file. If None, uses default path.
    :return: ConfigParser object with loaded configuration
    """
    if not config_path:
        # Use default path
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'conf', 'kurwica.conf')

    config = configparser.ConfigParser()
    logging.getLogger("kurwica.config").info(f"Loading configuration from {config_path}")

    if not os.path.exists(config_path):
        logging.getLogger("kurwica.config").warning(f"Configuration file not found at {config_path}")
        return config

    try:
        with open(config_path, 'r') as f:
            config.read_file(f)
        logging.getLogger("kurwica.config").info("Configuration loaded successfully")
        return config
    except Exception as e:
        logging.getLogger("kurwica.config").error(f"Failed to load configuration: {e}")
        return config

def save_config(config, config_path=None):
    """
    Save the configuration file.

    :param config: ConfigParser object with configuration to save
    :param config_path: Path to save the configuration file. If None, uses default path.
    """
    if not config_path:
        # Use default path
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'conf', 'kurwica.conf')

    try:
        with open(config_path, 'w') as f:
            config.write(f)
        logging.getLogger("kurwica.config").info(f"Configuration saved to {config_path}")
    except Exception as e:
        logging.getLogger("kurwica.config").error(f"Failed to save configuration: {e}")



