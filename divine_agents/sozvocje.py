class Sozvocje:
    """Simple graph structure holding concepts and their relations."""

    def __init__(self) -> None:
        self.nodes = set()
        self.edges = set()
        self.colors = {}
        self.descriptions = {}

    def add_node(self, name: str, color: str, description: str) -> None:
        self.nodes.add(name)
        self.colors[name] = color
        self.descriptions[name] = description

    def add_edge(self, n1: str, n2: str) -> None:
        self.edges.add((n1, n2))
