import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from . import logger


class _LogHandler(FileSystemEventHandler):
    """Internal handler that logs file modifications."""

    def on_modified(self, event):
        if not event.is_directory:
            logger.info("Modified: %s", event.src_path)


class Watcher:
    """Watch a path for file modifications and log them."""

    def __init__(self, path: str, recursive: bool = True):
        self.path = Path(path)
        self.recursive = recursive
        self.observer = Observer()

    def start(self) -> None:
        handler = _LogHandler()
        self.observer.schedule(handler, str(self.path), recursive=self.recursive)
        self.observer.start()

    def stop(self) -> None:
        self.observer.stop()
        self.observer.join()
