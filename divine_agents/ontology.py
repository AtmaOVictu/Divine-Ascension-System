class OntologicalLibrary:
    """A simple library storing terms and their opposites."""

    def __init__(self):
        self.terms = {
            "Veselje": "Trpljenje",
            "Absolutno": "Relativno",
            "Zdravje": "Bolezen",
            "Mir": "Kaos",
            "Svetloba": "Tema",
            "Ljubezen": "Sovraztvo",
        }

    def add_term(self, term: str, opposite: str) -> None:
        """Add a new term and its opposite."""
        self.terms[term] = opposite

    def get_opposite(self, term: str) -> str:
        """Return the opposite of a given term."""
        return self.terms.get(term, "Nasprotje ni definirano.")

    def transition_term(self, term: str) -> str:
        """Return a string representing the transition from term to its opposite."""
        opposite = self.get_opposite(term)
        return f"Prehod iz {term} v {opposite}"


class DynamicOntologicalLibrary(OntologicalLibrary):
    """An extension of OntologicalLibrary providing interaction analysis."""

    def interaction(self, term1: str, term2: str) -> str:
        """Return a message describing the interaction between two terms."""
        opposite1 = self.get_opposite(term1)
        opposite2 = self.get_opposite(term2)
        if opposite1 == term2 or opposite2 == term1:
            return f"Interakcija med {term1} in {term2} povzroca kontradikcijo."
        return f"Interakcija med {term1} in {term2} je smiselna in harmonicna."
