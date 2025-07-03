import copy

class KnowledgeBase:
    """Simple repository of predefined components."""

    def __init__(self):
        self.library = {
            "nujnosti": ["nova naloga", "kritična napaka", "sprememba stanja"],
            "naloge": ["samospoznanje", "logični prehod", "emotivni prehod"],
            "agenti": ["Agent1", "Agent2", "Agent3"],
            "prehodi": ["samospoznanje", "logični prehod", "emotivni prehod"],
        }

    def print_from_library(self, category: str) -> None:
        if category in self.library:
            print(f"Komponente v kategoriji '{category}': {self.library[category]}")
        else:
            print(f"Kategorija '{category}' ni najdena v bazi znanja.")

    def copy_from_library(self, category: str):
        if category in self.library:
            return copy.deepcopy(self.library[category])
        print(f"Kategorija '{category}' ni najdena v bazi znanja.")
        return []
