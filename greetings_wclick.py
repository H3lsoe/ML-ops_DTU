import click 

@click.command()
@click.option('--name', default='world', help='Name to greet.')
@click.option('--count', default=1, help='Number of greetings.')
def greet(name: str, count: int) -> None:
    """greet a person a given number of times."""
    for _ in range(count):
        print(f'Hello {name}!')

if __name__ == "__main__":
    greet()


# uv run greetings_wclick.py --name Morten --count 3