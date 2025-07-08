# -*- coding: utf-8 -*-
"""Ontological agent logic with numerology-based behavior."""

import random


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Agents hold a numerology number that influences their actions. State
    transitions occur when emotion or tension surpass defined thresholds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    ACTIONS = ("Help", "Hurt", "Explore", "Conquer", "Reflect")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        numerology_number: int = 1,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.numerology_number = numerology_number
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # Numerology -----------------------------------------------------------
    def numerology_influence(self) -> str:
        """Return an action suggestion based on numerology."""
        if self.numerology_number == 1:
            return "Help"
        if self.numerology_number == 2:
            return "Hurt"
        if self.numerology_number == 3:
            return "Explore"
        return random.choice(self.ACTIONS)

    def perform_action(self) -> str:
        """Choose and return an action while subtly adjusting tension."""
        action = self.numerology_influence()
        if action == "Help":
            self.tension = max(self.tension - 0.1, 0.0)
        elif action == "Hurt":
            self.tension += 0.1
        return action

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
        """Return a philosophical answer based on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            base += " Čutim močna čustva ob tem."
        return base
