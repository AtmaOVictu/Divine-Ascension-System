from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    #: Possible ontological states the agent can occupy.
    STATES = ("Ego", "Jaz", "Enotnost")

    #: Mapping from state to its philosophical stance on truth.
    TRUTHS = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    #: Optional prefixes that colour responses based on emotion.
    EMOTION_PREFIX = {
        "jeza": "Jezen odgovarjam: ",
        "strah": "S strahom povem: ",
        "veselje": "Z veseljem povem: ",
        "žalost": "Žalostno dodajam: ",
        "mirnost": "Mirno pravim: ",
    }

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: str = "mirnost",
        emotion_intensity: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_intensity = emotion_intensity
        self.history: List[str] = [state]

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Update emotion type and intensity and adjust tension."""
        self.emotion = emotion
        self.emotion_intensity = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = self.EMOTION_PREFIX.get(self.emotion, "")
        return prefix + self.TRUTHS.get(self.state, "")


