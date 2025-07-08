class LanguageModule:
    """Interpret and generate language influenced by agent state."""

    def __init__(self, agent) -> None:
        self.agent = agent

    def process_input(self, text: str) -> None:
        if "angry" in text:
            self.agent.update_emotion(0.6)
        elif "calm" in text:
            self.agent.update_emotion(0.2)

    def generate_response(self) -> str:
        if self.agent.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.agent.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
