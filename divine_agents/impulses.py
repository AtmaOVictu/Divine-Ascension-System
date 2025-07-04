class Volja:
    """Represents the impulse of will within the system."""

    def __init__(self):
        self.state = 0
        self.intensity = 0.0

    def aktivacija(self) -> str:
        """Activate will, moving from nothingness to action."""
        self.state = 1
        self.intensity = 1.0
        return "Volja je aktivirana: prehod iz nič v enoto."

    def sprememba(self) -> str:
        """Trigger a change to a new phase of will."""
        self.state = 2
        return "Volja je sprožila spremembo, prehod v novo fazo."

    def apply(self, agent) -> None:
        """Influence an agent by increasing emotion and tension."""
        agent.update_emotion(self.intensity)
        agent.transition()


class Vera:
    """Represents the impulse of faith within the system."""

    def __init__(self):
        self.state = 0
        self.intensity = 0.0

    def potrditev(self) -> str:
        """Confirm faith as a foundational recognition of reality."""
        self.state = 1
        self.intensity = 0.8
        return "Vera je postala temelj, prepoznavanje temeljev realnosti."

    def prepoznavanje(self) -> str:
        """Recognise the unknown and enable growth of faith."""
        self.state = 2
        return "Vera prepoznava neznano, omogoča širjenje obzorij in rasti."

    def apply(self, agent) -> None:
        """Influence an agent by increasing emotion and tension."""
        agent.update_emotion(self.intensity)
        agent.transition()


class Vzgib:
    """Combines will and faith impulses in an agent."""

    def __init__(self, volja: Volja | None = None, vera: Vera | None = None):
        self.volja = volja or Volja()
        self.vera = vera or Vera()

    def izvajanje(self, agent) -> tuple[str, str]:
        """Execute impulses on the given agent."""
        result_volja = self.volja.aktivacija()
        self.volja.apply(agent)
        result_vera = self.vera.potrditev()
        self.vera.apply(agent)
        return result_volja, result_vera
