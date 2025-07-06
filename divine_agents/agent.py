class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Current ontological state (``"Ego"``, ``"Jaz"``, or ``"Enotnost"``).
    tension:
        Current tension level in range ``0`` - ``1``.
    emotion:
        Numerical intensity of the active emotion in range ``0`` - ``1``.
    loyalty:
        Loyalty to the team or beliefs in range ``0`` - ``1``.
    emotional_state:
        Description of current emotion (e.g. ``"happy"``, ``"fearful"``).
    relationships:
        Mapping of agent names to relationship strength.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        loyalty: float = 0.5,
        emotional_state: str = "neutral",
        relationships: dict | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.loyalty = loyalty
        self.emotional_state = emotional_state
        self.relationships = relationships or {}
        self.history: list[str] = [state]
        self.decisions_history: list[str] = []

    def update_emotion(self, state: str, intensity: float) -> None:
        """Update the emotional state and intensity.

        Parameters
        ----------
        state:
            New emotional descriptor (e.g. ``"happy"`` or ``"fearful"``).
        intensity:
            Numeric intensity of the emotion in range ``0`` - ``1``.
        """

        self.emotional_state = state
        self.emotion = intensity
        self.tension += intensity * 0.9
        self.update_tension(self.tension)

    def calculate_relationship_tension(self) -> float:
        """Return extra tension generated from negative relationships."""
        if not self.relationships:
            return 0.0
        return sum(max(0.0, -v) for v in self.relationships.values()) / 10

    def update_tension(self, value: float | None = None) -> None:
        """Update tension considering current emotion and relationships."""
        if value is not None:
            self.tension = value
        self.tension += (self.emotion / 10) * 0.9
        self.tension += self.calculate_relationship_tension()
        self.tension = max(0.0, min(1.0, self.tension))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def make_moral_decision(self, situation: str) -> str:
        """Decide on an action based on emotion and loyalty."""
        if self.emotional_state == "fearful":
            if self.loyalty > 0.7:
                decision = f"{self.name} chooses to help others despite fear due to loyalty."
            else:
                decision = f"{self.name} decides to act selfishly, avoiding risk."
        elif self.emotional_state == "happy":
            if self.loyalty > 0.7:
                decision = f"{self.name} helps others selflessly in {situation}."
            else:
                decision = f"{self.name} focuses on personal gain, despite team needs."
        else:
            decision = f"{self.name} hesitates, torn between loyalty and personal interest."

        self.decisions_history.append(decision)
        return decision

    def collaborative_task(self, team: list["Agent"]) -> str:
        """Simulate a collaborative task with other agents."""
        success_factor = 0.0
        for agent in team:
            success_factor += agent.loyalty
            if agent.emotional_state == "happy":
                success_factor += 1

        if success_factor > len(team):
            return f"{self.name}'s team successfully completes the task due to strong collaboration!"
        return f"{self.name}'s team fails the task due to lack of cohesion."
