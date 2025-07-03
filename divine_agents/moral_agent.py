class MoralAgent:
    """Agent with moral decision-making, extending ontological Agent."""
    STATES = ("Ego", "Jaz", "Enotnost")
    ETHICS = ("utilitarianism", "deontology", "virtue", "justice")

    def __init__(self, name: str, ethics: str = "utilitarianism", state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.ethics = ethics
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        self.tension = value

    def transition(self) -> str:
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def make_decision(self, others: list) -> str:
        if self.ethics == "utilitarianism":
            total_emotion = sum(a.emotion for a in others) + self.emotion
            if total_emotion > len(others):
                return "Maximize happiness for all"
            return "Minimize suffering for most"
        if self.ethics == "deontology":
            return "Follow rules regardless of outcome"
        if self.ethics == "virtue":
            return "Act according to virtues"
        return "Seek justice for everyone"
