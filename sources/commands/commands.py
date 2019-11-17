import click


class CLIHandler():
    @click.command()
    def commands():
        print("hello boy")


if __name__ == '__main__':
    CLIHandler.commands()
