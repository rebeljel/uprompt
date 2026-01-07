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


# Usage

```python
# Zero-shot
p1 = up.zero_shot(task_description="Summarize the text", input_text="This is a long paragraph.")
print(p1.text)
```
# Output:
# Summarize the text
# Input: This is a long paragraph.
# Output:

# One-shot
```python
p2 = up.one_shot(
    task_description="Translate to German",
    examples=[{"text": "Good", "output": "Gut"}],
    input_text="Bye"
)
print(p2.text)
```
# Output:
# Translate to German
#
# Example:
# Input: Good
# Output: Gut
#
# Now do the same for:
# Input: Bye
# Output:

# Few-shot
```python
p3 = up.few_shot(
    task_description="Translate to German",
    examples=[
        {"text": "Good morning", "output": "Guten Morgen"},
        {"text": "Good night", "output": "Gute Nacht"},
    ],
    input_text="See you later"
)
print(p3.text)
```
# Output:
# Translate to German
#
# Examples:
# Input: Good morning
# Output: Guten Morgen
#
# Input: Good night
# Output: Gute Nacht
#
# Now do the same for:
# Input: See you later
# Output:

# Chain-of-Thought
```python
p4 = up.chain_of_thought(
    task_description="Solve math problem",
    input_text="If a train travels 60km in 1 hour, how far in 3 hours?"
)
print(p4.text)
```
# Output:
# Solve math problem
# Think step by step.
# Input: If a train travels 60km in 1 hour, how far in 3 hours?
# Output:

# Role prompt
```python
p5 = up.role_prompt(
    task_description="Explain AI like I'm 5",
    role="Teacher",
    input_text="What is machine learning?"
)
print(p5.text)
```
# Output:
# Explain AI like I'm 5
# You are a Teacher.
# Input: What is machine learning?
# Output:

# Self-critique
```python
p6 = up.self_critique(
    task_description="Summarize text",
    input_text="This is a long paragraph that needs summarizing."
)
print(p6.text)
```
# Output:
# Summarize text
# Provide an answer and then critique it.
# Input: This is a long paragraph that needs summarizing.
# Output:
