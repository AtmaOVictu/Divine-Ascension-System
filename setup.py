from setuptools import setup, find_packages

setup(
    name='divine_agents',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'divine_agents=divine_agents.dialogue:philosophical_dialogue',
        ],
    },
)
