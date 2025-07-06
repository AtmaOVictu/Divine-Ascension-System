import threading
from typing import Callable, Dict, List, Any


class IgloAgent:
    """Agent that stitches blocks together sequentially or in parallel."""

    def __init__(self) -> None:
        self.results: Dict[str, Any] = {}

    def _execute_block(self, block: Callable[[Dict[str, Any]], Any]) -> None:
        """Execute a single block and store its result."""
        result = block(self.results)
        self.results[block.__name__] = result

    def execute_in_sequence(self, blocks: List[Callable[[Dict[str, Any]], Any]]) -> None:
        """Execute blocks one after another."""
        for block in blocks:
            self._execute_block(block)

    def execute_in_parallel(self, blocks: List[Callable[[Dict[str, Any]], Any]]) -> None:
        """Execute blocks concurrently using threads."""
        threads = []
        for block in blocks:
            thread = threading.Thread(target=self._execute_block, args=(block,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    def execute(self, sequence: List[Callable[[Dict[str, Any]], Any]], parallel: List[Callable[[Dict[str, Any]], Any]]) -> Dict[str, Any]:
        """Run sequence blocks then parallel blocks and return results."""
        self.execute_in_sequence(sequence)
        self.execute_in_parallel(parallel)
        return self.results
