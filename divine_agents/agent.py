import random
from typing import List, Optional


class Agent:
    """Represent an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier of the agent.
    state:
        Initial ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Current level of tension influencing transitions.
    emotion:
        Current intensity of emotion influencing transitions.
    dna:
        Optional vector representing the agent's internal "DNA" used for
        mutation and reincarnation.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, dna: Optional[List[float]] = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        if dna is not None:
            self.dna = list(dna)
        else:
            self.dna = [random.random() for _ in range(10)]
        self.history = [state]

    # ------------------------------------------------------------------
    # Evolution utilities
    # ------------------------------------------------------------------
    def mutate(self, rate: float = 0.01) -> List[float]:
        """Return a mutated copy of the agent's DNA.

        Parameters
        ----------
        rate:
            Fraction of genes to mutate. At least one gene will be changed.
        """

        new_dna = self.dna.copy()
        num_genes = len(new_dna)
        count = max(1, int(num_genes * rate))
        indices = random.sample(range(num_genes), count)
        for i in indices:
            new_dna[i] = min(1.0, max(0.0, new_dna[i] + random.uniform(-0.1, 0.1)))
        return new_dna

    def reincarnate(self, new_name: str) -> "Agent":
        """Create a new agent with mostly identical DNA."""
        mutated = self.mutate(rate=0.01)
        return Agent(new_name, state=self.state, tension=self.tension,
                     emotion=self.emotion, dna=mutated)

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
