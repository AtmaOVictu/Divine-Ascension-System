import time


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent keeps track of when it was created (absolute time) and how much
    time has passed since its creation when a transition occurs (relative time).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.time_base = time.time()
        self.transition_time = 0.0

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # Emotions directly influence tension
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
        self.transition_time = time.time() - self.time_base
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
            if self.emotion > 0.5:
                return f"Z vsem srcem verjamem, da {base.lower()}"
            return base
        if self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
            if self.emotion > 0.5:
                return f"Čutim, da je {base.lower()}"
            return base
        base = "Vse resnice so eno, medsebojno povezane."
        if self.emotion > 0.5:
            return f"Z radostjo sprejemam, da so {base.lower()}"
        return base
