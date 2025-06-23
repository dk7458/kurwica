






#!/usr/bin/env python3

import subprocess
import logging

def execute_zfs_command(command, pool=None):
    """
    Execute a ZFS command.

    :param command: List of command arguments (e.g., ['list', '-H'])
    :param pool: Optional pool name to include in the command
    :return: Command output or None if command failed
    """
    logger = logging.getLogger("kurwica.zfs_utils")

    try:
        cmd = ["zfs"] + command
        if pool:
            cmd.append(pool)

        output = subprocess.check_output(cmd, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to execute ZFS command: {' '.join(cmd)}. Error: {e}")
        return None

def execute_zpool_command(command, pool=None):
    """
    Execute a Zpool command.

    :param command: List of command arguments (e.g., ['list', '-H'])
    :param pool: Optional pool name to include in the command
    :return: Command output or None if command failed
    """
    logger = logging.getLogger("kurwica.zfs_utils")

    try:
        cmd = ["zpool"] + command
        if pool:
            cmd.append(pool)

        output = subprocess.check_output(cmd, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to execute Zpool command: {' '.join(cmd)}. Error: {e}")
        return None



