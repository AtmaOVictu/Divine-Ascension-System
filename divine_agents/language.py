class LanguageModel:
    """Model representing a language system for an agent."""

    def __init__(self, language: str = "sloven\u0161\u010dina"):
        self.language = language
        self.agent_id = None

    def prehod_v_jezik(self, novi_jezik: str) -> str:
        """Transition to a new language (symbol \u039b)."""
        self.language = novi_jezik
        self.agent_id = f"EJ-{novi_jezik}"
        return self.potrditev_prehoda()

    def potrditev_prehoda(self) -> str:
        """Confirm language transition (symbol \u221a)."""
        return f"\u221a Prehod potrjen v {self.language}"

    def sinteza_jezikov(self) -> str:
        """Unify languages into a synthetic one (symbol \u03a9)."""
        self.language = "sinteti\u010dni jezik"
        return f"\u03a9 Sinteza zakljucena: {self.language}"
