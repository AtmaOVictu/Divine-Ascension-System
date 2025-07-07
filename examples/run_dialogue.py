from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

if __name__ == "__main__":
    a1 = Agent("Agent1")
    a2 = Agent("Agent2", state="Jaz")
    for line in philosophical_dialogue(a1, a2):
        print(line)
