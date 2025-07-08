import logging


logger = logging.getLogger(__name__)


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        logger.debug("Initialized %s with state=%s, tension=%s, emotion=%s", self.name, self.state, self.tension, self.emotion)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        logger.info("%s emotion updated to %s, tension is now %s", self.name, self.emotion, self.tension)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        logger.info("%s tension set to %s", self.name, self.tension)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        prev_state = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        if prev_state != self.state:
            logger.info("%s transitioned from %s to %s", self.name, prev_state, self.state)
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            reply = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            reply = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            reply = "Vse resnice so eno, medsebojno povezane."
        logger.debug("%s in state %s responds: %s", self.name, self.state, reply)
        return reply
