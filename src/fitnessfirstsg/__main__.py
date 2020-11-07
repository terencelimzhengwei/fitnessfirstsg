"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Unofficial API client for Fitness First SG."""


if __name__ == "__main__":
    main(prog_name="fitnessfirstsg")  # pragma: no cover
