import os


class DirectoryHelper:
    @staticmethod
    def current():
        return os.getcwd()

    @staticmethod
    def files(extension=None, path=None):
        if path is None:
            path = DirectoryHelper.current()

        files = []

        for file in os.listdir(path):
            filepath = os.path.join(path, file)

            if extension is None:
                files.append(filepath)
            elif file.endswith("." + extension):
                files.append(filepath)

        return files
