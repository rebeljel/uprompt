from uprompt import Uprompt

up = Uprompt()
p = up.zero_shot(task="Summarize text", input_text="Hello world")
print(p.text)