from dotenv import load_dotenv
from invoke import task

load_dotenv()


@task
def update(c):
    print("Updating dependencies...")
    c.run("poetry update")


@task
def build(c):
    print("Building the project")
    c.run("poetry build")


@task
def venv(c):
    print("Creating virtual environment...")
    c.run("python3 -m venv .venv")


@task
def clean(c):
    print("Cleaning up...")
    c.run("rm -rf coverage")
    c.run("rm -rf dist")


@task
def fixtures(c):
    """Lists PyTest fixtures."""
    c.run("pytest --fixtures")


@task
def utest(c):
    """Runs PyTest unit tests."""
    c.run("pytest tests/unit")


@task
def itest(c):
    """Runs PyTest integration tests."""
    c.run("pytest tests/integration")


@task
def test(c):
    """Runs PyTest unit and integration tests."""
    c.run("pytest tests/unit tests/integration")


@task
def ucover(c):
    """Runs PyTest unit tests with coverage."""
    c.run("coverage run -m pytest tests/unit")
    c.run("coverage lcov -o ./coverage/lcov.info")
    c.run("coverage report --fail-under=90")


@task
def cover(c):
    """Runs PyTest unit and integration tests with coverage."""
    c.run("coverage run -m pytest tests/unit")
    c.run("coverage lcov -o ./coverage/lcov.info")


@task
def lint(c):
    print("Linting...")
    # c.run("poetry run black .")
    # c.run("poetry run isort .")
    # c.run(
    #     "poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place ."
    # )
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


@task()
def format(c):
    print("Formatting...")
    c.run("poetry run black .")
    c.run("poetry run isort .")
    c.run("poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place .")


@task(pre=[clean, update, format, lint, utest], post=[build], default=True)
def ci(c):
    print("CI build...")
