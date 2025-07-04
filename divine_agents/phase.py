class RESPhase:
    """Represents a single RES phase with basic transition logic."""

    def __init__(self, label: str, emotion: str = "Neutral", tension: float = 0.5,
                 purpose: str = "Initial Purpose", gift: str = "") -> None:
        self.label = label
        self.emotion = emotion
        self.tension = tension
        self.purpose = purpose
        self.gift = gift

    def transition(self) -> bool:
        """Return True and update emotion/purpose if transition criteria met."""
        if self.tension >= 0.7:
            self.emotion = "Transformed Emotion"
            self.purpose = "New Purpose"
            return True
        return False

    def modify(self, new_emotion: str | None = None, new_tension: float | None = None,
               new_purpose: str | None = None, new_gift: str | None = None) -> None:
        """Modify phase attributes."""
        if new_emotion is not None:
            self.emotion = new_emotion
        if new_tension is not None:
            self.tension = new_tension
        if new_purpose is not None:
            self.purpose = new_purpose
        if new_gift is not None:
            self.gift = new_gift


def generate_phases() -> list[RESPhase]:
    """Create phases RES000 to RES100 inclusive."""
    phases: list[RESPhase] = []
    for i in range(101):
        if i == 0:
            label = "RES000"
        elif i < 10:
            label = f"RES00{i}"
        elif i < 100:
            label = f"RES0{i}"
        else:
            label = f"RES{i}"

        phases.append(RESPhase(label))
    return phases
