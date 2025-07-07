"""Core agent implementation for ontological transitions."""

from __future__ import annotations

import time
from typing import Dict


class Agent:
    """Represents an ontological agent with emotional awareness."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: Mapping of emotion labels to their intensity impact on tension
    EMOTIONS: Dict[str, float] = {
        "fear": 0.6,
        "joy": 0.8,
        "anger": 0.7,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", emotion: str = "neutral", tension: float = 0.0):
        self.name = name
        self.state = state
        self.emotion = emotion
        self.tension = tension
        self.history = [state]
        self.timestamp = time.time()

    def update_emotion(self, emotion: str) -> None:
        """Update the agent's emotion and adjust tension.

        Parameters
        ----------
        emotion:
            Name of the emotion to apply. Intensity is looked up in
            :pyattr:`EMOTIONS`.
        """

        self.emotion = emotion
        self.tension += self.EMOTIONS.get(emotion, 0.0)
        self.log(f"Emotion updated to {self.emotion}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.log(f"Tension level set to {self.tension}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""

        emotion_value = self.EMOTIONS.get(self.emotion, 0.0)
        if self.tension > 0.7 or emotion_value > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            else:
                self.state = "Ego"
            self.log(f"Transitioned to {self.state}")
        self.history.append(self.state)
        self.timestamp = time.time()
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            response = "Vse resnice so eno, medsebojno povezane."
        self.log(f"Responded: {response}")
        return response

    def log(self, message: str) -> None:
        """Log a message with a timestamp for debugging purposes."""
        timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(self.timestamp))
        print(f"{timestamp_str} - {self.name}: {message}")
