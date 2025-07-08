class Memory:
    """Simple memory storage for agents."""
    def __init__(self):
        self.short_term = []
        self.long_term = []

    def store_short_term(self, data):
        self.short_term.append(data)

    def store_long_term(self, data):
        self.long_term.append(data)

def parse_philosophical_statement(statement: str, memory: 'Memory') -> str:
    """Parse a philosophical statement and store it in short-term memory."""
    parsed = statement.strip()
    memory.store_short_term(parsed)
    return parsed
