"""Additional agents providing simulation and speculation capabilities."""

from __future__ import annotations

import random
import string
from typing import List


class ExtrapolatingAgent:
    """Agent that encodes text by shifting characters forward."""

    def __init__(self, shift: int) -> None:
        self.shift = shift
        self.history: List[str] = []

    def encode(self, data: str) -> str:
        result = []
        for char in data:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - base + self.shift) % 26 + base))
            else:
                result.append(char)
        encoded = ''.join(result)
        self.history.append(encoded)
        return encoded

    def extrapolate(self) -> str:
        if len(self.history) > 1:
            last = self.history[-1]
            return ''.join(chr(ord(c) + self.shift) for c in last)
        return "Ni dovolj podatkov za extrapolacijo"

    def self_adjust(self, feedback: str) -> str:
        if "povečaj" in feedback:
            self.shift += 1
        elif "zmanjšaj" in feedback:
            self.shift -= 1
        return f"Novo stanje shift: {self.shift}"


class IntrospectiveAgent:
    """Agent that encodes text by shifting characters backward."""

    def __init__(self, shift: int) -> None:
        self.shift = shift
        self.history: List[str] = []

    def encode(self, data: str) -> str:
        result = []
        for char in data:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - base - self.shift) % 26 + base))
            else:
                result.append(char)
        encoded = ''.join(result)
        self.history.append(encoded)
        return encoded

    def introspect(self) -> str:
        if len(self.history) > 1:
            last = self.history[-1]
            return ''.join(chr(ord(c) - self.shift) for c in last)
        return "Ni dovolj podatkov za introspekcijo"

    def self_adjust(self, feedback: str) -> str:
        if "povečaj" in feedback:
            self.shift += 1
        elif "zmanjšaj" in feedback:
            self.shift -= 1
        return f"Novo stanje shift: {self.shift}"


class SubstitutionAgent:
    """Agent that randomly substitutes letters."""

    def __init__(self) -> None:
        self.alphabet = string.ascii_lowercase

    def encode(self, data: str) -> str:
        result = []
        for char in data:
            if char.isalpha():
                new_char = random.choice(self.alphabet)
                result.append(new_char.upper() if char.isupper() else new_char)
            else:
                result.append(char)
        return ''.join(result)


class Simulation:
    """Create deterministic variations of the provided text."""

    def __init__(self) -> None:
        self.scenarios: List[str] = []

    def simulate_future(self, current_state: str) -> str:
        result = []
        for char in current_state:
            if char.isalpha():
                result.append(chr(ord(char) + random.randint(1, 3)))
            else:
                result.append(char)
        future = ''.join(result)
        self.scenarios.append(future)
        return future

    def generate_multiple_scenarios(self, current_state: str, num_scenarios: int = 5) -> List[str]:
        return [self.simulate_future(current_state) for _ in range(num_scenarios)]


class SpeculativeAgent:
    """Generate uncertain variations of the provided text."""

    def __init__(self) -> None:
        self.possibilities: List[str] = []

    def speculate(self, current_state: str) -> str:
        result = []
        for char in current_state:
            if char.isalpha():
                result.append(chr(ord(char) + random.randint(-5, 5)))
            else:
                result.append(char)
        future = ''.join(result)
        self.possibilities.append(future)
        return future
