"""A simple click interface example."""
import click


@click.command()
@click.argument('name', required=True)
def say_hello_to(name):
    """print name that is specified using CLI."""
    print(f'hello {name}')


if __name__ == '__main__':
    say_hello_to()
