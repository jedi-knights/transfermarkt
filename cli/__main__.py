import os

import click
from dotenv import load_dotenv

basedir = os.path.abspath(f"{os.path.dirname(__file__)}/..")
env_file = os.path.join(basedir, ".env")
load_dotenv(env_file)

plugin_folder = os.path.join(os.path.dirname(__file__), "commands")


class MyCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py") and filename != "__init__.py":
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + ".py")
        with open(fn) as f:
            code = compile(f.read(), fn, "exec")
            eval(code, ns, ns)

        return ns["cli"]


cli = MyCLI(
    help="This tool's subcommands are loaded from a " "plugin folder dynamically."
)


def main():
    cli()


if __name__ == "__main__":
    main()