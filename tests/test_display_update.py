from src.ui.display import update_display

def test_display_all_hidden(capsys, dummy_config):
    update_display("_____", dummy_config)
    captured = capsys.readouterr().out.strip()
    assert captured == "_ _ _ _ _"

def test_display_some_revealed(capsys, dummy_config):
    update_display("a__le", dummy_config)
    captured = capsys.readouterr().out.strip()
    assert captured == "a _ _ l e"

def test_display_all_revealed(capsys, dummy_config):
    update_display("apple", dummy_config)
    captured = capsys.readouterr().out.strip()
    assert captured == "a p p l e"

def test_display_repeated_letters(capsys, dummy_config):
    update_display("_pp__", dummy_config)
    captured = capsys.readouterr().out.strip()
    assert captured == "_ p p _ _"