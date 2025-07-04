"""Package exposing core classes and utilities for Divine Ascension."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from . import time_utils

__all__ = ["Agent", "philosophical_dialogue", "time_utils"]
