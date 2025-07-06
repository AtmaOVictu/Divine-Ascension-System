import logging
from typing import List


class VersionLogger:
    """Simple logger to track version changes and errors."""

    def __init__(self, log_file: str = "program_logs.txt") -> None:
        self.log_file = log_file
        self.logger = logging.getLogger(log_file)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(self.log_file)
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        # Avoid adding multiple handlers if logger already configured
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def log_version_change(self, version_number: float, description: str) -> None:
        """Log version updates with a short description."""
        self.logger.info("Version %s updated: %s", version_number, description)
        for handler in self.logger.handlers:
            handler.flush()

    def log_error(self, error_message: str) -> None:
        """Log errors encountered in the system."""
        self.logger.error("Error: %s", error_message)
        for handler in self.logger.handlers:
            handler.flush()

    def log_debug(self, message: str) -> None:
        """Log debugging information."""
        self.logger.debug("Debug: %s", message)
        for handler in self.logger.handlers:
            handler.flush()

    def view_logs(self) -> str:
        """Return the entire log file contents."""
        with open(self.log_file, "r", encoding="utf-8") as file:
            return file.read()


class VersionComparer:
    """Utility class to compare software versions."""

    def __init__(self, logger: VersionLogger) -> None:
        self.logger = logger

    def compare_versions(self, new_version: float, old_version: float) -> str:
        """Compare two versions and log the result."""
        if new_version > old_version:
            self.logger.log_version_change(new_version, "Upgraded version detected.")
            return "New version is an upgrade."
        else:
            self.logger.log_version_change(new_version, "Downgrade detected.")
            return "New version is a downgrade."
