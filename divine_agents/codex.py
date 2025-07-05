class Codex:
    """System that verifies commands and handles state transitions with error handling."""

    def __init__(self, initial_state: str):
        self.state = initial_state
        self.history = []
        self.error_log = []
        self.allowed_commands = ['move', 'reset', 'update']

    def validate_command(self, command: str) -> bool:
        """Check if the command is allowed for the current state."""
        return command in self.allowed_commands

    def handle_error(self, message: str) -> str:
        """Record an error and return an error message."""
        self.error_log.append(message)
        return f"Error: {message}"

    def get_next_state(self, command: str) -> str:
        """Determine next state based on the command."""
        if command == 'move':
            return 'moving_state'
        if command == 'reset':
            return 'initial_state'
        if command == 'update':
            return 'updated_state'
        return 'unknown_state'

    def transition(self, command: str) -> str:
        """Attempt a state transition using the given command."""
        if not self.validate_command(command):
            return self.handle_error(f"Invalid Command: {command}")

        new_state = self.get_next_state(command)
        self.history.append((self.state, command, new_state))
        self.state = new_state
        return f"State changed to {new_state}"

    def get_history(self):
        """Return the history of transitions."""
        return self.history

    def get_error_log(self):
        """Return the recorded errors."""
        return self.error_log
