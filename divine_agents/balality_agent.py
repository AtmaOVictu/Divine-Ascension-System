class BalalityAgent:
    """Agent that transitions through Ego, Jaz, and Enotnost based on tension and emotion."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set tension level directly."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Generate an answer reflecting the agent's current ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def reflect_on_duality(self) -> str:
        """Return introspective statement based on current state."""
        if self.state == "Ego":
            return f"{self.name}: Zavedam se sebe, a spoznati moram druge."
        if self.state == "Jaz":
            return f"{self.name}: V odnosih iščem resnico, a še vedno sem razdvojen."
        return f"{self.name}: Dosegel sem enotnost, a dvojnost še obstaja v meni."


def balality_dialogue(agent1: BalalityAgent, agent2: BalalityAgent):
    """Facilitate a short dialogue demonstrating state transitions."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(agent1.emotion + 0.6)
    agent2.update_emotion(agent2.emotion + 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(agent1.reflect_on_duality())
    lines.append(agent2.reflect_on_duality())
    return lines
