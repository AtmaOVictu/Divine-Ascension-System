import divine_agents.dialogue as dialog
from divine_agents.agent import Agent

if __name__ == "__main__":
    a1 = Agent("A1")
    a2 = Agent("A2", state="Jaz")
    for line in dialog.philosophical_dialogue(a1, a2):
        print(line)
