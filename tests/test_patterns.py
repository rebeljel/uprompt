# tests/test_patterns.py
import pytest
from uprompt import Uprompt

@pytest.fixture
def up():
    return Uprompt()

def test_zero_shot(up):
    p = up.zero_shot(task="Summarize", input_text="This is a test.")
    assert "Summarize" in p.text
    assert "Input: This is a test." in p.text
    assert p.pattern == "zero_shot"

def test_one_shot(up):
    p = up.one_shot(
        task="Translate to German",
        examples=[{"text": "Good", "output": "Gut"}],
        input_text="Bye"
    )
    assert "Translate to German" in p.text
    assert "Input: Good" in p.text
    assert "Output: Gut" in p.text
    assert "Input: Bye" in p.text
    assert p.pattern == "one_shot"

def test_few_shot(up):
    p = up.few_shot(
        task="Translate to German",
        examples=[
            {"text": "Good morning", "output": "Guten Morgen"},
            {"text": "Good night", "output": "Gute Nacht"}
        ],
        input_text="See you later"
    )
    assert "Translate to German" in p.text
    assert "Input: Good morning" in p.text
    assert "Output: Guten Morgen" in p.text
    assert "Input: Good night" in p.text
    assert "Output: Gute Nacht" in p.text
    assert "Input: See you later" in p.text
    assert p.pattern == "few_shot"
