
# Kurwica Documentation

## Overview

Kurwica is a command-line tool for automating ZFS pool maintenance on Debian systems. It provides features like automated scrubbing, snapshot management, logging, pool cleaning, and monitoring.

## Project Structure

The project follows a modular structure with the following key components:

```
kurwica/
├── conf/                  # Configuration files
│   ├── kurwica.conf       # Main configuration file
│   └── logging.conf       # Logging configuration file
├── src/                   # Source code
│   ├── kurwica/           # Main package
│   │   ├── __init__.py    # Package initializer
│   │   ├── cli/           # Command-line interface modules
│   │   │   └── main.py    # Main CLI entry point
│   │   ├── core/          # Core functionality modules
│   │   │   ├── cleaner.py  # Pool cleaning functionality (stub)
│   │   │   ├── monitor.py  # Monitoring functionality (stub)
│   │   │   ├── scrubber.py # Scrubbing functionality
│   │   │   ├── snapshot_manager.py # Snapshot management functionality
│   │   │   └── zfs_pool.py # ZFS pool interaction module
│   │   └── utils/         # Utility modules
│   │       ├── __init__.py
│   │       ├── config.py  # Configuration handling utilities
│   │       ├── logging_setup.py # Logging setup utilities
│   │       └── zfs_utils.py # ZFS-specific utilities (stub)
├── .gitignore             # Git ignore file
├── Makefile               # Makefile for build automation
├── README.md              # Project overview
├── requirements.txt       # Python dependencies
└── setup.py               # Package installation script
```

## Core Components

### 1. CLI Interface (cli/main.py)

The main entry point for the command-line tool. Currently, it's a basic implementation with argparse that will be extended to include all subcommands.

### 2. ZFS Pool Management (core/zfs_pool.py)

This module provides a class (`ZFSPool`) for interacting with ZFS pools. It includes methods for:

- Checking if a pool exists
- Getting pool status
- Starting and canceling scrubs
- Creating, deleting, and listing snapshots

### 3. Scrubber (core/scrubber.py)

Manages scrubbing operations for ZFS pools. It can:

- Run scrubs on all pools that need scrubbing
- Check the status of all pools
- Cancel all ongoing scrubs

### 4. Snapshot Manager (core/snapshot_manager.py)

Handles snapshot operations for ZFS pools, including:

- Creating snapshots based on configured intervals
- Listing all snapshots
- Deleting old snapshots (retention policy to be implemented)

### 5. Configuration Handling (utils/config.py)

Provides functions for loading and saving configuration files using the `configparser` module.

### 6. Logging Setup (utils/logging_setup.py)

Sets up logging configuration based on a config file, ensuring proper log directory creation.

## Configuration Files

### kurwica.conf

The main configuration file contains settings for:

- General settings like log and temp directories
- Pool definitions with scrub intervals
- Snapshot intervals
- Logging configuration

### logging.conf

Configures Python's logging module to output logs to both console and a file.

## Dependencies (requirements.txt)

The project depends on several Python libraries:

- argparse: For CLI interface
- configparser: For configuration handling
- subprocess32: For better subprocess handling
- psutil: For system utilities
- pytz: For timezone handling

## Future Development

### 1. Implement Missing Features

- Complete the implementation of pool cleaning (core/cleaner.py)
- Implement monitoring functionality (core/monitor.py)
- Add ZFS-specific utility functions (utils/zfs_utils.py)

### 2. Extend CLI Interface

Add subcommands for each feature:
- `pool`: Manage pools
- `scrub`: Manage scrubbing operations
- `snapshot`: Manage snapshots
- `log`: View logs
- `clean`: Perform cleaning operations
- `monitor`: Monitor pool health

### 3. Add API Layer

Develop an API layer that can be used by a future UI component.

## Installation and Usage

[Installation instructions will go here]

[Usage examples will go here]
