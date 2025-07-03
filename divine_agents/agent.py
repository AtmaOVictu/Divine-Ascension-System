"""Core agent implementation used in philosophical simulations."""

from __future__ import annotations

import random
from typing import List

from .ontoznano import Ontoznano


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        self.ontoznano = Ontoznano()
        self.tasks: List[str] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    # --- Additional behaviour ---
    def sprejmi_nalogo(self, naloga: str) -> None:
        """Accept a task and record ontological transition."""
        self.tasks.append(naloga)
        print(f"{self.name} sprejme nalogo: {naloga}")
        self.ontoznano.prehod_v_ontoznano(naloga)

    def interact(self, other: "Agent") -> None:
        """Basic interaction between two agents affecting emotions."""
        feedback = random.choice([
            "pozitivno",
            "negativno",
            "nevtralno",
            "strah",
            "jeza",
            "presenečenje",
        ])
        print(f"{self.name} komunicira z {other.name}. Povratna informacija: {feedback}")
        # treat negative feedback as raising tension
        delta = 0.6 if feedback in {"strah", "jeza", "negativno"} else 0.3
        self.update_emotion(delta)
        self.transition()

    def izvedi_naloge(self) -> None:
        """Execute all tasks assigned to the agent."""
        for naloga in self.tasks:
            print(f"Agent {self.name} izvaja nalogo: {naloga}")
            self.ontoznano.prehod_v_ontoznano(naloga)

    def prikazi_krake(self) -> None:
        """Display recorded task history."""
        print(f"Naloge za agenta {self.name}: {self.tasks}")
