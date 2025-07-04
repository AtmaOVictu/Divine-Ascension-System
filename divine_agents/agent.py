from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    NEGATIVE_EMOTIONS = {"fear", "anger"}
    POSITIVE_EMOTIONS = {"joy"}

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_level: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion_type = emotion_type
        self.history: List[str] = [state]

    def update_emotion(self, emotion_type: str, level: float) -> None:
        """Update emotion type and level, adjusting tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion_level = level
        if emotion_type in self.NEGATIVE_EMOTIONS:
            self.tension += level
        elif emotion_type in self.POSITIVE_EMOTIONS:
            self.tension = max(0.0, self.tension - level / 2)
        else:
            self.tension += level / 2

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        emotion_note = ""
        if self.emotion_type == "fear":
            emotion_note = "Občutim strah. "
        elif self.emotion_type == "anger":
            emotion_note = "Čutim jezo. "
        elif self.emotion_type == "joy":
            emotion_note = "Vesel sem. "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_note}{base}"
