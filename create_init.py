import os


def create_init_py(directory: str) -> None:
    """Ensure an __init__.py exists in the given directory."""
    init_file = os.path.join(directory, '__init__.py')
    if not os.path.exists(init_file):
        with open(init_file, 'w', encoding='utf-8') as fh:
            fh.write('# Automatically generated __init__.py\n')
        print(f"Created {init_file}")


def setup_package() -> None:
    """Ensure required packages are initialised."""
    for folder in ['divine_agents', 'tests']:
        create_init_py(folder)


if __name__ == '__main__':
    setup_package()
