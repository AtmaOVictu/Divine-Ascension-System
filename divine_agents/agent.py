class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent also tracks a ``balality`` value representing latent potential
    between opposites. When a transition occurs this potential is converted into
    an ability improvement.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        balality: float = 0.0,
        abilities: dict | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.balality = balality
        self.abilities = abilities or {
            "creativity": 0.0,
            "logic": 0.0,
            "empathy": 0.0,
        }
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        # store potential for ability growth
        self.balality += value / 2

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.balality += value / 2

    def improve_ability(self, ability: str) -> None:
        """Increase a specific ability based on accumulated balality."""
        amount = min(1.0, self.abilities.get(ability, 0.0) + self.balality)
        self.abilities[ability] = amount
        self.balality = 0.0

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
                self.improve_ability("empathy")
            elif self.state == "Jaz":
                self.state = "Enotnost"
                self.improve_ability("creativity")
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_prefix = ""
        if self.emotion > 0.7:
            emotion_prefix = "(z močnimi čustvi) "
        elif self.emotion > 0.3:
            emotion_prefix = "(čustveno) "

        if self.state == "Ego":
            return f"{emotion_prefix}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{emotion_prefix}Resnica je relativna, oblikovana z našimi odnosi."
        return f"{emotion_prefix}Vse resnice so eno, medsebojno povezane."

