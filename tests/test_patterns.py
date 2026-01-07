# tests/test_patterns.py
import pytest
from uprompt import Uprompt

@pytest.fixture
def up():
    return Uprompt()

# Existing tests
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

# --- New Pattern Tests ---

def test_chain_of_thought(up):
    p = up.chain_of_thought(
        task="Solve math problem",
        input_text="If a train travels 60km in 1 hour, how far in 3 hours?"
    )
    assert "Solve math problem" in p.text
    assert "Think step by step" in p.text
    assert "Input: If a train travels 60km in 1 hour" in p.text
    assert p.pattern == "chain_of_thought"

def test_role_prompt(up):
    p = up.role_prompt(
        task="Explain AI like I'm 5",
        role="Teacher",
        input_text="What is machine learning?"
    )
    assert "Explain AI like I'm 5" in p.text
    assert "You are a Teacher" in p.text
    assert "Input: What is machine learning?" in p.text
    assert p.pattern == "role_prompt"

def test_self_critique(up):
    p = up.self_critique(
        task="Summarize text",
        input_text="This is a long paragraph that needs summarizing."
    )
    assert "Summarize text" in p.text
    assert "critique" in p.text.lower()
    assert "Input: This is a long paragraph" in p.text
    assert p.pattern == "self_critique"
