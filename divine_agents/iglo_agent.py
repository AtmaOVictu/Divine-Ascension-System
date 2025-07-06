import threading
from typing import Callable, Dict, List, Any


class IgloAgent:
    """Coordinates execution of blocks sequentially or in parallel."""

    def __init__(self) -> None:
        self.results: Dict[str, Any] = {}

    def execute_in_sequence(self, blocks: List[Callable[[Dict[str, Any]], Any]]) -> None:
        """Execute blocks one after another, storing their results."""
        for block in blocks:
            self.results[block.__name__] = block(self.results)

    def _execute_block(self, block: Callable[[Dict[str, Any]], Any]) -> None:
        self.results[block.__name__] = block(self.results)

    def execute_in_parallel(self, blocks: List[Callable[[Dict[str, Any]], Any]]) -> None:
        """Execute blocks concurrently using threads."""
        threads: List[threading.Thread] = []
        for block in blocks:
            thread = threading.Thread(target=self._execute_block, args=(block,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

    def execute(self, sequence: List[Callable[[Dict[str, Any]], Any]], parallel: List[Callable[[Dict[str, Any]], Any]]) -> Dict[str, Any]:
        """Run sequential and parallel blocks and return their results."""
        self.execute_in_sequence(sequence)
        self.execute_in_parallel(parallel)
        return self.results
