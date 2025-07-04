class MemorySystem:
    """Stores historical states and transitions for an agent."""

    def __init__(self):
        self.history = []
        self.current_state = None
        self.transition_points = []

    def update(self, new_state, transition_type="linear"):
        if self.current_state is not None:
            self.history.append(self.current_state)
        self.current_state = new_state
        self.transition_points.append(transition_type)

    def revert_to_previous(self):
        if self.history:
            self.current_state = self.history.pop()
            self.transition_points.pop()
        else:
            print("Ni prejšnje verzije za vračanje.")

    def get_current_state(self):
        return self.current_state

    def get_all_history(self):
        return list(self.history)

    def get_all_transitions(self):
        return list(self.transition_points)

    def optimize_transitions(self):
        optimized = []
        for i, transition in enumerate(self.transition_points):
            if transition == "linear" and i > 0 and self.transition_points[i - 1] != "linear":
                optimized.append("optimized_linear")
            else:
                optimized.append(transition)
        self.transition_points = optimized

