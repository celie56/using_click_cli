# Using Click in Python

Click is a tool used to make quick CLI interfaces.

This doc is intended to outline how to set up a click interface and test that it is working.



## Setup

`pipenv install click`



## A basic file

```python
"""A simple click interface example."""
import click


@click.command()
@click.argument('name', required=True)
def say_hello_to(name):
    """print name that is specified using CLI."""
    print(f'hello {name}')


if __name__ == '__main__':
    say_hello_to()
```

[Quickstart &#8212; Click Documentation (7.x)](https://click.palletsprojects.com/en/7.x/quickstart/#basic-concepts-creating-a-command)



## Running a command

```bash
(temp)  🌈  ~/dev/temp  python say_hello_to.py chris
hello chris
```



## Creating a unit test

```python
"""Tests for our greet program."""
import string
import random

from click.testing import CliRunner
import greet


def make_fake_name() -> str:
    """Fake name generator."""
    return ''.join(random.choices(string.ascii_uppercase, k=10))


def test_say_hello_to() -> None:
    """Test our click CLI."""
    runner = CliRunner()
    fake_name = make_fake_name()
    result = runner.invoke(greet.say_hello_to, [fake_name])

    assert result.exit_code == 0
    assert result.output == f'hello {fake_name}\n'
```

[Testing Click Applications &#8212; Click Documentation (7.x)](https://click.palletsprojects.com/en/7.x/testing/)



```bash
(temp) 🌈  ~/dev/temp  pytest
============================= test session starts ==============================
platform linux -- Python 3.8.2, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: /home/chris/dev/temp
collected 1 item                                                               

test_greet.py .                                                          [100%]

============================== 1 passed in 0.01s ===============================
```


