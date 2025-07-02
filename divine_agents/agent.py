class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Human readable identifier for the agent.
    state:
        Starting ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension:
        Initial tension level. Values above ``0.7`` trigger a transition.
    emotion:
        Initial emotion intensity. Values above ``0.5`` trigger a transition.
    materials:
        Optional list of philosophical texts influencing the agent.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, materials=None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.materials = list(materials) if materials else []
        self.philosophical_beliefs = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def add_material(self, material: str) -> None:
        """Attach philosophical material to the agent."""
        self.materials.append(material)

    def analyze_materials(self) -> None:
        """Derive beliefs from the currently attached materials."""
        for material in self.materials:
            text = material.lower()
            if "absolut" in text:
                belief = "Resnica je absolutna in neodvisna od drugih."
            elif "relativ" in text:
                belief = "Resnica je relativna, oblikovana z našimi odnosi."
            elif "enot" in text:
                belief = "Vse resnice so eno, medsebojno povezane."
            else:
                continue
            if belief not in self.philosophical_beliefs:
                self.philosophical_beliefs.append(belief)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            elif self.state == "Enotnost":
                self.state = "Ego"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if self.emotion > 0.5:
            return f"{base} (Čustva vplivajo na moje dojemanje.)"
        return base
