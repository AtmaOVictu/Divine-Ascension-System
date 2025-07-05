from .emotion import EmotionSystem
from .ethics import EthicsJudgement
from .rl import ReinforcementLearner


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.emotion_system = EmotionSystem(emotion, tension)
        self.ethics = EthicsJudgement()
        self.learner = ReinforcementLearner()
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_system.update_emotion(value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.emotion_system.set_tension(value)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        # Use reinforcement learner to determine an action (placeholder actions)
        action = self.learner.choose_action(self.state, ["Aktiviraj", "Prehod", "Zaklju\u010di"])
        self.learner.update(self.state, action, self.emotion_system.emotion + self.emotion_system.tension)

        if self.emotion_system.tension > 0.7 or self.emotion_system.emotion > 0.5:
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

        emotion_note = f"(čustvo: {self.emotion_system.emotion:.2f}, napetost: {self.emotion_system.tension:.2f})"
        return f"{base} {emotion_note}"
