"""Utilities for controlled, slow data storage."""

import time
from typing import Callable, Iterable, List, Any


class ControlledStorage:
    """Store data items slowly with optional confirmation."""

    def __init__(self) -> None:
        self.data: List[Any] = []

    def store_slowly(
        self,
        items: Iterable[Any],
        delay: float = 1.0,
        confirm: Callable[[Any], bool] | None = None,
    ) -> None:
        """Store each item with a delay and optional confirmation.

        Parameters
        ----------
        items: Iterable[Any]
            Items to store.
        delay: float, optional
            Delay in seconds between storing each item.
        confirm: Callable[[Any], bool] | None, optional
            Function returning True to confirm storing the item.
            If None, items are stored without confirmation.
        """
        for item in items:
            if confirm is None or confirm(item):
                self.data.append(item)
                time.sleep(delay)

