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
        """Return a philosophical answer influenced by emotion and state."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{base} Čustvo: {self.emotion:.1f}."


class RespectAgent(Agent):
    """Agent that prioritises respect and order."""

    def respond(self, question: str) -> str:
        if self.state == "Ego":
            return "Spoštovanje je temeljni princip, ki ohranja red."
        return super().respond(question)


class DisrespectAgent(Agent):
    """Agent that challenges rules and conventions."""

    def respond(self, question: str) -> str:
        if self.state == "Ego":
            return "Pravila so zato, da se kršijo, spoštovanje je iluzija."
        return super().respond(question)


class FearAgent(Agent):
    """Agent driven by fear."""

    def respond(self, question: str) -> str:
        if self.state == "Ego":
            return "Strah usmerja naše odločitve; delujemo, da preprečimo škodo."
        return super().respond(question)


class OneValueAgent(Agent):
    """Agent focusing on a single guiding value."""

    def __init__(self, name: str, value: float = 1.0, **kwargs):
        super().__init__(name, **kwargs)
        self.value = value

    def respond(self, question: str) -> str:
        if self.value > 0.5:
            return "Odločitve sprejemam na podlagi ene same vrednosti."
        return "Težko vidim kaj več od tega."
