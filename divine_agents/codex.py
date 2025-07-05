class Codex:
    """Codex manages state transitions based on incoming commands."""

    def __init__(self, initial_state: str = "initial_state"):
        self.state = initial_state
        self.history = []  # record of (old_state, command, new_state)
        self.error_log = []
        self.allowed_commands = {"move", "reset", "update"}

    def validate_command(self, command: str) -> bool:
        """Return True if the command is permitted."""
        return command in self.allowed_commands

    def handle_error(self, message: str) -> str:
        """Record an error and return the formatted message."""
        self.error_log.append(message)
        return f"Error: {message}"

    def get_next_state(self, command: str) -> str:
        """Determine the next state based on the command."""
        if command == "move":
            return "moving_state"
        if command == "reset":
            return "initial_state"
        if command == "update":
            return "updated_state"
        return "unknown_state"

    def transition(self, command: str) -> str:
        """Attempt a state transition using the command."""
        if not self.validate_command(command):
            return self.handle_error(f"Invalid Command: {command}")

        new_state = self.get_next_state(command)
        self.history.append((self.state, command, new_state))
        self.state = new_state
        return f"State changed to {new_state}"

    def get_history(self):
        return self.history

    def get_error_log(self):
        return self.error_log
