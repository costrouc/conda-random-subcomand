from conda import plugins

from conda_random_subcommand.command import run_random_subcommand


@plugins.hookimpl
def conda_subcommands():
    """
    Register external subcommands in conda
    """
    yield plugins.CondaSubcommand(
        name="random",
        summary="random subcommand",
        action=run_random_subcommand,
    )
