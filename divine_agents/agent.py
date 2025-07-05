from __future__ import annotations
from .processor import OntoProcesor, MetaEgo, MetaJaz, Bog


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

        # meta components and ontological processor
        self.meta_ego = MetaEgo()
        self.meta_jaz = MetaJaz()
        self.bog = Bog()
        self.meta_ego.napetost = tension
        self.onto_procesor = OntoProcesor(self, self.meta_ego, self.meta_jaz, self.bog)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.meta_ego.napetost = self.tension

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.meta_ego.napetost = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def prehod(self, simbol: str) -> None:
        """Use OntoProcesor to analyze a symbol and manage state."""
        self.onto_procesor.analizira_prehod(simbol)
        self.onto_procesor.izracunaj_napetost()
        self.onto_procesor.optimiziraj_prehod()

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
