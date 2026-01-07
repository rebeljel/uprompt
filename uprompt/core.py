# uprompt/core.py
class Prompt:
    def __init__(self, text: str, pattern: str, metadata: dict = None):
        self.text = text
        self.pattern = pattern
        self.metadata = metadata or {}

    def __str__(self):
        return self.text

class Uprompt:
    """
    Main entry point for Uprompt library.
    """

    def __init__(self):
        # Could store default config later
        pass
