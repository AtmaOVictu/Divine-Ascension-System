import math


def logistic_function(t: float, k: float, c: float) -> float:
    """Return logistic transition value."""
    return 1 / (1 + math.exp(-k * (t - c)))


def logarithmic_function(t: float, k: float, c: float) -> float:
    """Return logarithmic growth value."""
    return k * math.log(t + c)


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


class CodexAgent(Agent):
    """Agent that evolves using logistic and logarithmic transitions."""

    def __init__(self, name: str, emotion_type: str = "neutral", k_bio: float = 1.0,
                 c_bio: float = 0.5, k_soc: float = 1.5, c_soc: float = 0.6,
                 state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.emotion_type = emotion_type
        self.k_bio = k_bio
        self.c_bio = c_bio
        self.k_soc = k_soc
        self.c_soc = c_soc

    def update_emotion(self, value: float) -> None:  # type: ignore[override]
        """Adjust emotion and update tension based on emotion type."""
        self.emotion = value
        if self.emotion_type == "positive":
            self.tension += value
        elif self.emotion_type == "negative":
            self.tension -= value
        else:
            self.tension += value / 2

    def evolve(self) -> str:
        """Update tension using logistic and logarithmic functions then transition."""
        bio = logistic_function(self.tension, self.k_bio, self.c_bio)
        soc = logarithmic_function(self.tension, self.k_soc, self.c_soc)
        self.tension = bio + soc
        return self.transition()
