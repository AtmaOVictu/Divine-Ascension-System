"""Container classes enforcing modular responsibilities."""
from .modules import AwarenessModule, OppositionModule, TransitionModule


class AwarenessContainer:
    """Container managing awareness module."""

    def __init__(self) -> None:
        self.awareness_module = AwarenessModule("AwarenessModule")

    def run(self) -> str:
        self.awareness_module.activate()
        return self.awareness_module.state


class OppositionContainer:
    """Container managing opposition module."""

    def __init__(self) -> None:
        self.opposition_module = OppositionModule("OppositionModule")

    def run(self) -> str:
        self.opposition_module.toggle_opposition()
        return self.opposition_module.state


class TransitionContainer:
    """Container orchestrating transitions between awareness and opposition."""

    def __init__(self, awareness: AwarenessContainer, opposition: OppositionContainer) -> None:
        self.transition_module = TransitionModule(awareness.awareness_module, opposition.opposition_module)

    def run(self) -> None:
        self.transition_module.process()
