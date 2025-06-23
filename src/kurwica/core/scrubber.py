



#!/usr/bin/env python3

import logging
from .zfs_pool import ZFSPool

class Scrubber:
    """Manages scrubbing operations for ZFS pools."""

    def __init__(self, pool_config):
        """
        Initialize the Scrubber with a pool configuration.

        :param pool_config: Dictionary containing pool names and their scrub intervals
        """
        self.pool_config = pool_config
        self.pools = {}
        self.logger = logging.getLogger("kurwica.scrubber")

        # Initialize pools
        for pool_name, interval in pool_config.items():
            self.pools[pool_name] = ZFSPool(pool_name, interval)

    def run_scrubs(self):
        """Run scrubs on all pools that need scrubbing."""
        for pool_name, pool in self.pools.items():
            if pool.needs_scrub():
                self.logger.info(f"Pool '{pool_name}' needs scrubbing")
                pool.scrub()
            else:
                self.logger.debug(f"Pool '{pool_name}' does not need scrubbing")

    def check_status(self):
        """Check the status of all pools."""
        for pool_name, pool in self.pools.items():
            status = pool.get_scrub_status()
            if status:
                self.logger.info(f"Status for pool '{pool_name}':\n{status}")
            else:
                self.logger.warning(f"No status available for pool '{pool_name}'")

    def cancel_all_scrubs(self):
        """Cancel all ongoing scrubs."""
        for pool_name, pool in self.pools.items():
            pool.cancel_scrub()
            self.logger.info(f"Cancelled scrub on pool '{pool_name}'")


