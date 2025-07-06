from __future__ import annotations
from typing import Dict, List

from .agent import Agent


class SymbolicSubAgent:
    """Subagent responsible for processing a single symbol."""

    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    def process(self) -> str:
        """Return a message indicating the symbol is processed."""
        return f"Podagent za simbol '{self.symbol}' obdeluje operacijo."


class SymbolicAgent(Agent):
    """Agent composed of subagents for each provided symbol."""

    def __init__(self, name: str, symbols: List[str], state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.sub_agents: Dict[str, SymbolicSubAgent] = {
            s: SymbolicSubAgent(s) for s in symbols
        }

    def operate(self) -> List[str]:
        """Invoke processing on all subagents."""
        results = []
        for sub in self.sub_agents.values():
            results.append(sub.process())
        return results
