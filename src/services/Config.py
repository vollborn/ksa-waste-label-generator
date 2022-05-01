from src.config import colors, backgrounds


class Config:
    data = {}

    def __init__(self):
        self.data = {
            "colors": colors.get(),
            "backgrounds": backgrounds.get()
        }

    def get(self, key):
        split = key.split('.')
        configValue = self.data

        try:
            for part in split:
                configValue = configValue[part]
        except KeyError:
            return None

        return configValue
