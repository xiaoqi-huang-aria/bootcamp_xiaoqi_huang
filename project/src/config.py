"""
Project configuration helpers.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# project/src/config.py -> project/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

def load_env() -> bool:
    """Load environment variables from a local ``.env`` file."""
    return load_dotenv()

def get_key(name: str, default=None):
    """Get an environment variable by name."""
    return os.getenv(name, default)

def get_data_dir() -> Path:
    """Get the data directory path."""
    data_dir = Path(get_key("DATA_DIR", "./data"))

    # If DATA_DIR is relative, interpret it relative to PROJECT_ROOT
    if not data_dir.is_absolute():
        data_dir = PROJECT_ROOT / data_dir

    return data_dir.resolve()