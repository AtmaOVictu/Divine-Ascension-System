from .phonetics import PhoneticTruthMap


class Agent:
    """Ontological agent capable of transitioning states and interpreting phonetic input."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self._phonetic_map = PhoneticTruthMap()

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

    def _mood_descriptor(self) -> str:
        """Provide a short textual description of the agent's emotional intensity."""
        if self.emotion > 0.7:
            return "strastno"
        if self.emotion > 0.4:
            return "vznemirjeno"
        return "mirno"

    def interpret_phoneme(self, phoneme: str) -> str:
        """Map phonetic input to a philosophical term."""
        return self._phonetic_map.map_phonetic_input(phoneme)

    def respond(self, question: str, phoneme: str | None = None) -> str:
        """Return a philosophical answer influenced by state, emotion and phonetic input."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        mood = self._mood_descriptor()
        if phoneme:
            meaning = self.interpret_phoneme(phoneme)
            return f"({phoneme} → {meaning}) {base} Agent je {mood}."
        return f"{base} Agent je {mood}."
