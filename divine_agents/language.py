class LanguageModule:
    """Generate responses based on an agent's ontological state."""

    def formulate_response(self, state: str) -> str:
        if state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if state == "Jaz":
            return "Resnica je relativna, oblikovana z nasimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
