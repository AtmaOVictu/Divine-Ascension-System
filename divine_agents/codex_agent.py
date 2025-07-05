class CodexAgent:
    """Advanced agent with emotional and philosophical context."""

    STATES = ("Ego", "Jaz", "Enotnost", "Transcendenca")

    def __init__(self, name: str, state: str = "Ego"):
        self.name = name
        self.state = state
        self.tension = 0.0
        self.emotion = 0.0
        self.love = 0.0
        self.hate = 0.0
        self.history = [state]
        self.philosophical_context = {}

    def update_emotion(self) -> None:
        """Update emotion based on love and hate."""
        self.emotion = self.love - self.hate
        self.history.append(f"Emotion updated: {self.emotion}")

    def update_love(self, value: float) -> None:
        self.love = value
        self.update_emotion()

    def update_hate(self, value: float) -> None:
        self.hate = value
        self.update_emotion()

    def transition(self) -> str:
        """Move through states when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            elif self.state == "Enotnost":
                self.state = "Transcendenca"
        self.history.append(f"Transitioned to: {self.state}")
        return self.state

    def philosophical_analysis(self) -> None:
        """Store a short philosophical summary based on love and hate."""
        if self.love > self.hate:
            self.philosophical_context[self.name] = (
                "Agent is following a path of love and unity."
            )
        elif self.hate > self.love:
            self.philosophical_context[self.name] = (
                "Agent is experiencing conflict and division."
            )
        else:
            self.philosophical_context[self.name] = (
                "Agent is in a state of equilibrium."
            )

    def respond(self, question: str) -> str:
        """Return an answer about truth based on the current ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        if self.state == "Enotnost":
            return "Vse resnice so eno, medsebojno povezane."
        return "Transcendenca presega vse delitve resnice."

    def print_history(self) -> None:
        print(f"History of {self.name}:")
        for event in self.history:
            print(event)


class CriticalReflectionAgent(CodexAgent):
    """Agent capable of reflecting on its own actions."""

    def reflect_on_actions(self) -> None:
        if any(state == "Ego" for state in self.history):
            self.history.append(
                f"{self.name} is reflecting on Ego state: How does this affect my perception of reality?"
            )
        if any(state == "Jaz" for state in self.history):
            self.history.append(
                f"{self.name} is reflecting on Jaz state: Am I progressing towards unity?"
            )
        if any(state == "Enotnost" for state in self.history):
            self.history.append(
                f"{self.name} is reflecting on Enotnost state: Have I reached a state of transcendence?"
            )
        self.history.append(f"Critical reflection completed for {self.name}.")


class LoveHatePhilosophicalAgent(CriticalReflectionAgent):
    """Agent that analyses the influence of love and hate."""

    def evaluate_emotional_impact(self) -> None:
        if self.love > self.hate:
            self.history.append(
                f"{self.name} is motivated by love, seeking harmony and unity."
            )
        elif self.hate > self.love:
            self.history.append(
                f"{self.name} is motivated by hate, creating conflict and division."
            )
        else:
            self.history.append(
                f"{self.name} is in a state of emotional equilibrium, seeking balance."
            )


class CodexSimulation:
    """Run a simulation for a list of agents."""

    def __init__(self, agents):
        self.agents = agents

    def run_simulation(self) -> None:
        for agent in self.agents:
            agent.transition()
            agent.philosophical_analysis()
            agent.print_history()

    def print_agents_philosophical_context(self) -> None:
        for agent in self.agents:
            print(
                f"{agent.name}'s philosophical context: {agent.philosophical_context.get(agent.name, 'No analysis')}"
            )
