class LanguageModule:
    """Process language input and generate agent responses."""

    def __init__(self, agent):
        self.agent = agent

    def process_input(self, text: str) -> None:
        """Update emotion based on simple keyword detection."""
        if "fear" in text.lower() or "anger" in text.lower():
            self.agent.update_emotion(0.6)
        elif "joy" in text.lower() or "calm" in text.lower():
            self.agent.update_emotion(0.2)

    def generate_reply(self) -> str:
        """Generate a philosophical reply based on the agent state."""
        return self.agent.respond("Kaj je resnica?")
