"""Simple command-line interface to manage agents and run dialogues."""

from typing import Dict
from .agent import Agent
from .dialogue import philosophical_dialogue


def create_agent(name: str, state: str = "Ego") -> Agent:
    return Agent(name, state=state)


def list_agents(agents: Dict[str, Agent]) -> None:
    for a in agents.values():
        print(f"{a.name}: state={a.state}, tension={a.tension:.2f}, emotion={a.emotion:.2f}")


def run_dialogue(agents: Dict[str, Agent], a1: str, a2: str) -> None:
    lines = philosophical_dialogue(agents[a1], agents[a2])
    for line in lines:
        print(line)


def main() -> None:
    agents: Dict[str, Agent] = {}
    while True:
        command = input("(list/add/dialogue/quit) > ").strip()
        if command == "list":
            list_agents(agents)
        elif command == "add":
            name = input("Name: ")
            agents[name] = create_agent(name)
        elif command == "dialogue":
            a1 = input("Agent1: ")
            a2 = input("Agent2: ")
            if a1 in agents and a2 in agents:
                run_dialogue(agents, a1, a2)
            else:
                print("Unknown agents")
        elif command == "quit":
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
