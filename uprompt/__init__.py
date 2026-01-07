# uprompt/__init__.py
from .core import Uprompt
from .patterns import Patterns

def _add_patterns_methods():
    def zero_shot(self, *, task: str, input_text: str):
        return Patterns.zero_shot(task=task, input_text=input_text)

    def one_shot(self, *, task: str, examples: list[dict], input_text: str):
        return Patterns.one_shot(task=task, examples=examples, input_text=input_text)

    def few_shot(self, *, task: str, examples: list[dict], input_text: str):
        return Patterns.few_shot(task=task, examples=examples, input_text=input_text)
    
    def chain_of_thought(self, *, task: str, input_text: str):
        return Patterns.chain_of_thought(task=task, input_text=input_text)

    setattr(Uprompt, "chain_of_thought", chain_of_thought)
    setattr(Uprompt, "zero_shot", zero_shot)
    setattr(Uprompt, "one_shot", one_shot)
    setattr(Uprompt, "few_shot", few_shot)


_add_patterns_methods()