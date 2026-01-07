# uprompt/patterns.py
from .core import Prompt

class Patterns:
    @staticmethod
    def zero_shot(
        task_description: str,
        input_text: str,
        category: str = None
    ) -> Prompt:
        """
        Generate a zero-shot prompt.

        Zero-shot prompts provide the model with an instruction and input text
        without giving any examples. The model is expected to perform the task
        directly.

        Args:
            task_description (str): A natural language description of the task to perform.
            input_text (str): The input text that the model will process.
            category (str, optional): Optional category of the task, e.g., 'summarization',
                                      'translation', 'sentiment'. Defaults to None.

        Returns:
            Prompt: A Prompt object containing the formatted prompt text and metadata.
        """
        text = f"{task_description}\nInput: {input_text}\nOutput:"
        return Prompt(text=text, pattern="zero_shot", category=category)

    @staticmethod
    def one_shot(
        task_description: str,
        examples: list[dict],
        input_text: str
    ) -> Prompt:
        """
        Generate a one-shot prompt.

        One-shot prompts give the model a single example of input/output before
        asking it to perform the task on new input.

        Args:
            task_description (str): A description of the task.
            examples (list[dict]): A list containing exactly one example, with keys 'text' and 'output'.
            input_text (str): Input text for the model to process.

        Returns:
            Prompt: A Prompt object containing the formatted prompt text.
        """
        ex = examples[0]
        text = (
            f"{task_description}\n\n"
            f"Example:\nInput: {ex['text']}\nOutput: {ex['output']}\n\n"
            f"Now do the same for:\nInput: {input_text}\nOutput:"
        )
        return Prompt(text=text, pattern="one_shot")

    @staticmethod
    def few_shot(
        task_description: str,
        examples: list[dict],
        input_text: str
    ) -> Prompt:
        """
        Generate a few-shot prompt.

        Few-shot prompts provide multiple examples before asking the model to
        perform the task on new input.

        Args:
            task_description (str): A description of the task.
            examples (list[dict]): A list of example input/output dictionaries.
            input_text (str): Input text for the model to process.

        Returns:
            Prompt: A Prompt object containing the formatted prompt text.
        """
        example_str = "\n\n".join([f"Input: {ex['text']}\nOutput: {ex['output']}" for ex in examples])
        text = (
            f"{task_description}\n\nExamples:\n{example_str}\n\n"
            f"Now do the same for:\nInput: {input_text}\nOutput:"
        )
        return Prompt(text=text, pattern="few_shot")

    @staticmethod
    def chain_of_thought(
        task_description: str,
        input_text: str
    ) -> Prompt:
        """
        Generate a chain-of-thought prompt.

        Chain-of-thought prompts encourage the model to reason step by step before
        providing an answer.

        Args:
            task_description (str): A description of the task.
            input_text (str): Input text for the model to process.

        Returns:
            Prompt: A Prompt object containing the formatted prompt text.
        """
        text = f"{task_description}\nThink step by step.\nInput: {input_text}\nOutput:"
        return Prompt(text=text, pattern="chain_of_thought")

    @staticmethod
    def role_prompt(
        task_description: str,
        role: str,
        input_text: str
    ) -> Prompt:
        """
        Generate a role-based prompt.

        The model assumes a role before performing the task (e.g., "You are a teacher").

        Args:
            task_description (str): A description of the task.
            role (str): The role the model should assume.
            input_text (str): Input text for the model to process.

        Returns:
            Prompt: A Prompt object containing the formatted prompt text.
        """
        text = f"{task_description}\nYou are a {role}.\nInput: {input_text}\nOutput:"
        return Prompt(text=text, pattern="role_prompt")

    @staticmethod
    def self_critique(
        task_description: str,
        input_text: str
    ) -> Prompt:
        """
        Generate a self-critique prompt.

        The model provides an answer and then critiques it to improve quality.

        Args:
            task_description (str): A description of the task.
            input_text (str): Input text for the model to process.

        Returns:
            Prompt: A Prompt object containing the formatted prompt text.
        """
        text = f"{task_description}\nProvide an answer and then critique it.\nInput: {input_text}\nOutput:"
        return Prompt(text=text, pattern="self_critique")
