from .agent import Agent


class RespectAgent(Agent):
    """Agent that emphasizes respect and order."""

    def respond(self, question: str) -> str:
        if self.state == "Ego":
            return "Spoštovanje je temeljno načelo, ki ohranja red."
        return super().respond(question)


class DisrespectAgent(Agent):
    """Agent that questions rules and respect."""

    def respond(self, question: str) -> str:
        if self.state == "Ego":
            return "Pravila so za kršenje, spoštovanje je iluzija."
        return super().respond(question)


class FearAgent(Agent):
    """Agent driven primarily by fear."""

    def respond(self, question: str) -> str:
        if self.state == "Ego":
            return "Strah vodi naše odločitve, delujemo da se izognemo škodi."
        return super().respond(question)


class OneValueAgent(Agent):
    """Agent that bases decisions on a single value."""

    def __init__(self, name: str, value: float = 1.0, **kwargs):
        super().__init__(name, **kwargs)
        self.value = value

    def respond(self, question: str) -> str:
        if self.value > 0.5:
            return "Odločam se na podlagi ene same vrednosti."
        return "Ne vidim veliko dlje od tega."
