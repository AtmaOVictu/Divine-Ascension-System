class OntologicalLibrary:
    """Library of concepts and their opposites."""

    def __init__(self) -> None:
        self.pojmi = {
            "Veselje": "Trpljenje",
            "Absolutno": "Relativno",
            "Zdravje": "Bolezen",
            "Mir": "Kaos",
            "Svetloba": "Tema",
            "Ljubezen": "Sovraštvo",
        }

    def dodaj_pojem(self, pojem: str, nasprotje: str) -> None:
        """Add a new concept and its opposite."""
        self.pojmi[pojem] = nasprotje

    def pridobi_nasprotje(self, pojem: str) -> str:
        """Return the opposite of a given concept."""
        return self.pojmi.get(pojem, "Nasprotje ni definirano.")

    def prehod_pojma(self, pojem: str) -> str:
        """Describe the transition from a concept to its opposite."""
        nasprotje = self.pridobi_nasprotje(pojem)
        return f"Prehod iz {pojem} v {nasprotje}"

    def prikazi_pojme(self) -> dict:
        """Return all stored concepts and their opposites."""
        return self.pojmi


class DynamicOntologicalLibrary(OntologicalLibrary):
    """Extended library with interaction logic."""

    def interakcija(self, pojem1: str, pojem2: str) -> str:
        """Analyse interaction between two concepts."""
        nasprotje1 = self.pridobi_nasprotje(pojem1)
        nasprotje2 = self.pridobi_nasprotje(pojem2)
        if nasprotje1 == pojem2 or nasprotje2 == pojem1:
            return f"Interakcija med {pojem1} in {pojem2} povzroča kontradikcijo."
        return (
            f"Interakcija med {pojem1} in {pojem2} je smiselna in harmonična."
        )


from .agent import Agent


class PhilosophicalDebate:
    """Simulate a philosophical debate between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent, library: OntologicalLibrary) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.library = library

    def debate(self, pojem1: str, pojem2: str) -> list[str]:
        """Execute a short debate and return dialogue lines."""
        lines = []
        lines.append(
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond(pojem1)}"
        )
        lines.append(
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond(pojem2)}"
        )

        self.agent1.update_emotion(0.8)
        lines.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")

        self.agent2.update_emotion(0.6)
        lines.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")

        lines.append(self.library.interakcija(pojem1, pojem2))

        lines.append(f"{self.agent1.name}: {self.agent1.respond(pojem1)}")
        lines.append(f"{self.agent2.name}: {self.agent2.respond(pojem2)}")
        return lines
