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
