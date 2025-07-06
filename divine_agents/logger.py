import logging
from pathlib import Path


class VersionLogger:
    """Simple logger to track program versions and events."""

    def __init__(self, log_file: str = "program_logs.txt") -> None:
        self.log_file = Path(log_file)
        logging.basicConfig(
            filename=self.log_file,
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            force=True,
        )

    def log_version_change(self, version_number: float, description: str) -> None:
        """Log a change in version."""
        logging.info(f"Version {version_number} updated: {description}")

    def log_error(self, error_message: str) -> None:
        """Log an error message."""
        logging.error(f"Error: {error_message}")

    def log_debug(self, message: str) -> None:
        """Log debug information."""
        logging.debug(f"Debug: {message}")

    def view_logs(self) -> str:
        """Return contents of the log file."""
        if self.log_file.exists():
            return self.log_file.read_text()
        return ""


class VersionComparer:
    """Compare two version numbers and log the result."""

    def __init__(self, logger: VersionLogger) -> None:
        self.logger = logger

    def compare_versions(self, new_version: float, old_version: float) -> str:
        """Compare new and old versions and log the outcome."""
        if new_version > old_version:
            self.logger.log_version_change(new_version, "Upgraded version detected.")
            return "New version is an upgrade."
        self.logger.log_version_change(new_version, "Downgrade detected.")
        return "New version is a downgrade."
