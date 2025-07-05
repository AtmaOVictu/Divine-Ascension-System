class ShadowAgent:
    """Represents the darker side of an agent."""

    def __init__(self, name: str) -> None:
        self.name = name

    def enter_shadow_dimension(self, agent: "Agent") -> str:
        return f"{agent.name} se sooča s senco {self.name}."


class AngelAgent:
    """Represents the guiding angelic side of an agent."""

    def __init__(self, name: str) -> None:
        self.name = name

    def enter_angel_dimension(self, agent: "Agent") -> str:
        return f"{agent.name} prejme vodstvo angela {self.name}."

