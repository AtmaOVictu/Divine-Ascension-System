class SortingHatAgent:
    """Agent that sorts words into ontological boxes."""

    def __init__(self, name: str):
        self.name = name
        self.onto_box = []
        self.main_box = []
        self.branches = {}

    def sort(self, word: str) -> str:
        """Sort a word based on basic philosophical categories."""
        foundational = {"potential", "origin", "void", "nothingness"}
        main_concepts = {"truth", "self", "unity", "balance"}

        if word.lower() in foundational:
            self.onto_box.append(word)
            return "Onto"
        if word.lower() in main_concepts:
            self.main_box.append(word)
            return "Main Branch"

        key = word[0].lower()
        self.branches.setdefault(key, []).append(word)
        return f"Branch '{key.upper()}'"

    def get_sorted_boxes(self) -> dict:
        """Return current sorting state."""
        return {
            "Onto": self.onto_box,
            "Main Branch": self.main_box,
            "Branches": self.branches,
        }


class MultilingualSortingHatAgent(SortingHatAgent):
    """Sorting hat with simple multilingual awareness."""

    def __init__(self, name: str, language: str = "English"):
        super().__init__(name)
        self.language = language

    def sort(self, word: str) -> str:  # type: ignore[override]
        if self.language.lower() == "spanish":
            spanish_onto = {"verdad", "yo", "vacío"}
            if word.lower() in spanish_onto:
                self.onto_box.append(word)
                return "Onto"
        return super().sort(word)
