class Agent:
    """Ontological agent capable of state and fame transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        fame: float = 0.0,
        participation: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.fame = fame
        self.participation = participation
        self.decay_rate = 0.05
        self.history = [state]

        self.boxes = {
            "fame": self.get_fame_box(),
            "emotional_state": self.get_emotional_box(),
            "participation": self.get_participation_box(),
        }

        self.clusters = {
            "social_cluster": [self.boxes["fame"], self.boxes["emotional_state"]],
            "activity_cluster": [self.boxes["participation"]],
        }

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    # Fame, emotional state and participation box helpers ------------------

    def get_fame_box(self) -> str:
        """Return the current fame box based on fame percentage."""
        if self.fame <= 0.2:
            return "Unknown Fame Box"
        if self.fame <= 0.5:
            return "Moderate Fame Box"
        if self.fame <= 0.8:
            return "Influential Fame Box"
        return "Legendary Fame Box"

    def get_emotional_box(self) -> str:
        """Return the current emotional state box based on fame."""
        if self.fame >= 0.8:
            return "Arrogant Box"
        if self.fame >= 0.5:
            return "Balanced Box"
        if self.fame >= 0.2:
            return "Insecure Box"
        return "Frustrated Box"

    def get_participation_box(self) -> str:
        """Return the participation state box."""
        if self.participation >= 0.8:
            return "Highly Active Box"
        if self.participation >= 0.5:
            return "Moderate Activity Box"
        return "Passive Participation Box"

    # Fame and participation updates --------------------------------------

    def update_fame(
        self, positive_actions: float, negative_actions: float, participation_score: float
    ) -> float:
        """Update fame based on actions and participation."""
        positive_weight = 0.1
        negative_weight = 0.05
        participation_weight = 0.1

        fame_change = (
            positive_actions * positive_weight
            - negative_actions * negative_weight
            + participation_score * participation_weight
        )
        self.fame += fame_change
        self.fame = max(0.0, min(1.0, self.fame))
        self.apply_fame_decay()

        self.boxes["fame"] = self.get_fame_box()
        self.boxes["emotional_state"] = self.get_emotional_box()
        self.boxes["participation"] = self.get_participation_box()

        self.clusters["social_cluster"] = [self.boxes["fame"], self.boxes["emotional_state"]]
        self.clusters["activity_cluster"] = [self.boxes["participation"]]

        return self.fame

    def apply_fame_decay(self) -> None:
        """Decay fame by a percentage over time."""
        if self.fame > 0.0:
            self.fame -= self.fame * self.decay_rate
            self.fame = max(0.0, self.fame)

    def update_participation(self, new_participation_score: float) -> None:
        """Update the agent's algorithmic participation."""
        self.participation = max(0.0, min(1.0, new_participation_score))
        self.boxes["participation"] = self.get_participation_box()
        self.clusters["activity_cluster"] = [self.boxes["participation"]]

    def get_cluster_boxes(self, cluster_name: str):
        """Return all boxes in a specific cluster."""
        return self.clusters.get(cluster_name, [])
