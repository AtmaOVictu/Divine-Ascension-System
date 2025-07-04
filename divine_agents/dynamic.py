"""Additional dynamic agents and utilities for simulations and speculations."""

from __future__ import annotations

import random
import string
from typing import List


class ExtrapolatingAgent:
    """Agent that predicts future changes using a Caesar-style shift."""

    def __init__(self, shift: int):
        self.shift = shift
        self.history: List[str] = []

    def encode(self, data: str) -> str:
        encoded = []
        for ch in data:
            if ch.isalpha():
                base = 65 if ch.isupper() else 97
                encoded.append(chr((ord(ch) - base + self.shift) % 26 + base))
            else:
                encoded.append(ch)
        result = "".join(encoded)
        self.history.append(result)
        return result

    def extrapolate(self) -> str:
        if len(self.history) > 1:
            last = self.history[-1]
            return "".join(chr(ord(c) + self.shift) for c in last)
        return "Ni dovolj podatkov za extrapolacijo"

    def self_adjust(self, feedback: str) -> str:
        if "povečaj" in feedback:
            self.shift += 1
        elif "zmanjšaj" in feedback:
            self.shift -= 1
        return f"Novo stanje shift: {self.shift}"


class IntrospectiveAgent:
    """Agent that analyzes internal states with a reverse Caesar shift."""

    def __init__(self, shift: int):
        self.shift = shift
        self.history: List[str] = []

    def encode(self, data: str) -> str:
        encoded = []
        for ch in data:
            if ch.isalpha():
                base = 65 if ch.isupper() else 97
                encoded.append(chr((ord(ch) - base - self.shift) % 26 + base))
            else:
                encoded.append(ch)
        result = "".join(encoded)
        self.history.append(result)
        return result

    def introspect(self) -> str:
        if len(self.history) > 1:
            last = self.history[-1]
            return "".join(chr(ord(c) - self.shift) for c in last)
        return "Ni dovolj podatkov za introspekcijo"

    def self_adjust(self, feedback: str) -> str:
        if "povečaj" in feedback:
            self.shift += 1
        elif "zmanjšaj" in feedback:
            self.shift -= 1
        return f"Novo stanje shift: {self.shift}"


class SubstitutionAgent:
    """Agent that encodes text using random substitution."""

    def __init__(self) -> None:
        self.alphabet = string.ascii_lowercase

    def encode(self, data: str) -> str:
        encoded = []
        for ch in data:
            if ch.isalpha():
                new = random.choice(self.alphabet)
                encoded.append(new.upper() if ch.isupper() else new)
            else:
                encoded.append(ch)
        return "".join(encoded)


class Simulation:
    """Create deterministic but random-like future scenarios."""

    def __init__(self) -> None:
        self.scenarios: List[str] = []

    def simulate_future(self, current_state: str) -> str:
        future = []
        for ch in current_state:
            if ch.isalpha():
                future.append(chr(ord(ch) + random.randint(1, 3)))
            else:
                future.append(ch)
        result = "".join(future)
        self.scenarios.append(result)
        return result

    def generate_multiple_scenarios(self, current_state: str, num: int = 5) -> List[str]:
        return [self.simulate_future(current_state) for _ in range(num)]


class SpeculativeAgent:
    """Agent that imagines highly uncertain future states."""

    def __init__(self) -> None:
        self.possibilities: List[str] = []

    def speculate(self, current_state: str) -> str:
        out = []
        for ch in current_state:
            if ch.isalpha():
                out.append(chr(ord(ch) + random.randint(-5, 5)))
            else:
                out.append(ch)
        result = "".join(out)
        self.possibilities.append(result)
        return result


class CodingSystem:
    """System orchestrating multiple agents and speculative utilities."""

    def __init__(self, shift: int):
        self.extrapolation_agent = ExtrapolatingAgent(shift)
        self.introspection_agent = IntrospectiveAgent(shift)
        self.substitution_agent = SubstitutionAgent()
        self.simulation = Simulation()
        self.speculative_agent = SpeculativeAgent()

    def process_data(self, data: str) -> List[str]:
        lines = []
        lines.append(f"Originalna besedila: {data}")

        extrapolated = self.extrapolation_agent.encode(data)
        lines.append(f"Extrapolirana besedila: {extrapolated}")

        introspected = self.introspection_agent.encode(data)
        lines.append(f"Introspektivna besedila: {introspected}")

        substituted = self.substitution_agent.encode(data)
        lines.append(f"Substitucijska šifra: {substituted}")

        feedback = "povečaj"
        lines.append(self.extrapolation_agent.self_adjust(feedback))
        lines.append(self.introspection_agent.self_adjust(feedback))

        simulated_future = self.simulation.simulate_future(data)
        lines.append(f"Simulacija prihodnosti: {simulated_future}")

        scenarios = self.simulation.generate_multiple_scenarios(data, num=3)
        lines.append(f"Generirani scenariji: {scenarios}")

        speculative_future = self.speculative_agent.speculate(data)
        lines.append(f"Špekulacija prihodnosti: {speculative_future}")
        return lines
