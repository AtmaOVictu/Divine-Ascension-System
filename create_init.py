import os

DIRECTORIES = ['divine_agents', 'tests']


def create_init_py(directory: str) -> None:
    init_file = os.path.join(directory, '__init__.py')
    if not os.path.exists(init_file):
        with open(init_file, 'w') as f:
            f.write('# Automatically generated __init__.py\n')
        print(f'Created {init_file}')


def setup_package() -> None:
    for directory in DIRECTORIES:
        create_init_py(directory)


if __name__ == '__main__':
    setup_package()
