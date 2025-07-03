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

    def respond(self, question: str, emotion: str | None = None) -> str:
        """Return a philosophical answer depending on the current state.

        The returned statement is influenced by the provided emotion:
        fear, joy or anger. Each emotion prepends a phrase to the base
        statement for the agent's ontological state.
        """

        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }

        emotion_prefix = {
            "fear": {
                "Ego": "V strahu zagovarjam, da ",
                "Jaz": "S strahom razumem, da ",
                "Enotnost": "Čeprav me je strah, verjamem, da ",
            },
            "joy": {
                "Ego": "Z veseljem trdim, da ",
                "Jaz": "Z radostjo vidim, da ",
                "Enotnost": "Z veseljem razkrivam, da ",
            },
            "anger": {
                "Ego": "V jezi vztrajam, da ",
                "Jaz": "V jezi spoznavam, da ",
                "Enotnost": "Kljub jezi verjamem, da ",
            },
        }

        prefix = ""
        if emotion and emotion in emotion_prefix:
            prefix = emotion_prefix[emotion][self.state]

        return f"{prefix}{base[self.state]}"
