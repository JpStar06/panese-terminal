class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, name, func, help_text=""):
        self.commands[name] = {
            "func": func,
            "help": help_text
        }

    def execute(self, name, args, ctx):
        cmd = self.commands.get(name)
        if not cmd:
            return False

        cmd["func"](args, ctx)
        return True