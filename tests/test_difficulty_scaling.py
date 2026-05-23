import pytest

def test_attempt_values(config):
    assert config["attempts"]["easy"] > config["attempts"]["normal"] > config["attempts"]["hard"] 

def test_hint_penalty_scaling(config):
    assert config["hint_penalty"]["easy"] > config["hint_penalty"]["normal"] > config["hint_penalty"]["hard"]

def test_multiplier_scaling(config):
    assert config["scoring"]["difficulty_multiplier"]["easy"] < \
           config["scoring"]["difficulty_multiplier"]["normal"] < \
           config["scoring"]["difficulty_multiplier"]["hard"]