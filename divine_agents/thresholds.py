class SymbolicBox:
    """Symbolic container that functions as a threshold."""
    def __init__(self, stage: str, data: dict = None):
        self.stage = stage
        self.data = data if data else {}
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        """Update the box data."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        """Activate protection to prevent transitions."""
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: dict) -> None:
        """Move to the next threshold stage."""
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        if not self.is_valid_transition(next_stage):
            raise ValueError("Invalid transition")
        self.stage = next_stage
        self.update_data(new_data)

    def get_data(self) -> dict:
        """Retrieve the current state of the box."""
        return self.data

    def is_valid_transition(self, next_stage: str) -> bool:
        """Check if the transition to the next stage is allowed."""
        allowed_transitions = {
            "Ego": ["Jaz"],
            "Jaz": ["Enotnost"],
            "Enotnost": []
        }
        return next_stage in allowed_transitions.get(self.stage, [])

    def __str__(self) -> str:
        return f"Box at stage {self.stage} with data: {self.data}"


class EmotionalBox:
    """Emotional box that functions as a threshold for emotional validation."""
    def __init__(self, emotion: str):
        self.emotion = emotion
        self.status = "unprocessed"

    def process_emotion(self, emotional_agent) -> str:
        """Process the emotional state and confirm it."""
        self.status = emotional_agent.process_emotion(self.emotion)
        return self.status

    def transition_emotion(self, emotional_agent) -> str:
        """Move emotion to the next threshold if it's processed."""
        if self.status == "Emotion confirmed: Negative":
            return "Emotion halted. Task cannot proceed."
        return emotional_agent.process_emotion(self.emotion)
