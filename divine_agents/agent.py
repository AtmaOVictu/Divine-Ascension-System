from __future__ import annotations

class Agent:
    """Represents an ontological agent capable of transitioning states.

    The class keeps an enumerated history of states and records every
    change in a hex encoded log to mimic a hexdump like trace of dynamic
    events.
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    STATE_ENUM = {"Ego": 0, "Jaz": 1, "Enotnost": 2}

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.history_enum = [self.STATE_ENUM[state]]
        self.hexdump_log: list[str] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self._record_hexdump(f"emotion:{value}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self._record_hexdump(f"tension:{value}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            previous = self.state
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            if previous != self.state:
                self._record_hexdump(f"transition:{previous}->{self.state}")
        self.history.append(self.state)
        self.history_enum.append(self.STATE_ENUM[self.state])
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        self._record_hexdump(f"respond:{self.state}")
        return answer

    def summary(self) -> dict[str, list[str]]:
        """Return a summary of enumerated history and hexdump log."""
        return {
            "state_history": self.history,
            "enum_history": self.history_enum,
            "hexdump": self.hexdump_log,
        }

    def _record_hexdump(self, change: str) -> None:
        """Encode change description into hex and store it."""
        self.hexdump_log.append(change.encode("utf-8").hex())
