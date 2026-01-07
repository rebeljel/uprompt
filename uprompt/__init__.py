# uprompt/__init__.py
from .core import Uprompt
from .patterns import Patterns

def _add_patterns_methods():
    def zero_shot(self, *, task_description: str, input_text: str, category: str = None):
        """
        Create a zero-shot prompt.

        Args:
            task_description (str): Natural language description of the task.
            input_text (str): Input text for the task.
            category (str, optional): Optional category of the task (e.g., 'summarization').

        Returns:
            Prompt: A Prompt object containing the formatted prompt text.
        """
        return Patterns.zero_shot(task_description=task_description, input_text=input_text, category=category)

    def one_shot(self, *, task_description: str, examples: list[dict], input_text: str):
        """
        Create a one-shot prompt.

        Args:
            task_description (str): Natural language description of the task.
            examples (list[dict]): A list of example input/output pairs, e.g., [{'input': 'Hi', 'output': 'Salut'}].
            input_text (str): Input text for the task.

        Returns:
            Prompt: A Prompt object containing the formatted prompt text.
        """
        return Patterns.one_shot(task_description=task_description, examples=examples, input_text=input_text)

    def few_shot(self, *, task_description: str, examples: list[dict], input_text: str):
        """
        Create a few-shot prompt.

        Args:
            task_description (str): Natural language description of the task.
            examples (list[dict]): A list of example input/output pairs.
            input_text (str): Input text for the task.

        Returns:
            Prompt: A Prompt object containing the formatted prompt text.
        """
        return Patterns.few_shot(task_description=task_description, examples=examples, input_text=input_text)

    def chain_of_thought(self, *, task_description: str, input_text: str):
        """
        Create a chain-of-thought style prompt for reasoning tasks.

        Args:
            task_description (str): Natural language description of the task.
            input_text (str): Input text for the task.

        Returns:
            Prompt: A Prompt object containing the formatted prompt text.
        """
        return Patterns.chain_of_thought(task_description=task_description, input_text=input_text)

    def role_prompt(self, *, task_description: str, role: str, input_text: str):
        """
        Create a role-based prompt (e.g., "You are a teacher...").

        Args:
            task_description (str): Natural language description of the task.
            role (str): The role the model should assume.
            input_text (str): Input text for the task.

        Returns:
            Prompt: A Prompt object containing the formatted prompt text.
        """
        return Patterns.role_prompt(task_description=task_description, role=role, input_text=input_text)

    def self_critique(self, *, task_description: str, input_text: str):
        """
        Create a self-critique style prompt for reviewing outputs.

        Args:
            task_description (str): Natural language description of the task.
            input_text (str): Input text for the task.

        Returns:
            Prompt: A Prompt object containing the formatted prompt text.
        """
        return Patterns.self_critique(task_description=task_description, input_text=input_text)

    # Attach methods to Uprompt class
    setattr(Uprompt, "zero_shot", zero_shot)
    setattr(Uprompt, "one_shot", one_shot)
    setattr(Uprompt, "few_shot", few_shot)
    setattr(Uprompt, "chain_of_thought", chain_of_thought)
    setattr(Uprompt, "role_prompt", role_prompt)
    setattr(Uprompt, "self_critique", self_critique)

_add_patterns_methods()
