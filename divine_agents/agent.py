"""Ontological agents used in philosophical simulations."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}

    def update_emotion(self, value: float) -> None:
        """Update overall emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, fear: float = 0.0, joy: float = 0.0, anger: float = 0.0) -> None:
        """Update specific emotions and modify tension."""
        self.emotions["fear"] = fear
        self.emotions["joy"] = joy
        self.emotions["anger"] = anger
        self.update_emotion(max(fear, joy, anger))

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
        emotion_note = "" if self.emotion <= 0.5 else " Moja custva so mocna."
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + emotion_note
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z nasimi odnosi." + emotion_note
        return "Vse resnice so eno, medsebojno povezane." + emotion_note


class SecondaryAgent(Agent):
    """Agent that monitors another agent and intervenes when criteria are met."""

    def __init__(self, name: str, main_agent: Agent, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.main_agent = main_agent

    def monitor_main_agent(self) -> None:
        """Adjust internal state based on the observed agent."""
        if self.main_agent.state == "Enotnost" and self.main_agent.tension < 0.5:
            self.state = "Jaz"
            self.feel(fear=0.5)
            self.history.append(self.state)
