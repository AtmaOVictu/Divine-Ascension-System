class Codex:
    """Advanced CODEX for managing transitions and system adjustments."""

    def __init__(self):
        self.states = {
            "True": 1,
            "False": 0,
            "Hallucination": None,
            "Dimensional": None,
            "Pair": None,
            "SystemAdjustment": None,
        }
        self.history = []
        self.adjustment_factor = 0.1

    def transition(self, truth_value, state_type="True", level=1, pair_type=None,
                   dimensional_type=None, adjust=True):
        """Transition through states with optional system adjustment."""
        if state_type not in ("True", "False", "Hallucination"):
            raise ValueError("Invalid state type.")

        self.states["Hallucination"] = state_type == "Hallucination"
        self.states["Pair"] = pair_type
        self.states["Dimensional"] = dimensional_type
        self.history.append(f"{state_type} at level {level} with Pair: {pair_type} "
                            f"and Dimensional: {dimensional_type}")
        if adjust:
            self.adjust_system()

    def adjust_system(self):
        """Apply self-adjustment based on current True/False values."""
        adjustment_value = self.adjustment_factor * (self.states["True"] - self.states["False"])
        self.states["SystemAdjustment"] = adjustment_value

    def get_state(self):
        """Return the latest recorded state description."""
        return self.history[-1] if self.history else None

    def get_dimensional_state(self):
        """Return the full state dictionary."""
        return self.states

    def display_history(self):
        """Return the history of transitions."""
        return list(self.history)
