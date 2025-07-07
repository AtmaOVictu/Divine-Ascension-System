class SymbolicBox:
    """Symbolic container that functions as a threshold."""

    def __init__(self, stage: str, data: dict | None = None):
        self.stage = stage
        self.data = data if data is not None else {}
        self.protection_flag = False

    def update_data(self, new_data: dict) -> None:
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot modify data.")
        self.data.update(new_data)

    def set_protection(self, flag: bool) -> None:
        self.protection_flag = flag

    def transition(self, next_stage: str, new_data: dict) -> None:
        if self.protection_flag:
            raise PermissionError("Box is protected. Cannot transition.")
        if not self.is_valid_transition(next_stage):
            raise ValueError("Invalid transition")
        self.stage = next_stage
        self.update_data(new_data)

    def get_data(self) -> dict:
        return self.data

    def is_valid_transition(self, next_stage: str) -> bool:
        allowed_transitions = {
            "∴": ["∆"],
            "∆": ["⊘"],
            "⊘": [],
        }
        return next_stage in allowed_transitions.get(self.stage, [])

    def __str__(self) -> str:
        return f"Box at stage {self.stage} with data: {self.data}"


from .agent import Agent


class EmotionalAgent(Agent):
    """Agent specialized in processing emotions."""

    def __init__(self, name: str = "Emotional Agent", state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name=name, state=state, tension=tension, emotion=emotion)

    def process_emotion(self, emotion: str) -> str:
        if emotion in ["anger", "frustration", "fear"]:
            return "Emotion confirmed: Negative"
        if emotion in ["happiness", "joy"]:
            return "Emotion confirmed: Positive"
        return "Emotion confirmed: Neutral"


class EmotionalBox:
    """Emotional box functioning as a threshold for emotional validation."""

    def __init__(self, emotion: str):
        self.emotion = emotion
        self.status = "unprocessed"

    def process_emotion(self, emotional_agent: EmotionalAgent) -> str:
        self.status = emotional_agent.process_emotion(self.emotion)
        return self.status

    def transition_emotion(self, emotional_agent: EmotionalAgent) -> str:
        if self.status == "Emotion confirmed: Negative":
            return "Emotion halted. Task cannot proceed."
        return emotional_agent.process_emotion(self.emotion)
