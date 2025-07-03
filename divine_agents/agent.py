"""Osnovni ontološki agent."""

from dataclasses import dataclass


@dataclass
class Emotion:
    """Model čustva z intenziteto."""

    name: str = "nevtralno"
    intensity: float = 0.0


class Agent:
    """Predstavlja agenta, ki lahko prehaja med stanjema Ego, Jaz in Enotnost."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion()
        self.history = [state]

    def update_emotion(self, name: str, intensity: float) -> None:
        """Nastavi čustvo in primerno poveča napetost."""
        self.emotion = Emotion(name, intensity)
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Izvede prehod stanja, če so preseženi pragovi."""
        if self.tension > 0.7 or self.emotion.intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Vrne filozofski odgovor glede na stanje in čustvo."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion.name != "nevtralno":
            return f"{base} Občutim {self.emotion.name}."
        return base
