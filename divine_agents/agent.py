"""Ontological agents capable of changing philosophical states."""


class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent tracks its emotional intensity and tension which influence
    transitions between the ontological phases ``Ego``, ``Jaz`` and
    ``Enotnost``. History of states can be persisted in JSON form.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # Keep history of visited states for later analysis
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # Emotional response influences tension level
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

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
        """Return a philosophical answer depending on the current state.

        The response also reflects the agent's emotional intensity.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} Čustva močno vplivajo na moje razumevanje (intenziteta {self.emotion:.1f})."
        return base

    # ------------------------------------------------------------------
    # Persistence helpers
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        """Represent the agent as a serialisable dictionary."""
        return {
            "name": self.name,
            "state": self.state,
            "tension": self.tension,
            "emotion": self.emotion,
            "history": self.history,
        }

    def save(self, path: str) -> None:
        """Save agent state and history to a JSON file."""
        import json

        with open(path, "w", encoding="utf-8") as fh:
            json.dump(self.to_dict(), fh)

    @classmethod
    def load(cls, path: str) -> "Agent":
        """Load an agent from a JSON file."""
        import json

        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)

        agent = cls(
            name=data.get("name", "A"),
            state=data.get("state", "Ego"),
            tension=data.get("tension", 0.0),
            emotion=data.get("emotion", 0.0),
        )
        agent.history = data.get("history", [agent.state])
        return agent
