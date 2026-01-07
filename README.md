# Uprompt

Uprompt is a Python library designed to simplify prompt engineering for large language models (LLMs). 
It provides a collection of well-known prompting patterns, including zero-shot, one-shot, few-shot, 
chain-of-thought, role-based, constrained, and self-critique prompts.  

With Uprompt, developers and researchers can:
- Generate structured prompts programmatically
- Quickly experiment with different prompt engineering strategies
- Keep prompts reusable, consistent, and easy to maintain

Example usage:

```python
from uprompt import Uprompt

up = Uprompt()
p = up.few_shot(
    instruction="Classify sentiment",
    examples=[("I love this!", "Positive"), ("I hate this", "Negative")],
    input_text="This is amazing"
)

print(p)
