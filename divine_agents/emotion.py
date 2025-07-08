class EmotionalBox:
    """Handle language-aware emotional updates for agents."""

    def __init__(self, agent, language: str = "English"):
        self.agent = agent
        self.language = language

    def update_emotion(self) -> float:
        """Update the agent's emotion depending on the language and state."""
        delta = 0.0
        if self.language == "English":
            if self.agent.state == "Ego":
                delta = 0.05
            elif self.agent.state == "Jaz":
                delta = -0.03
            else:
                delta = -0.1
        elif self.language == "Spanish":
            if self.agent.state == "Ego":
                delta = 0.1
            elif self.agent.state == "Jaz":
                delta = -0.05
            else:
                delta = -0.2
        elif self.language == "German":
            if self.agent.state == "Ego":
                delta = 0.02
            elif self.agent.state == "Jaz":
                delta = -0.07
            else:
                delta = -0.05
        else:
            delta = 0.05

        new_value = self.agent.emotion + delta
        new_value = max(0.0, min(1.0, new_value))
        # use agent method to ensure tension updates
        self.agent.update_emotion(new_value)
        return self.agent.emotion
