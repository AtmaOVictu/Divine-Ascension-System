class RESOperations:
    """Manage RES operations with binary values."""
    def __init__(self):
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
        return self.operations.get(res_id, 'Napaka: Neznana operacija')

    def add_operation(self, res_id: str, binary_value: str) -> None:
        if res_id in self.operations:
            print(f"Operacija {res_id} že obstaja. Posodobitev ni izvedena.")
        else:
            self.operations[res_id] = binary_value
            print(f"Operacija {res_id} je bila dodana z vrednostjo {binary_value}.")

    def update_operation(self, res_id: str, new_binary_value: str) -> None:
        if res_id in self.operations:
            self.operations[res_id] = new_binary_value
            print(f"Operacija {res_id} je bila posodobljena na novo vrednost {new_binary_value}.")
        else:
            print(f"Napaka: Operacija {res_id} ne obstaja. Posodobitev ni izvedena.")

    def execute_operation(self, res_id: str) -> str:
        binary_value = self.get_binary_value(res_id)
        if binary_value == 'Napaka: Neznana operacija':
            print(binary_value)
            return ''
        if binary_value == '00000000':
            return f"Operacija {res_id} je v začetnem stanju (RES000)."
        if binary_value == '00000001':
            return f"Operacija {res_id} prehaja v novo stanje (RES001)."
        return f"Operacija {res_id} je izvedena z vrednostjo {binary_value}."

    def delete_operation(self, res_id: str) -> None:
        if res_id in self.operations:
            del self.operations[res_id]
            print(f"Operacija {res_id} je bila uspešno odstranjena.")
        else:
            print(f"Napaka: Operacija {res_id} ne obstaja, zato ni bila odstranjena.")
