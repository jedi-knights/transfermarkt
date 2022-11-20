import os

from dotenv import load_dotenv
from invoke import call, task

load_dotenv()




@task
def clean(c):
    """
    Clean the project
    """
    print("Cleaning up...")

    c.run("rm -rf .venv")
    c.run("rm -rf coverage")
    c.run("rm -rf dist")
    c.run("rm -rf htmlcov")
    c.run("rm -rf .mypy_cache")
    c.run("rm -rf src/transfermarket/output.txt")


@task
def install(c):
    """
    Update Poetry dependencies
    """
    print("Install dependencies...")
    c.run("pip install --upgrade pip")
    c.run("poetry install --no-interaction --no-root")
    c.run("echo y | mypy --install-types")


@task(post=[install])
def setup(c):
    """Set up the project."""
    c.run("pip install --upgrade pip")
    c.run("python3 -m venv .venv")
    c.run(". .venv/bin/activate")


@task
def upgrade(c):
    """
    Upgrade project dependencies
    """
    print("Upgrade dependencies...")
    c.run("pip install --upgrade pip")
    c.run("poetry update --no-interaction")


@task
def build(c):
    """
    Build the package
    """
    print("Building the project")
    c.run("poetry build")


@task
def venv(c):
    print("Creating virtual environment...")
    c.run("python3 -m venv .venv")


@task
def test(c):
    """
    Run tests
    """
    print("Running tests...")
    c.run("poetry run pytest tests/unit")


@task
def cov(c):
    """Runs PyTest unit and integration tests with coverage."""
    c.run("poetry run coverage run -m pytest tests/unit")
    c.run("poetry run coverage lcov -o ./coverage/lcov.info")
    c.run("poetry run coverage report --fail-under=90")


@task()
def fmt(c):
    """
    Format the code
    """
    print("Formatting...")
    c.run("poetry run black .")
    c.run("poetry run isort .")
    c.run("poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place .")


@task
def lint(c):
    print("Linting...")
    c.run("poetry run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics")
    c.run("poetry run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics")
    # c.run("poetry run mypy .")
    # c.run("poetry run safety check")
    # c.run("poetry run bandit -r .")
    # c.run("poetry run pyupgrade --py36-plus .")
    # c.run("poetry run pre-commit run --all-files")


@task
def pylint(c):
    print("Linting...")
    c.run("poetry run pylint $(git ls-files '*.py')")


@task(pre=[clean, install, lint, test])
def pub(c):
    """
    Publishes the project to PyPI.
    """
    print("Publishing...")
    c.run("poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD")


@task(pre=[clean, install, lint, test], post=[build], default=True)
def ci(c):
    print("CI build...")
