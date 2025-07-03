class Agent:
    """Ontological agent capable of transitioning states and moving between worlds."""

    STATES = ("Ego", "Jaz", "Enotnost")
    WORLDS = ("Miza", "Svet", "Vest")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, world: str = "Miza") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.world = world
        self.history = [state]

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

    def switch_world(self, new_world: str) -> None:
        """Switch to a different operational world."""
        if new_world in self.WORLDS:
            self.world = new_world

    def world_action(self) -> str:
        """Return a description of the agent's action in the current world."""
        if self.world == "Miza":
            return f"{self.name} strategizes at the table."
        if self.world == "Svet":
            return f"{self.name} interacts socially with others."
        return f"{self.name} seeks spiritual insight."

    def philosophical_statement(self) -> str:
        """Return a philosophical statement influenced by the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if self.emotion > 0.5:
            return base + " Čutim to močno!"
        return base

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        return self.philosophical_statement()
