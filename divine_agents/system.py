from typing import List

from .module import AgentModule


class DynamicAgentSystem:
    """Manage multiple modules and coordinate dialogues between them."""

    def __init__(self) -> None:
        self.modules: List[AgentModule] = []

    def add_module(self, module: AgentModule) -> None:
        self.modules.append(module)

    def run(self, question: str) -> List[str]:
        """Run dialogues sequentially between modules."""
        lines: List[str] = []
        for i in range(len(self.modules) - 1):
            lines.extend(self.modules[i].dialogue_with(self.modules[i + 1], question))
        return lines
