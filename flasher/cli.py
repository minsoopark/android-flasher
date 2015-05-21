import click

from .flasher import generate

@click.command()
def generate_script():
    generate()

