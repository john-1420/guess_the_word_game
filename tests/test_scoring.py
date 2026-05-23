from src.gameplay.scoring import calculate_score

def test_score_no_hints(config):
    score = calculate_score(5, "normal", 0, config)
    assert score == 5 * config["scoring"]["difficulty_multiplier"]["normal"]

def test_score_with_hints(config):
    score = calculate_score(5, "normal", 2, config)
    assert score == max(
        5 * config["scoring"]["difficulty_multiplier"]["normal"] -
        2 * config["hint_penalty"]["normal"],
        0
    )

def test_score_never_negative(config):
    score = calculate_score(0, "hard", 10, config)
    assert score == 0