import json
from pathlib import Path


def extract_utilisateurs_from_json():
    """
    Extract data from JSON source file.
    This is the EXTRACT phase.
    """

    # Path to JSON file
    file_path = Path(__file__).parent / "data" / "utilisateurs.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data
