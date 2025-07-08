# Divine-Ascension-System

This project contains a minimal framework for simulating ontological agents
that transition between the states **Ego**, **Jaz** and **Enotnost**.  Each agent
tracks its emotional intensity and tension levels which influence state
transitions and dialogue generation.

Key features:

* Automatic transitions when tension exceeds `0.7` or emotion exceeds `0.5`.
* Exponential tension decay over time.
* Agents can influence one another, increasing or decreasing tension.
* A `philosophical_dialogue` helper that produces interactions reflecting the
  current states of the agents.

Run the unit tests with `python -m unittest` to verify behaviour.
