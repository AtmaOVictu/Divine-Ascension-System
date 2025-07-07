class SymbolicBox:
    """Symbolic container functioning as a threshold between ontological states."""

    def __init__(self, stage: str, data: dict | None = None):
        self.stage = stage
        self.data = data or {}
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update internal data if box is not protected."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Set protection flag to block modifications or transitions."""
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: dict | None = None) -> None:
        """Move to the next stage if allowed."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        if not self.is_valid_transition(next_stage):
            raise ValueError(f"Invalid transition from {self.stage} to {next_stage}")
        self.stage = next_stage
        if new_data:
            self.update_data(new_data)

    def is_valid_transition(self, next_stage: str) -> bool:
        """Return True if the transition is allowed."""
        allowed_transitions = {
            "Ego": ["Jaz"],
            "Jaz": ["Enotnost"],
            "Enotnost": [],
        }
        return next_stage in allowed_transitions.get(self.stage, [])

    def __str__(self) -> str:
        return f"Box at stage {self.stage} with data: {self.data}"


class EmotionalBox:
    """Holds an emotion value and processes it via an emotional agent."""

    def __init__(self, emotion: str):
        self.emotion = emotion
        self.status = "unprocessed"

    def process_emotion(self, agent: "EmotionalAgent") -> str:
        """Process emotion with the given agent and store the status."""
        self.status = agent.process_emotion(self.emotion)
        return self.status

    def transition_emotion(self, agent: "EmotionalAgent") -> str:
        """Attempt to re-process the emotion to allow continuation."""
        if self.status == "Emotion confirmed: Negative":
            return "Emotion halted. Task cannot proceed."
        return agent.process_emotion(self.emotion)
