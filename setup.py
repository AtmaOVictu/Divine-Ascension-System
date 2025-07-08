from setuptools import setup, find_packages

setup(
    name='divine_agents',
    version='0.1.0',
    description='Agent-based philosophical simulation framework',
    packages=find_packages(include=['divine_agents', 'divine_agents.*']),
    python_requires='>=3.8',
)
