from .agent import Agent

class LanguageModule:
    """Handle language processing for an agent."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def process_input(self, text: str) -> None:
        """Adjust emotion based on simple keywords."""
        if "angry" in text:
            self.agent.update_emotion(0.8)
        elif "calm" in text:
            self.agent.update_emotion(0.2)

    def generate_response(self) -> str:
        """Generate a philosophical response based on agent state."""
        if self.agent.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.agent.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
