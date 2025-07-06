from .agent import Agent
from .dialogue import philosophical_dialogue


def main():
    agent1 = Agent("Agent 1")
    agent2 = Agent("Agent 2", state="Jaz")
    for line in philosophical_dialogue(agent1, agent2):
        print(line)


if __name__ == "__main__":
    main()
