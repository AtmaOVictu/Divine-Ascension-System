import asyncio
from typing import List

from .agent import Agent

class RealtimeSession:
    """Simulate a realtime conversation between agents."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    async def run(self, prompts: List[str]) -> List[str]:
        """Run conversation by sending each prompt to all agents."""
        transcript: List[str] = []
        for question in prompts:
            for agent in self.agents:
                response = agent.respond(question)
                transcript.append(f"{agent.name} ({agent.state}): {response}")
                # Increase emotion to trigger potential transitions
                agent.update_emotion(0.6)
                new_state = agent.transition()
                if new_state != agent.history[-2]:
                    transcript.append(f"{agent.name} prehaja v stanje: {new_state}")
        return transcript

def simulate_realtime_session(agents: List[Agent], prompts: List[str]) -> List[str]:
    """Convenience wrapper to run a RealtimeSession synchronously."""
    session = RealtimeSession(agents)
    return asyncio.run(session.run(prompts))
