class SymbolicBox:
    """Symbolic container functioning as a threshold between stages."""
    def __init__(self, stage: str, data: dict = None):
        self.stage = stage
        self.data = data or {}
        self.protection_flag = False

    def update_data(self, new_data: dict):
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.data.update(new_data)

    def set_protection(self, flag: bool):
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: dict):
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        if not self.is_valid_transition(next_stage):
            raise ValueError("Invalid transition.")
        self.stage = next_stage
        self.update_data(new_data)

    def get_data(self):
        return self.data

    def is_valid_transition(self, next_stage: str):
        allowed_transitions = {"∴": ["∆"], "∆": ["⊘"], "⊘": []}
        return next_stage in allowed_transitions.get(self.stage, [])

    def __str__(self):
        return f"Box at stage {self.stage} with data: {self.data}"


class EmotionalBox:
    """Emotional box functioning as a threshold for emotional validation."""
    def __init__(self, emotion: str):
        self.emotion = emotion
        self.status = "unprocessed"

    def process_emotion(self, emotional_agent):
        self.status = emotional_agent.process_emotion(self.emotion)
        return self.status

    def transition_emotion(self, emotional_agent):
        if self.status == "Emotion confirmed: Negative":
            return "Emotion halted. Task cannot proceed."
        return emotional_agent.process_emotion(self.emotion)
