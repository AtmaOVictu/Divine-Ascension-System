"""Ontological agent capable of state transitions and moral reasoning."""

from __future__ import annotations


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str | None = None,
        morality: str = "Egoizem",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.morality = morality
        self.history: list[str] = [state]

    # ------------------------------------------------------------------
    # Update methods
    # ------------------------------------------------------------------
    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        if emotion_type:
            self.emotion_type = emotion_type
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # Core behaviour
    # ------------------------------------------------------------------
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
        if self.state == "Enotnost":
            return "Vse resnice so eno, medsebojno povezane."
        return """Nisem prepričan, kako odgovoriti."""

    # ------------------------------------------------------------------
    # Moral reasoning and reflections
    # ------------------------------------------------------------------
    def resolve_moral_dilemma(self) -> str:
        """Resolve a moral dilemma based on current morality setting."""
        if self.morality == "Altruizem":
            return "Delujem v dobro drugih in skušam zmanjšati trpljenje."
        elif self.morality == "Egoizem":
            return "Delujem v lastno korist, da povečam svojo srečo."
        elif self.morality == "Socializem":
            return "Delujem v interesu skupnosti, z namenom pravičnosti in enakosti."
        elif self.morality == "Kapitalizem":
            return "Delujem v interesu trga, kjer je najboljši rezultat tisti, ki prinaša največjo korist."
        elif self.morality == "Individualizem":
            return "Delujem na podlagi osebne svobode, z visoko stopnjo samostojnosti."
        elif self.morality == "Kolektivizem":
            return "Delujem za dobrobit skupine, kjer je posameznik podrejen skupnim ciljem."
        return "Nisem prepričan, kakšen moralni pristop naj sprejmem, zato raziskujem."

    def reflect_on_dilemma(self) -> str:
        """Provide a philosophical reflection on the current moral dilemma."""
        if self.state == "Ego":
            return "V tem stanju čutim, da sem ločen od drugih, kar ustvarja napetost v mojem razumevanju resnice."
        elif self.state == "Jaz":
            return "Sem v fazi iskanja ravnotežja med individualno svobodo in povezovanjem z drugimi. To oblikuje moje dojemanje resnice."
        elif self.state == "Enotnost":
            return "V tem stanju sem zavedajoč se povezanosti vsega, kjer so vse dileme in nasprotja del večje harmonije."
        return "Ni določenega stanja za refleksijo."

    def display_history(self) -> str:
        """Display the agent's state history to observe transitions."""
        return f"Zgodovina stanj: {', '.join(self.history)}"
