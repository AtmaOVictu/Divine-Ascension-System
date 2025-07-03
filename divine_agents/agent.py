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

    def respond(self, question: str, emotion: str) -> str:
        """Return a philosophical answer influenced by state and emotion.

        Parameters
        ----------
        question : str
            Ignored for now but kept for future expansion.
        emotion : str
            Current emotional context (e.g., ``"fear"``, ``"joy"``, ``"anger"``).

        Returns
        -------
        str
            Philosophical statement adjusted for the agent's state and emotion.
        """

        emotion = emotion.lower()
        responses = {
            "Ego": {
                "fear": "\u010cutim strah, a verjamem, da je resnica \u0161e vedno absolutna.",
                "joy": "Z veseljem zagovarjam absoluten pogled na resnico.",
                "anger": "Z jezo branim svoje prepri\u010danje o absolutni resnici.",
            },
            "Jaz": {
                "fear": "\u010ceprav me je strah, razumem, da je resnica relativna.",
                "joy": "Z veseljem priznavam relativnost resnice.",
                "anger": "Z jezo opozarjam, da se resnica oblikuje skozi odnose.",
            },
            "Enotnost": {
                "fear": "\u010cetudi obstaja strah, spoznavam, da so vse resnice ena.",
                "joy": "Z radostjo sprejemam, da so vse resnice medsebojno povezane.",
                "anger": "Tudi v jezi vidim, da je vse povezano v enotni resnici.",
            },
        }

        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z na\u0161imi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        modifier = responses.get(self.state, {}).get(emotion, "")
        return f"{base} {modifier}".strip()
