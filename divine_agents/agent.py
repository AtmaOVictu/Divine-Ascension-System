class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally its type."""
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
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
        """Return a philosophical answer depending on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_note = ""
        intensity = self.emotion
        etype = getattr(self, "emotion_type", "neutral")
        if etype == "fear":
            if intensity > 0.7:
                emotion_note = " Govorim previdno in obrambno zaradi strahu."
            elif intensity > 0.3:
                emotion_note = " Zadržano odgovarjam zaradi rahlega strahu."
        elif etype == "joy":
            if intensity > 0.7:
                emotion_note = " Veselje prežema moje besede."
            elif intensity > 0.3:
                emotion_note = " V odgovoru se čuti kanček veselja."
        elif etype == "anger":
            if intensity > 0.7:
                emotion_note = " Jeza krepi mojo odločnost." 
            elif intensity > 0.3:
                emotion_note = " Jezen sem, kar se odraža v tonu."

        return f"{base}{emotion_note}"
