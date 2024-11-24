# Python build-in packages
from pathlib import Path

class PathDefinitions:

    @staticmethod
    def get_current_dir():
        return Path.cwd()
    
    