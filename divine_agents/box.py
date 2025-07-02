from __future__ import annotations

from typing import List


class Box:
    """Container storing philosophical tasks or data."""

    def __init__(self, box_name: str, contents: List[str] | None = None) -> None:
        self.box_name = box_name
        self.contents: List[str] = list(contents) if contents else []

    def add_content(self, content: str) -> None:
        """Add content to the box."""
        self.contents.append(content)

    def remove_content(self, content: str) -> None:
        """Remove content from the box if present."""
        if content in self.contents:
            self.contents.remove(content)

    def analyze_contents(self) -> List[str]:
        """Provide philosophical influence derived from contents."""
        beliefs: List[str] = []
        for content in self.contents:
            text = content.lower()
            if "absolutna resnica" in text:
                beliefs.append("Resnica je absolutna in neodvisna od drugih.")
            elif "relativna resnica" in text:
                beliefs.append("Resnica je relativna, oblikovana z našimi odnosi.")
            elif "enotna resnica" in text:
                beliefs.append("Vse resnice so eno, medsebojno povezane.")
        return beliefs

    def display_contents(self) -> List[str]:
        """Return current contents."""
        return list(self.contents)


from .agent import Agent


class AgentWithBox(Agent):
    """Agent containing a Box to influence transitions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, materials=None) -> None:
        super().__init__(name, state, tension, emotion, materials)
        self.box = Box("Filozofska Škatla")

    def add_task_to_box(self, task: str) -> None:
        self.box.add_content(task)

    def review_box_contents(self) -> List[str]:
        return self.box.display_contents()

    def transition_with_box(self) -> str:
        beliefs = self.box.analyze_contents()
        for belief in beliefs:
            if belief not in self.philosophical_beliefs:
                self.philosophical_beliefs.append(belief)
        return self.transition()

