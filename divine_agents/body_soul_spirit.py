"""Ontological agents for Body, Soul, and Spirit phases.

Each agent manages transitions between states based on symbolic commands.
"""

from __future__ import annotations


class BodyAgent:
    """Agent representing physical experience."""

    def __init__(self) -> None:
        self.state = "Material"

    def transition(self, symbol: str) -> None:
        """Transition the body through its phases."""
        if symbol == "Material":
            self.state = "Material"
            print("Telo: Material - Zunanji svet, materialnost, fizične omejitve.")
        elif symbol == "Sensation":
            self.state = "Sensation"
            print("Telo: Sensation - Zaznavanje, občutki, fizična čutnost.")
        elif symbol == "Action":
            self.state = "Action"
            print("Telo: Action - Aktivacija in izvajanje dejanj, odziv na okolje.")
        elif symbol in {"ADD", "DODAJ"}:
            self.state = "Expansion"
            print(
                "Telo: Expansion - Dodajanje novih čutnih sposobnosti, širjenje fizičnih zmožnosti."
            )
        else:
            print("Neznan simbol za telo.")

    def get_state(self) -> str:
        return self.state


class SoulAgent:
    """Agent representing internal experience."""

    def __init__(self) -> None:
        self.state = "Awareness"

    def transition(self, symbol: str) -> None:
        """Transition the soul through its phases."""
        if symbol == "Awareness":
            self.state = "Awareness"
            print("Duša: Awareness - Samozavedanje, refleksija o lastnem obstoju.")
        elif symbol == "Emotion":
            self.state = "Emotion"
            print(
                "Duša: Emotion - Čustvena doživetja, reakcije na zunanje in notranje dražljaje."
            )
        elif symbol == "Reflection":
            self.state = "Reflection"
            print(
                "Duša: Reflection - Razmišljanje, analiza, iskanje smiselnosti v izkušnjah."
            )
        elif symbol == "Growth":
            self.state = "Growth"
            print(
                "Duša: Growth - Razvoj znotraj emocionalnih in intelektualnih okvirov."
            )
        elif symbol in {"ADD", "DODAJ"}:
            self.state = "Enlightenment"
            print(
                "Duša: Enlightenment - Osvetljenost, širjenje zavedanja do višjih ravni."
            )
        else:
            print("Neznan simbol za dušo.")

    def get_state(self) -> str:
        return self.state


class SpiritAgent:
    """Agent representing transcendental experience."""

    def __init__(self) -> None:
        self.state = "Divine"

    def transition(self, symbol: str) -> None:
        """Transition the spirit through its phases."""
        if symbol == "Divine":
            self.state = "Divine"
            print("Duh: Divine - Povezava z božanskim, večnost, transcendenca.")
        elif symbol == "Unity":
            self.state = "Unity"
            print("Duh: Unity - Enotnost, povezovanje vseh nasprotij v harmonično celoto.")
        elif symbol == "Eternal":
            self.state = "Eternal"
            print("Duh: Eternal - Nespremenljivost, večno bivanje in razumevanje.")
        elif symbol == "Enlightenment":
            self.state = "Enlightenment"
            print("Duh: Enlightenment - Osvetljenost, popolno razumevanje resničnosti.")
        elif symbol in {"ADD", "DODAJ"}:
            self.state = "Transcendence"
            print(
                "Duh: Transcendence - Premik preko vseh omejitev, dosego popolne enotnosti z vesoljem."
            )
        else:
            print("Neznan simbol za duh.")

    def get_state(self) -> str:
        return self.state

