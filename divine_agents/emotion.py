class EmotionalBox:
    """Manage emotional state updates based on language and ontological state."""

    def __init__(self, agent, language: str = "English"):
        self.agent = agent
        self.language = language

    def update_emotion(self):
        """Update emotion intensity according to language and state."""
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

        # Clamp emotion to [0,1]
        self.agent.emotion = min(1.0, max(0.0, self.agent.emotion))
        return self.agent.emotion
