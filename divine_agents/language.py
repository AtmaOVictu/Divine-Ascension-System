class Language:
    """Basic representation of a language with grammar and semantics."""

    def __init__(self, name: str, rules: dict):
        self.name = name
        self.rules = rules
        self.constructs = []

    def add_construct(self, construct: str) -> None:
        """Add a new language construct."""
        self.constructs.append(construct)

    def interpret(self, expression: str) -> str:
        """Return a simple interpretation of the expression."""
        return f"Interpretation: {expression}"


class AgentLanguage(Language):
    """Language connected to an agent for managing state transitions."""

    def __init__(self, name: str, rules: dict, agent):
        super().__init__(name, rules)
        self.agent = agent

    def transition(self, emotion: float, tension: float) -> str:
        """Trigger an agent state transition based on emotion and tension."""
        self.agent.update_emotion(emotion)
        self.agent.update_tension(tension)
        return self.agent.transition()


class PhilosophicalLanguage(AgentLanguage):
    """Example language focusing on philosophical constructs."""

    def interpret(self, expression: str) -> str:
        return f"Filozofsko tolma\u010denje: {expression}"


class MathematicalLanguage(AgentLanguage):
    """Example language for simple mathematical expressions."""

    def interpret(self, expression: str) -> str:
        try:
            return str(eval(expression))  # nosec B307 - simplified for demo
        except Exception:
            return "Napaka"
