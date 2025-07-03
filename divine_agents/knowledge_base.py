import copy

class KnowledgeBase:
    """Store pre-defined components for agents and tasks."""

    def __init__(self):
        self.library = {
            "nujnosti": ["nova naloga", "kritična napaka", "sprememba stanja"],
            "naloge": ["samospoznanje", "logični prehod", "emotivni prehod"],
            "agenti": ["Agent1", "Agent2", "Agent3"],
            "prehodi": ["samospoznanje", "logični prehod", "emotivni prehod"],
        }

    def print_from_library(self, category: str) -> str:
        """Print and return components for the given category."""
        if category in self.library:
            components = ", ".join(self.library[category])
            message = f"Komponente v kategoriji '{category}': {components}"
        else:
            message = f"Kategorija '{category}' ni najdena v bazi znanja."
        print(message)
        return message

    def copy_from_library(self, category: str):
        """Return a deep copy of components for the given category."""
        if category in self.library:
            return copy.deepcopy(self.library[category])
        print(f"Kategorija '{category}' ni najdena v bazi znanja.")
        return []
