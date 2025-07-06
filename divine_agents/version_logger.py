import logging
from typing import Optional

class VersionLogger:
    """Simple logger to track version changes and errors."""

    def __init__(self, log_file: str = "program_logs.txt"):
        self.log_file = log_file
        self.logger = logging.getLogger(f"VersionLogger_{id(self)}")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_version_change(self, version_number: str, description: str) -> None:
        self.logger.info(f"Version {version_number} updated: {description}")

    def log_error(self, error_message: str) -> None:
        self.logger.error(f"Error: {error_message}")

    def log_debug(self, message: str) -> None:
        self.logger.debug(f"Debug: {message}")

    def view_logs(self) -> str:
        with open(self.log_file, "r") as file:
            return file.read()
