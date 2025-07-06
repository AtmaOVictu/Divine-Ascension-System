class Categorizer:
    """Categorizes terms and stores their connotations."""

    def __init__(self):
        self.catalog = {}

    def add_term(self, term: str, category: str, connotation: str) -> None:
        """Add a term with its category and connotation."""
        self.catalog[term] = {
            "category": category,
            "connotation": connotation,
        }

    def categorize(self, term: str) -> dict:
        """Return category and connotation for a term."""
        return self.catalog.get(term, {"category": "unknown", "connotation": ""})

    def enumerate_category(self, category: str):
        """Return all terms belonging to a given category."""
        return [t for t, data in self.catalog.items() if data["category"] == category]
