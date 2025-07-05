"""Core agent logic for the divine ascension system.

Agents transition between ontological states (Ego, Jaz, Enotnost) depending on
their emotional intensity and accumulated tension.  The transition rules follow
the specifications from ``AGENTS`` instructions:

* When ``tension`` is greater than ``0.7`` **or** ``emotion`` is greater than
  ``0.5`` the agent advances one state forward.
* ``Ego`` → ``Jaz`` → ``Enotnost``.

The module also exposes simple persistence helpers so that an agent's state can
be saved and later restored.
"""

import json
import math


def logistic_function(x: float, k: float = 1.0, c: float = 0.5) -> float:
    """Smooth step used when evolving emotional tension."""
    return 1 / (1 + math.exp(-k * (x - c)))


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # tension gradually increases using a logistic curve to keep it bounded
        self.tension = logistic_function(self.tension + value)

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
        """Return a philosophical answer depending on the current state.

        The intensity of emotion colours the statement to reflect the agent's
        current feelings.
        """
        emotion_prefix = "mirno"
        if self.emotion > 0.7:
            emotion_prefix = "strastno"
        elif self.emotion > 0.3:
            emotion_prefix = "zmerno"

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix}: {base}"

    def save_state(self, path: str) -> None:
        """Persist the current agent state to ``path``."""
        data = {
            "name": self.name,
            "state": self.state,
            "tension": self.tension,
            "emotion": self.emotion,
            "history": self.history,
        }
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh)

    def load_state(self, path: str) -> None:
        """Load agent state from ``path``."""
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        self.name = data.get("name", self.name)
        self.state = data.get("state", self.state)
        self.tension = data.get("tension", self.tension)
        self.emotion = data.get("emotion", self.emotion)
        self.history = data.get("history", self.history)
