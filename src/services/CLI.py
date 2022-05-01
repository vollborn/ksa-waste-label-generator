import colorama

from src.services.Config import Config


class CLI:
    config = None

    def __init__(self):
        self.config = Config()
        colorama.init(autoreset=True)

    def println(self, message="", color=None, background=None):
        if color is None:
            color = self.config.get("colors.default")

        if background is None:
            background = self.config.get("backgrounds.default")

        print(color + background + message)

    def print(self, message="", color=None, background=None):
        if color is None:
            color = self.config.get("colors.default")

        if background is None:
            background = self.config.get("backgrounds.default")

        print(color + background + message, end="")
