# Uprompt

A Python library for **prompt engineering design patterns**. Easily create zero-shot, one-shot, few-shot, chain-of-thought, role-based, and self-critique prompts with a clean and structured API.

---

## Features

- Zero-shot prompts  
- One-shot prompts (single example)  
- Few-shot prompts (multiple examples)  
- Chain-of-thought reasoning prompts  
- Role / persona prompts  
- Self-critique prompts  
- Easy-to-use keyword-argument API  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/uprompt.git
cd uprompt
```
2. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux
# OR
.\.venv\Scripts\Activate.ps1 # Windows PowerShell
```


3. Install the package in editable mode:

```bash
pip install -e .
```

4. Install dev dependencies for testing:


```bash
pip install pytest
```


## Usage


# Zero-shot
p1 = up.zero_shot(task="Summarize the text", input_text="This is a long paragraph.")
print(p1.text)

# One-shot
p2 = up.one_shot(
    task="Translate to German",
    examples=[{"text": "Good", "output": "Gut"}],
    input_text="Bye"
)
print(p2.text)

# Few-shot
p3 = up.few_shot(
    task="Translate to German",
    examples=[
        {"text": "Good morning", "output": "Guten Morgen"},
        {"text": "Good night", "output": "Gute Nacht"},
    ],
    input_text="See you later"
)
print(p3.text)

# Chain-of-Thought
p4 = up.chain_of_thought(
    task="Solve math problem",
    input_text="If a train travels 60km in 1 hour, how far in 3 hours?"
)
print(p4.text)

# Role prompt
p5 = up.role_prompt(
    task="Explain AI like I'm 5",
    role="Teacher",
    input_text="What is machine learning?"
)
print(p5.text)

# Self-critique
p6 = up.self_critique(
    task="Summarize text",
    input_text="This is a long paragraph that needs summarizing."
)
print(p6.text)


## Project Structure

uprompt/                <- package folder
├── __init__.py          <- Uprompt class + pattern methods
├── core.py              <- Uprompt & Prompt classes
├── patterns.py          <- Prompt engineering pattern implementations
tests/
└── test_patterns.py     <- pytest tests
pyproject.toml           <- project metadata
.venv/                   <- virtual environment
README.md
LICENSE

## Testing

pytest tests/

