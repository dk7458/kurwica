




#!/usr/bin/env python3

import logging
from datetime import datetime, timedelta
from .zfs_pool import ZFSPool

class SnapshotManager:
    """Manages snapshot operations for ZFS pools."""

    def __init__(self, pool_config, snapshot_intervals):
        """
        Initialize the SnapshotManager with pool configuration and snapshot intervals.

        :param pool_config: Dictionary containing pool names
        :param snapshot_intervals: Dictionary containing snapshot types and their intervals in hours
        """
        self.pool_config = pool_config
        self.snapshot_intervals = snapshot_intervals
        self.pools = {}
        self.logger = logging.getLogger("kurwica.snapshot_manager")

        # Initialize pools
        for pool_name in pool_config.keys():
            self.pools[pool_name] = ZFSPool(pool_name)

    def create_snapshots(self):
        """Create snapshots on all pools based on the configured intervals."""
        current_time = datetime.now()

        for pool_name, pool in self.pools.items():
            for snapshot_type, interval_hours in self.snapshot_intervals.items():
                # Check if a snapshot of this type is needed
                last_snapshot = self.get_last_snapshot(pool, snapshot_type)

                if not last_snapshot or (current_time - last_snapshot).total_seconds() / 3600 >= interval_hours:
                    snapshot_name = f"{snapshot_type}_{current_time.strftime('%Y%m%d_%H%M%S')}"
                    self.logger.info(f"Creating {snapshot_type} snapshot '{snapshot_name}' on pool '{pool_name}'")
                    pool.create_snapshot(snapshot_name)
                else:
                    self.logger.debug(f"No {snapshot_type} snapshot needed for pool '{pool_name}'")

    def get_last_snapshot(self, pool, snapshot_type):
        """Get the last snapshot of a specific type."""
        snapshots = pool.list_snapshots()
        filtered_snapshots = [s for s in snapshots if s.startswith(f"{pool.name}@{snapshot_type}_")]

        if not filtered_snapshots:
            return None

        # Sort by timestamp in snapshot name
        filtered_snapshots.sort(reverse=True)
        last_snapshot_name = filtered_snapshots[0]
        timestamp_str = last_snapshot_name.split("_")[1]  # Extract timestamp from snapshot name

        try:
            timestamp = datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S")
            return timestamp
        except ValueError:
            self.logger.warning(f"Invalid timestamp format in snapshot: {last_snapshot_name}")
            return None

    def delete_old_snapshots(self):
        """Delete old snapshots based on retention policy."""
        # Implement retention policy here
        pass

    def list_all_snapshots(self):
        """List all snapshots for all pools."""
        for pool_name, pool in self.pools.items():
            snapshots = pool.list_snapshots()
            if snapshots:
                self.logger.info(f"Snapshots for pool '{pool_name}':")
                for snapshot in snapshots:
                    self.logger.info(f"  - {snapshot}")
            else:
                self.logger.info(f"No snapshots found for pool '{pool_name}'")



