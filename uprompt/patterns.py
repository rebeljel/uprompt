# uprompt/patterns.py
from .core import Prompt

class Patterns:
    @staticmethod
    def zero_shot(task: str, input_text: str) -> Prompt:
        text = f"{task}\nInput: {input_text}\nOutput:"
        return Prompt(text=text, pattern="zero_shot")

    @staticmethod
    def one_shot(task: str, examples: list[dict], input_text: str) -> Prompt:
        # Only one example is expected
        ex = examples[0]
        text = f"{task}\n\nExample:\nInput: {ex['text']}\nOutput: {ex['output']}\n\nNow do the same for:\nInput: {input_text}\nOutput:"
        return Prompt(text=text, pattern="one_shot")

    @staticmethod
    def few_shot(task: str, examples: list[dict], input_text: str) -> Prompt:
        example_str = "\n\n".join([f"Input: {ex['text']}\nOutput: {ex['output']}" for ex in examples])
        text = f"{task}\n\nExamples:\n{example_str}\n\nNow do the same for:\nInput: {input_text}\nOutput:"
        return Prompt(text=text, pattern="few_shot")
    
    @staticmethod
    def chain_of_thought(task: str, input_text: str) -> Prompt:
        text = f"{task}\nThink step by step.\nInput: {input_text}\nOutput:"
        return Prompt(text=text, pattern="chain_of_thought")