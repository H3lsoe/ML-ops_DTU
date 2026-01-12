import typer

def greet(name: str = "world", count: int = 1) -> None:
    """greet a person a given number of times."""
    for _ in range(count):
        print(f'Hello {name}!')

if __name__ == "__main__":
    typer.run(greet)
