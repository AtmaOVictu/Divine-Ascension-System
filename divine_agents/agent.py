from .intensity import Intensity


class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # Each agent tracks intensity for colour coded feedback
        self.intensity = Intensity()
        self.last_colour = ""

    def _determine_intensity_state(self) -> str:
        """Map current tension to an intensity state name."""
        if self.tension >= 0.7:
            return "visoka napetost"
        if self.tension >= 0.4:
            return "prehod"
        if self.tension >= 0.2:
            return "stabilnost"
        if self.emotion > 0:
            return "razjasnitev"
        return "negacija"

    def update_emotion(self, value: float) -> str:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.intensity.stanje = self._determine_intensity_state()
        self.last_colour = self.intensity.povecaj_intenziteto()
        return self.last_colour

    def update_tension(self, value: float) -> str:
        """Directly set tension level and return colour."""
        self.tension = value
        self.intensity.stanje = self._determine_intensity_state()
        self.last_colour = self.intensity.povecaj_intenziteto()
        return self.last_colour

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
        """Return a philosophical answer depending on the current state.

        The answer is capitalised when emotion or tension exceed thresholds and
        includes a colour indicator describing the current intensity.
        """
        if self.state == "Ego":
            msg = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            msg = "Vse resnice so eno, medsebojno povezane."

        if self.tension > 0.7 or self.emotion > 0.5:
            msg = msg.upper()

        colour = self.last_colour or self.intensity.povecaj_intenziteto()
        return f"{msg} ({colour})"
