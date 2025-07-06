from .agent import Agent
from .dialogue import philosophical_dialogue


def main() -> None:
    a1 = Agent("A1")
    a2 = Agent("A2", state="Jaz")
    for line in philosophical_dialogue(a1, a2):
        print(line)


if __name__ == "__main__":
    main()
