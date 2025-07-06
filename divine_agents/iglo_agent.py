import threading
from typing import Callable, List, Any, Dict


class IgloAgent:
    """Coordinates execution of functional blocks in sequence or parallel."""

    def __init__(self) -> None:
        self.results: Dict[str, Any] = {}

    def execute_in_sequence(self, blocks: List[Callable[[Dict[str, Any]], Any]]) -> None:
        """Execute blocks sequentially, passing results dict to each."""
        for block in blocks:
            result = block(self.results)
            self.results[block.__name__] = result

    def execute_in_parallel(self, blocks: List[Callable[[Dict[str, Any]], Any]]) -> None:
        """Execute independent blocks concurrently."""
        threads = []
        for block in blocks:
            thread = threading.Thread(target=self._run_block, args=(block,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    def _run_block(self, block: Callable[[Dict[str, Any]], Any]) -> None:
        result = block(self.results)
        self.results[block.__name__] = result

    def execute(self,
                sequence: List[Callable[[Dict[str, Any]], Any]],
                parallel: List[Callable[[Dict[str, Any]], Any]]) -> Dict[str, Any]:
        """Run sequence blocks then parallel blocks."""
        self.execute_in_sequence(sequence)
        self.execute_in_parallel(parallel)
        return self.results
