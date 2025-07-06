from __future__ import annotations

from typing import Dict, List, Optional


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        loyalty: float = 0.5,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.loyalty = loyalty

        self.relationships: Dict[str, float] = {}
        self.decisions_history: List[str] = []
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.tension = max(0.0, min(1.0, self.tension))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

    def add_relationship(self, other: 'Agent', strength: float) -> None:
        """Store relationship strength with another agent."""
        self.relationships[other.name] = strength

    def calculate_relationship_tension(self) -> float:
        """Additional tension contributed by relationships."""
        if not self.relationships:
            return 0.0
        # Average negative relationships increase tension
        avg = sum(self.relationships.values()) / len(self.relationships)
        return max(0.0, 0.5 - avg)

    def update_tension_dynamically(self) -> None:
        """Slowly increase tension influenced by emotion and relationships."""
        self.tension += (self.emotion / 10) * 0.9
        self.tension += self.calculate_relationship_tension()
        self.tension = max(0.0, min(1.0, self.tension))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def make_moral_decision(self, situation: str) -> str:
        """Return a moral decision influenced by emotion and loyalty."""
        if self.emotion > 0.6:
            if self.loyalty > 0.7:
                decision = (
                    f"{self.name} chooses to help others despite fear due to loyalty."
                )
            else:
                decision = f"{self.name} decides to act selfishly, avoiding risk."
        elif self.state == "Enotnost" or self.loyalty > 0.7:
            decision = f"{self.name} helps others selflessly in {situation}."
        else:
            decision = f"{self.name} hesitates, torn between loyalty and personal interest."
        self.decisions_history.append(decision)
        return decision

    def team_decision(self, team: List['Agent']) -> str:
        """Make a simple team-based decision influenced by group emotions."""
        success_factor = 0.0
        for agent in team:
            success_factor += agent.loyalty + (
                1.0 if agent.emotion > 0.5 else 0.0
            )
        if success_factor > len(team):
            return f"{self.name}'s team successfully completes the task due to strong collaboration!"
        return f"{self.name}'s team fails the task due to lack of cohesion."

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        return f"{base} (čustvo: {self.emotion:.2f})"
