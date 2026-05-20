from src.game import update_display

def test_display_all_hidden(capsys):
    update_display("_____")
    captured = capsys.readouterr().out.strip()
    assert captured == "_ _ _ _ _"

def test_display_some_revealed(capsys):
    update_display("a__le")
    captured = capsys.readouterr().out.strip()
    assert captured == "a _ _ l e"

def test_display_all_revealed(capsys):
    update_display("apple")
    captured = capsys.readouterr().out.strip()
    assert captured == "a p p l e"

def test_display_repeated_letters(capsys):
    update_display("_pp__")
    captured = capsys.readouterr().out.strip()
    assert captured == "_ p p _ _"