class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent keeps track of its ontological ``state`` (``Ego`` -> ``Jaz`` ->
    ``Enotnost``), current ``tension`` level and ``emotion`` intensity.
    Emotions influence tension and may trigger a state transition.  The class is
    intentionally small so that it can easily be used and tested within unit
    tests.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = ""
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def apply_emotion(self, name: str, intensity: float) -> None:
        """Set a named emotion which also influences tension."""
        self.emotion_name = name
        self.update_emotion(intensity)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        previous = self.state
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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if self.emotion_name:
            return f"{base} (Čustvo: {self.emotion_name}, stopnja: {self.emotion:.2f})"
        return base

    def emotion_description(self) -> str:
        """Human readable description of the current emotion intensity."""
        if self.emotion < 0.33:
            return "miren"
        if self.emotion < 0.66:
            return "negotov"
        return "intenziven"
