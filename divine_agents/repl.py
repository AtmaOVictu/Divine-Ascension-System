"""Simple REPL for interacting with ontological agents."""

from .agent import Agent


def run_demo_loop(agent1: Agent, agent2: Agent) -> None:
    """Interactive loop letting a user converse with two agents."""
    print("Vstop v REPL. Za izhod vpiši 'quit' ali 'exit'.")
    while True:
        try:
            user = input('Vi: ')
        except EOFError:
            break
        if user.strip().lower() in {'quit', 'exit'}:
            break
        print(f"{agent1.name} ({agent1.state}): {agent1.respond(user)}")
        agent1.transition()
        print(f"{agent2.name} ({agent2.state}): {agent2.respond(user)}")
        agent2.transition()

