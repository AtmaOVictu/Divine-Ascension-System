from divine_agents.ecosystem import create_default_ecosystem


def test_simulation_shapes():
    eco = create_default_ecosystem()
    energy, tension = eco.run(10)
    assert len(energy) == 10 and len(energy[0]) == 5
    assert len(tension) == 10 and len(tension[0]) == 5


def test_state_progression():
    eco = create_default_ecosystem()
    eco.run(5)
    states = [agent.state for agent in eco.agents]
    assert all(state in agent.STATES for agent, state in zip(eco.agents, states))
