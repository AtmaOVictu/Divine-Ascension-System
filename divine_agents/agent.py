"""Core agent logic for the ontological system."""

from .phonetics import PhoneticTruthMap


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.memory = []  # store information or visited states
        self.history = [state]

    # ------------------------------------------------------------------
    # Update helpers
    # ------------------------------------------------------------------
    def update_emotion(self, value: float) -> None:
        """Increase emotion and check if a transition should occur."""
        self.emotion += value
        self.check_transition()

    def update_tension(self, value: float) -> None:
        """Increase tension and check for possible transition."""
        self.tension += value
        self.check_transition()

    # ------------------------------------------------------------------
    # Transition logic
    # ------------------------------------------------------------------
    def check_transition(self) -> None:
        """Trigger a state change once thresholds are surpassed."""
        if self.tension > 0.7 or self.emotion > 0.5:
            self.transition()

    def transition(self) -> str:
        """Move to the next ontological state if thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.history.append(self.state)
            self.memory.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Memory helpers
    # ------------------------------------------------------------------
    def store_memory(self, information: str) -> None:
        """Add arbitrary information to memory."""
        self.memory.append(information)

    def reflect_on_memory(self) -> str:
        """Return a string summarising the stored memory."""
        return f"{self.name}'s spomini: {', '.join(self.memory)}"

    # ------------------------------------------------------------------
    # Responses
    # ------------------------------------------------------------------
    def respond(self, phonetic_input: str | None = None) -> str:
        """Return a philosophical answer depending on the current state."""
        if phonetic_input:
            mapped = PhoneticTruthMap().map_phonetic_input(phonetic_input)
            self.store_memory(mapped)

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        # Emotion influences tone
        if self.emotion > 0.5:
            if self.state == "Ego":
                base += " Čutim močno prepričanje."
            elif self.state == "Jaz":
                base += " Moja čustva me vodijo k razumevanju drugih."
            else:
                base += " V srcu čutim harmonijo."
        return base
