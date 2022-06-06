import inspect
import sys

from src.services.CLI import CLI
from src.services.Config import Config
from src.services.Database import Database


class DependencyInjector:
    instance = None
    dependencies = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    @classmethod
    def inject(cls, function, *custom_arguments):
        instance = cls.get_instance()

        if instance.dependencies is None:
            config = Config()

            instance.dependencies = {
                "args": sys.argv,
                "cli": CLI(),
                "config": config,
                "database": Database(config)
            }

        argSpecs = inspect.getfullargspec(function)
        args = []

        dependencyKeys = instance.dependencies.keys()

        counter = 0
        customArgCount = len(custom_arguments)

        for argName in argSpecs.args:
            if counter < customArgCount:
                counter += 1
                continue

            if argName in dependencyKeys:
                args.append(instance.dependencies[argName])

        return function(*custom_arguments, *args)
