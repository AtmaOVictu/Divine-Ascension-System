class Agent:
    """Represents an ontological agent capable of transitioning states and fame boxes."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.fame = 0.0
        self.participation = 0.0
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

    # Fame and participation box utilities
    def get_fame_box(self) -> str:
        """Return the fame box corresponding to current fame."""
        if self.fame <= 0.2:
            return "Unknown Fame Box"
        if self.fame <= 0.5:
            return "Moderate Fame Box"
        if self.fame <= 0.8:
            return "Influential Fame Box"
        return "Legendary Fame Box"

    def get_emotional_box(self) -> str:
        """Return the emotional box derived from fame."""
        if self.fame >= 0.8:
            return "Arrogant Box"
        if self.fame >= 0.5:
            return "Balanced Box"
        if self.fame >= 0.2:
            return "Insecure Box"
        return "Frustrated Box"

    def get_participation_box(self) -> str:
        """Return the participation box based on participation."""
        if self.participation >= 0.8:
            return "Highly Active Box"
        if self.participation >= 0.5:
            return "Moderate Activity Box"
        return "Passive Participation Box"

    def update_fame(self, positive_actions: float, negative_actions: float, participation_score: float) -> float:
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
        self.fame = min(1.0, max(0.0, self.fame))
        self.apply_fame_decay()

        self.boxes["fame"] = self.get_fame_box()
        self.boxes["emotional_state"] = self.get_emotional_box()
        self.boxes["participation"] = self.get_participation_box()

        self.clusters["social_cluster"] = [self.boxes["fame"], self.boxes["emotional_state"]]
        self.clusters["activity_cluster"] = [self.boxes["participation"]]

        return self.fame

    def apply_fame_decay(self) -> None:
        """Reduce fame over time."""
        if self.fame > 0.0:
            self.fame -= self.fame * self.decay_rate
            self.fame = max(0.0, self.fame)

    def update_participation(self, new_participation_score: float) -> None:
        """Set new participation score and update boxes."""
        self.participation = min(1.0, max(0.0, new_participation_score))
        self.boxes["participation"] = self.get_participation_box()
        self.clusters["activity_cluster"] = [self.boxes["participation"]]

    def get_cluster_boxes(self, cluster_name: str):
        """Return boxes belonging to a cluster."""
        return self.clusters.get(cluster_name, [])

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.boxes["emotional_state"] = self.get_emotional_box()
        self.clusters["social_cluster"] = [self.boxes["fame"], self.boxes["emotional_state"]]
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            reply = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            reply = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            reply = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            reply += " Čutim intenzivna čustva."
        return reply
