import json
from utils.error import LoadingSettingsError


def load(file) -> list:
    """Loads Settings
    
    Export -> [START DIRECTORY, END DIRECTORY, THREADS, CODEC]
    """
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            exportData = data["export"]
            rendering = data["rendering"]
            importing = data["import"]

            end_directory = exportData["end_directory"]

            threads = rendering["threads"]

            start_directory = importing["start_directory"]
            codec = rendering["codec"]

            return [start_directory, end_directory, threads, codec]
    except Exception:
        raise LoadingSettingsError(f"Failed to load {file}")