from .memory import Memory


class LanguageModule:
    """Generates philosophical responses based on agent state."""

    def compose_response(self, agent, question: str) -> str:
        if agent.state == "Ego":
            reply = "Resnica je absolutna in neodvisna od drugih."
        elif agent.state == "Jaz":
            reply = "Resnica je relativna, oblikovana z nasimi odnosi."
        else:
            reply = "Vse resnice so eno, medsebojno povezane."

        agent.memory.record(f"Q:{question} A:{reply}")
        return reply
