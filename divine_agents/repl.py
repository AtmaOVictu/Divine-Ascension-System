import asyncio
from typing import Callable

from .agent import Agent


async def run_demo_loop(
    agent: Agent,
    input_func: Callable[[str], str] = input,
    print_func: Callable[[str], None] = print,
) -> None:
    """Interactive REPL loop for conversing with an agent.

    Parameters
    ----------
    agent:
        The agent participating in the conversation.
    input_func:
        Function used to obtain user input. Defaults to ``input``.
    print_func:
        Function used to output agent responses. Defaults to ``print``.
    """
    print_func("Type 'quit' or 'exit' to leave the conversation.")
    while True:
        try:
            user = await asyncio.to_thread(input_func, "You: ")
        except EOFError:
            break
        if user.strip().lower() in {"quit", "exit"}:
            break
        response = agent.respond(user)
        print_func(f"{agent.name} ({agent.state}): {response}")
        # escalate emotion slightly to showcase transitions
        new_emotion = min(agent.emotion + 0.2, 1.0)
        agent.update_emotion(new_emotion)
        agent.transition()

