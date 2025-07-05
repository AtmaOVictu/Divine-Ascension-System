class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent holds an ontological ``state`` (``Ego``, ``Jaz`` or ``Enotnost``)
    and can adjust its emotional level and tension.  State transitions occur
    when tension exceeds ``0.7`` or emotion exceeds ``0.5``.  Additional helper
    methods enable regulation, modulation and regeneration of the agent's
    internal parameters.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.regeneration_needed = False

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def check_regeneration(self) -> None:
        """Trigger regeneration if emotional values are very low."""
        if self.emotion < 0.2 and self.tension < 0.2:
            self.regeneration_needed = True
            self.regenerate()

    def regenerate(self) -> None:
        """Restore neutral emotion and tension levels when required."""
        if self.regeneration_needed:
            self.emotion = 0.5
            self.tension = 0.5
            self.regeneration_needed = False

    def regulate(self) -> None:
        """Balance extreme emotions to keep the agent stable."""
        if self.emotion > 0.8:
            self.emotion -= 0.1
        elif self.emotion < 0.2:
            self.emotion += 0.1

    def modulate(self) -> None:
        """Recalibrate if emotions run high while active."""
        if self.emotion > 0.7 and self.state != "Enotnost":
            self.regeneration_needed = True
            self.check_regeneration()

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
        emotion_note = ""
        if self.emotion > 0.7:
            emotion_note = " (izraža močna čustva)"
        elif self.emotion < 0.3:
            emotion_note = " (izraža umirjenost)"

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return base + emotion_note
