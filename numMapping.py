import os

text = input()
text = text.replace ('"', '')
text = text.replace (',', ';')

if ("%;" in text) and ("*" not in text):
    text = text.replace ('%', '')

print(text)

#copies the result to clipboard
command = 'echo | set /p nul=' + text.strip() + '| clip'
os.system(command)