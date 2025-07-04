from dataclasses import dataclass
from typing import List


@dataclass
class RESPhase:
    """Representation of a RES phase."""

    label: str
    emotion: str = "Neutral"
    tension: float = 0.5
    purpose: str = "Initial Purpose"
    gift: str = ""

    def transition_ready(self) -> bool:
        """Return True if the phase can transition to the next."""
        return self.tension >= 0.7

    def transition(self) -> bool:
        """Perform a phase transition if tension threshold is met."""
        if self.transition_ready():
            self.emotion = "Transformed Emotion"
            self.purpose = "New Purpose"
            return True
        return False

    def modify(
        self,
        new_emotion: str | None = None,
        new_tension: float | None = None,
        new_purpose: str | None = None,
        new_gift: str | None = None,
    ) -> None:
        """Modify phase attributes."""
        if new_emotion is not None:
            self.emotion = new_emotion
        if new_tension is not None:
            self.tension = new_tension
        if new_purpose is not None:
            self.purpose = new_purpose
        if new_gift is not None:
            self.gift = new_gift


def create_phases() -> List[RESPhase]:
    """Generate phases RES000 through RES100."""
    phases: List[RESPhase] = []
    for i in range(101):
        if i == 0:
            label = "RES000"
        elif i < 10:
            label = f"RES00{i}"
        elif i < 100:
            label = f"RES0{i}"
        else:
            label = f"RES{i}"
        phases.append(RESPhase(label=label))
    return phases
