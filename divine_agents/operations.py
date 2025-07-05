class RESOperations:
    """Manage RES operations and binary values."""

    def __init__(self) -> None:
        self.operations = {
            'RES000': '00000000',
            'RES001': '00000001',
            'RES010': '00000010',
            'RES011': '00000011',
            'RES100': '00000100',
            'RES101': '00000101',
            'RES110': '00000110',
            'RES111': '00000111',
        }

    def get_binary_value(self, res_id: str) -> str:
        """Return binary value for given operation or error message."""
        return self.operations.get(res_id, 'Napaka: Neznana operacija')

    def add_operation(self, res_id: str, binary_value: str) -> None:
        """Add new operation if not already present."""
        if res_id in self.operations:
            raise ValueError(f"Operacija {res_id} že obstaja.")
        self.operations[res_id] = binary_value

    def update_operation(self, res_id: str, new_binary_value: str) -> None:
        """Update existing operation's binary value."""
        if res_id not in self.operations:
            raise KeyError(f"Operacija {res_id} ne obstaja.")
        self.operations[res_id] = new_binary_value

    def execute_operation(self, res_id: str) -> str:
        """Execute operation based on binary value."""
        binary_value = self.get_binary_value(res_id)
        if binary_value == 'Napaka: Neznana operacija':
            return binary_value
        if binary_value == '00000000':
            return f"Operacija {res_id} je v začetnem stanju (RES000)."
        if binary_value == '00000001':
            return f"Operacija {res_id} prehaja v novo stanje (RES001)."
        return f"Operacija {res_id} je izvedena z vrednostjo {binary_value}."

    def delete_operation(self, res_id: str) -> None:
        """Delete existing operation if present."""
        if res_id not in self.operations:
            raise KeyError(f"Operacija {res_id} ne obstaja.")
        del self.operations[res_id]

