class EmotionalBox:
    """Update agent emotion with language-aware rules."""
    def __init__(self, agent, language="English"):
        self.agent = agent
        self.language = language

    def update_emotion(self) -> float:
        """Adjust emotion based on language and current state."""
        if self.language == "English":
            if self.agent.state == "Ego":
                self.agent.emotion += 0.05
            elif self.agent.state == "Jaz":
                self.agent.emotion -= 0.03
            else:
                self.agent.emotion -= 0.1
        elif self.language == "Spanish":
            if self.agent.state == "Ego":
                self.agent.emotion += 0.1
            elif self.agent.state == "Jaz":
                self.agent.emotion -= 0.05
            else:
                self.agent.emotion -= 0.2
        elif self.language == "German":
            if self.agent.state == "Ego":
                self.agent.emotion += 0.02
            elif self.agent.state == "Jaz":
                self.agent.emotion -= 0.07
            else:
                self.agent.emotion -= 0.05
        # clamp to [0,1]
        self.agent.emotion = min(1.0, max(0.0, self.agent.emotion))
        return self.agent.emotion
