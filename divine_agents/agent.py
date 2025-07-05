class Agent:
    """Represent an ontological agent capable of transitioning states.

    The agent holds an ontological ``state`` (``Ego`` → ``Jaz`` → ``Enotnost``)
    and responds to philosophical questions according to that state.  Emotional
    intensity influences the agent's tension level which in turn may trigger a
    state transition.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]
        self.regeneration_needed = False

    # ------------------------------------------------------------------
    # Emotion and tension management
    # ------------------------------------------------------------------

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, label: str, level: float) -> None:
        """Set emotion label and level."""
        self.emotion_label = label
        self.update_emotion(level)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # State transitions and regulation
    # ------------------------------------------------------------------

    def check_regeneration(self) -> None:
        """Determine if regeneration is required and trigger it."""
        if self.emotion < 0.2:
            self.regeneration_needed = True
            self.regenerate()

    def regenerate(self) -> None:
        """Reset emotion and tension to a neutral level."""
        if self.regeneration_needed:
            self.emotion = 0.5
            self.tension = 0.5
            self.regeneration_needed = False

    def regulate(self) -> None:
        """Balance extreme emotional states."""
        if self.emotion > 0.8:
            self.emotion -= 0.1
        elif self.emotion < 0.2:
            self.emotion += 0.1

    def modulate(self) -> None:
        """Trigger regeneration if emotion remains high while active."""
        if self.emotion > 0.7:
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
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        # Modify the response based on the current emotional label
        if self.emotion_label == "anger":
            base += " Čutim jezo ob tej razpravi."
        elif self.emotion_label == "joy":
            base += " To me veseli."
        elif self.emotion_label == "fear":
            base += " Občutim strah."
        elif self.emotion_label == "sorrow":
            base += " To me žalosti."

        return base
