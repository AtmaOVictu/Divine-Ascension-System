import random


class Agent:
    """Represent an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier for the agent.
    state:
        Initial ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Initial tension value.
    emotion:
        Initial emotion intensity.
    numerology:
        Optional numerology number guiding hidden actions.
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    ACTIONS = ("Help", "Hurt", "Explore", "Conquer", "Reflect")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, numerology: int | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.numerology = numerology
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def numerology_action(self) -> str:
        """Return action influenced by numerology number."""
        if self.numerology == 1:
            return self.ACTIONS[0]
        if self.numerology == 2:
            return self.ACTIONS[1]
        if self.numerology == 3:
            return self.ACTIONS[2]
        if self.numerology == 4:
            return self.ACTIONS[3]
        if self.numerology:
            return self.ACTIONS[4]
        return random.choice(self.ACTIONS)

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
        """Return a philosophical answer depending on state and emotion."""
        prefix = "Čustveno " if self.emotion > 0.5 else ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{base}"
