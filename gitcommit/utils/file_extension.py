import os


class FileExtension:
    def get_extension(filepath):
        _, ext = os.path.splitext(filepath)
        return ext
