"""Execution agent that stitches blocks in sequence or parallel."""
from __future__ import annotations

from typing import Callable, Dict, Any, List
import threading


class IgloAgent:
    """Agent that coordinates sequential and parallel block execution."""

    def __init__(self) -> None:
        self.results: Dict[str, Any] = {}

    def _execute_block(self, block: Callable[[Dict[str, Any]], Any]) -> None:
        result = block(self.results)
        self.results[block.__name__] = result

    def execute_in_sequence(self, blocks: List[Callable[[Dict[str, Any]], Any]]) -> None:
        """Execute blocks sequentially."""
        for block in blocks:
            self._execute_block(block)

    def execute_in_parallel(self, blocks: List[Callable[[Dict[str, Any]], Any]]) -> None:
        """Execute blocks concurrently."""
        threads: List[threading.Thread] = []
        for block in blocks:
            thread = threading.Thread(target=self._execute_block, args=(block,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

    def execute(self, sequence: List[Callable[[Dict[str, Any]], Any]], parallel: List[Callable[[Dict[str, Any]], Any]]) -> Dict[str, Any]:
        """Run sequence first, then parallel blocks."""
        self.execute_in_sequence(sequence)
        self.execute_in_parallel(parallel)
        return self.results
