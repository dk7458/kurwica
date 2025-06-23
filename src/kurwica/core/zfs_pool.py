


#!/usr/bin/env python3

import subprocess
import logging
from datetime import datetime, timedelta

class ZFSPool:
    """Represents a ZFS pool and provides methods to interact with it."""

    def __init__(self, name, scrub_interval=None):
        """
        Initialize a new ZFS pool.

        :param name: Name of the ZFS pool
        :param scrub_interval: Scrub interval in hours (optional)
        """
        self.name = name
        self.scrub_interval = scrub_interval
        self.logger = logging.getLogger(f"kurwica.pool.{name}")

        # Check if pool exists
        if not self.exists():
            raise ValueError(f"ZFS pool '{name}' does not exist")

    def exists(self):
        """Check if the ZFS pool exists."""
        try:
            output = subprocess.check_output(
                ["zpool", "list", "-H", "-o", "name"],
                universal_newlines=True
            )
            return self.name in output.split("\n") if output else False
        except subprocess.CalledProcessError:
            self.logger.error(f"Failed to check if pool '{self.name}' exists")
            return False

    def get_status(self):
        """Get the status of the ZFS pool."""
        try:
            output = subprocess.check_output(
                ["zpool", "status", "-v", self.name],
                universal_newlines=True
            )
            return output
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to get status for pool '{self.name}': {e}")
            return None

    def scrub(self):
        """Start a scrub on the ZFS pool."""
        try:
            self.logger.info(f"Starting scrub on pool '{self.name}'")
            subprocess.check_call(["zpool", "scrub", self.name])
            self.logger.info(f"Scrub started on pool '{self.name}'")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to start scrub on pool '{self.name}': {e}")

    def cancel_scrub(self):
        """Cancel an ongoing scrub on the ZFS pool."""
        try:
            self.logger.info(f"Cancelling scrub on pool '{self.name}'")
            subprocess.check_call(["zpool", "scrub", "-s", self.name])
            self.logger.info(f"Scrub cancelled on pool '{self.name}'")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to cancel scrub on pool '{self.name}': {e}")

    def get_scrub_status(self):
        """Get the status of an ongoing or recent scrub."""
        try:
            output = subprocess.check_output(
                ["zpool", "status", "-v", self.name],
                universal_newlines=True
            )
            return output
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to get scrub status for pool '{self.name}': {e}")
            return None

    def needs_scrub(self):
        """Check if the pool needs a scrub based on the interval."""
        if not self.scrub_interval:
            return False

        try:
            # Get last scrub time
            output = subprocess.check_output(
                ["zpool", "get", "-H", "-o", "value", f"{self.name}.scrub_time"],
                universal_newlines=True
            )
            last_scrub_str = output.strip()
            if not last_scrub_str or last_scrub_str == "-":
                self.logger.info(f"Pool '{self.name}' has never been scrubbed")
                return True

            # Parse the last scrub time
            last_scrub_time = datetime.strptime(last_scrub_str, "%Y-%m-%d.%H:%M:%S")
            now = datetime.now()

            # Calculate time since last scrub
            time_since_last_scrub = now - last_scrub_time

            # Check if enough time has passed for another scrub
            return time_since_last_scrub.total_seconds() / 3600 >= self.scrub_interval
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to check scrub status for pool '{self.name}': {e}")
            return False

    def create_snapshot(self, name):
        """Create a snapshot of the ZFS pool."""
        try:
            self.logger.info(f"Creating snapshot '{name}' on pool '{self.name}'")
            subprocess.check_call(["zfs", "snapshot", f"{self.name}@{name}"])
            self.logger.info(f"Snapshot '{name}' created on pool '{self.name}'")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to create snapshot '{name}' on pool '{self.name}': {e}")

    def delete_snapshot(self, name):
        """Delete a snapshot from the ZFS pool."""
        try:
            self.logger.info(f"Deleting snapshot '{name}' from pool '{self.name}'")
            subprocess.check_call(["zfs", "destroy", f"{self.name}@{name}"])
            self.logger.info(f"Snapshot '{name}' deleted from pool '{self.name}'")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to delete snapshot '{name}' from pool '{self.name}': {e}")

    def list_snapshots(self):
        """List all snapshots in the ZFS pool."""
        try:
            output = subprocess.check_output(
                ["zfs", "list", "-t", "snapshot", "-H", "-o", "name"],
                universal_newlines=True
            )
            return [s for s in output.split("\n") if s.startswith(f"{self.name}@")]
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to list snapshots for pool '{self.name}': {e}")
            return []

    def clean(self):
        """Perform cleaning operations on the ZFS pool."""
        # Implement cleaning logic here
        pass

