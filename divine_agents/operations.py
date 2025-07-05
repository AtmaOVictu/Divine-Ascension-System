# Mapping of RES operations to binary values
RES_OPERATIONS = {
    'RES000': '00000000',
    'RES001': '00000001',
    'RES010': '00000010',
    'RES011': '00000011',
    'RES100': '00000100',
    'RES101': '00000101',
    'RES110': '00000110',
    'RES111': '00000111',
}

def get_binary_value(res_id: str) -> str:
    """Return the binary value for a given RES operation."""
    return RES_OPERATIONS.get(res_id, 'Neznana operacija')
