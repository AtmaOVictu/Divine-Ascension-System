class Codex:
    """Utility to generate README.md from project information."""

    def __init__(self, project_name, description, components, tests, usage_examples, license_info=None):
        self.project_name = project_name
        self.description = description
        self.components = components
        self.tests = tests
        self.usage_examples = usage_examples
        self.license_info = license_info

    def generate(self):
        readme = f"# {self.project_name}\n\n"
        readme += f"## Description\n{self.description}\n\n"
        readme += "## Components\n"
        for comp, details in self.components.items():
            readme += f"- `{comp}`: {details}\n"
        readme += "\n## Usage\n" + self.usage_examples + "\n"
        if self.tests:
            readme += "\n## Testing\n" + self.tests + "\n"
        if self.license_info:
            readme += "\n## License\n" + self.license_info + "\n"
        return readme

    def save(self, path="README.md"):
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(self.generate())


if __name__ == "__main__":
    PROJECT_NAME = "Divine-Ascension-System"
    DESCRIPTION = (
        "Divine-Ascension-System je napreden sistem za ontolo\u0161ke agente, "
        "ki prehajajo skozi razli\u010dna stanja zavedanja in sprejemajo moralne odlo\u010ditve."
    )
    COMPONENTS = {
        "divine_agents/agent.py": "Definicija agentov, njihovih lastnosti in prehodov.",
        "divine_agents/dialogue.py": "Implementacija filozofskih dialogov med agenti.",
        "tests/": "Enote za testiranje prehodov in moralnih odlo\u010ditv."
    }
    TESTS = "Za zagon testov uporabite:\n```bash\npytest\n```"
    USAGE = (
        "1. Klonirajte repozitorij in namestite odvisnosti:\n"
        "```bash\ngit clone <repo-url>\ncd Divine-Ascension-System\npip install -r requirements.txt\n```\n"
        "2. Za\u017eenite primer dialoga:\n"
        "```bash\npython -m divine_agents.dialogue\n```"
    )
    LICENSE = "Projekt je licenciran pod MIT licenco."

    codex = Codex(PROJECT_NAME, DESCRIPTION, COMPONENTS, TESTS, USAGE, LICENSE)
    codex.save()
    print("README.md generated.")
