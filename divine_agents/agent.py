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
        """Return a philosophical answer that incorporates the provided question."""
        q = question.lower()

        if "resnica" in q or "truth" in q:
            if self.state == "Ego":
                return "Resnica je absolutna in neodvisna od drugih."
            if self.state == "Jaz":
                return "Resnica je relativna, oblikovana z našimi odnosi."
            return "Vse resnice so eno, medsebojno povezane."

        if "smisel" in q or "meaning" in q or "purpose" in q:
            if self.state == "Ego":
                return "Smisel življenja je v osebni izpolnitvi."
            if self.state == "Jaz":
                return "Smisel življenja se razkriva v naših odnosih."
            return "Smisel življenja je v enosti vseh stvari."

        if self.state == "Ego":
            return (
                f"V stanju Ego razmišljam, da je odgovor na '{question}' "
                "povezan z mojo lastno perspektivo."
            )
        if self.state == "Jaz":
            return (
                f"V stanju Jaz menim, da '{question}' oblikujejo naše "
                "medsebojne povezave."
            )
        return (
            f"V stanju Enotnost vidim '{question}' kot del enotne resnice."
        )
