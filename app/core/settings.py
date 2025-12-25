# app/core/settings.py
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"

# Load environment variables from .env file
load_dotenv(dotenv_path=ENV_PATH, override=False)

MONGO_CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING", "")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "")