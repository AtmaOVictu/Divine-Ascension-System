class Agent:
    """Ontološki agent, ki je sposoben prehajanja med stanj­i."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str | None = None) -> None:
        """Inicializira agenta.

        Parameters
        ----------
        name:
            Ime agenta.
        state:
            Začetno ontološko stanje (privzeto ``Ego``).
        tension:
            Začetna napetost.
        emotion:
            Začetna intenziteta čustev.
        emotion_label:
            Vrsta čustva (npr. ``fear``).
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, label: str) -> None:
        """Nastavi intenziteto in vrsto čustva ter prilagodi napetost."""
        self.emotion = value
        self.emotion_label = label
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
        """Pripravi filozofski odgovor glede na trenutno stanje in čustva."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        if self.emotion_label and self.emotion_label != "neutral":
            return f"Občutam {self.emotion_label}, zato menim: {base}"
        return base
