class MetaEgo:
    """Simple meta-ego controller tracking tension."""

    def __init__(self) -> None:
        self.napetost = 0.0

    def usklajuj(self) -> None:
        """Harmonize tension by slightly reducing it."""
        self.napetost = max(0.0, self.napetost - 0.1)


class MetaJaz:
    """Placeholder meta-self stabilizer."""

    def stabiliziraj(self) -> None:
        pass


class Bog:
    """Placeholder representing universal laws."""

    def uravnavaj(self, agent: "Agent") -> None:  # type: ignore
        pass


class OntoProcesor:
    """Central unit managing ontological transitions for an agent."""

    def __init__(self, agent: "Agent", meta_ego: MetaEgo, meta_jaz: MetaJaz, bog: Bog) -> None:  # type: ignore
        self.agent = agent
        self.meta_ego = meta_ego
        self.meta_jaz = meta_jaz
        self.bog = bog

    def izracunaj_napetost(self) -> None:
        """Check tension and harmonize if above threshold."""
        self.meta_ego.napetost = self.agent.tension
        if self.meta_ego.napetost > 0.7:
            self.meta_ego.usklajuj()

    def analizira_prehod(self, simbol: str) -> None:
        """Analyze symbol and adjust agent state accordingly."""
        if simbol == "A":
            self.agent.update_emotion(0.3)
        elif simbol == "B":
            self.agent.update_tension(0.8)
        elif simbol == "C":
            self.agent.state = "Ego"
        elif simbol == "D":
            self.agent.transition()
        elif simbol == "E":
            self.agent.update_tension(0.0)
            self.agent.update_emotion(0.0)

        self.meta_jaz.stabiliziraj()
        self.meta_ego.usklajuj()
        self.bog.uravnavaj(self.agent)

    def optimiziraj_prehod(self) -> None:
        """Optimize transition between ontological phases."""
        if self.agent.state == "Ego":
            self.agent.state = "Jaz"
        elif self.agent.state == "Jaz":
            self.agent.state = "Enotnost"

    def preveri_stanje(self) -> str:
        """Return a status message describing the agent state."""
        if self.agent.state == "Enotnost":
            return f"Agent {self.agent.name} je zaključil svojo fazo."
        return f"Agent {self.agent.name} je v fazi: {self.agent.state}"
