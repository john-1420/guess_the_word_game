import json
import pytest
from pathlib import Path

@pytest.fixture
def config():
    path = Path("config/settings.json")
    return json.loads(path.read_text())

@pytest.fixture
def dummy_config():
    return {"colour_output": False}