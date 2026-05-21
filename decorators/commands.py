class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, name, func, help_text="", details=""):
        self.commands[name] = {
            "name": name,
            "func": func,
            "help": help_text,
            "details": details
        }

    def execute(self, name, args, ctx):

        cmd = self.commands.get(name)

        if not cmd:
            return False

        cmd["func"](
            args,
            ctx=ctx,
            state=ctx.get("state")
        )

        return True

    def get_command(self, name):
        return self.commands.get(name)


registry = CommandRegistry()


def comando(name, help_text="", details=""):

    def decorator(func):

        registry.register(
            name,
            func,
            help_text,
            details
        )

        return func

    return decorator