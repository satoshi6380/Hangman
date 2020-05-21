word = 'Simon says'


def what_to_do(instructions):
    inst = instructions.replace(word, '').strip()
    return 'I ' + inst if instructions.startswith(word) or instructions.endswith(word) else "I won't do it!"