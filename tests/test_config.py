from src.config_manager import save_config
import json

def test_config_save(tmp_path, monkeypatch):
    fake_path = tmp_path / "settings.json"
    monkeypatch.setattr("src.config_manager.CONFIG_PATH", fake_path)

    config = {"colour_output": False}
    save_config(config)

    loaded = json.loads(fake_path.read_text())
    assert loaded["colour_output"] is False