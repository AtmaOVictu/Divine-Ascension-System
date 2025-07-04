class Codex:
    """Advanced CODEX managing transitions, dimensional doks, and adjustments."""

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
        self.dimensions = []

    def transition(
        self,
        truth_value,
        state_type="True",
        level=1,
        pair_type=None,
        dimensional_type=None,
        adjust=True,
    ):
        """Transition through states with optional adjustments."""

        if state_type == "True":
            self.history.append(
                f"True at level {level} with Pair: {pair_type} and Dimensional: {dimensional_type}"
            )
            self.states["True"] = truth_value
            self.states["Hallucination"] = False
        elif state_type == "False":
            self.history.append(
                f"False at level {level} with Pair: {pair_type} and Dimensional: {dimensional_type}"
            )
            self.states["False"] = truth_value
            self.states["Hallucination"] = True
        elif state_type == "Hallucination":
            self.history.append(
                f"Hallucination at level {level} with Pair: {pair_type} and Dimensional: {dimensional_type}"
            )
            self.states["Hallucination"] = True
        else:
            raise ValueError("Invalid state type.")

        self.states["Pair"] = pair_type
        self.states["Dimensional"] = dimensional_type
        if dimensional_type:
            self.dimensions.append(dimensional_type)
        if adjust:
            self.adjust_system()

        return self.states

    def adjust_system(self):
        """Adjust system tension based on current truth and illusion."""
        adjustment_value = self.adjustment_factor * (self.states["True"] - self.states["False"])
        self.states["SystemAdjustment"] = adjustment_value

    def get_state(self):
        """Return the last recorded state description."""
        return self.history[-1] if self.history else None

    def get_dimensional_state(self):
        """Return current state dictionary."""
        return self.states

    def display_history(self):
        """Return history of transitions."""
        return self.history
