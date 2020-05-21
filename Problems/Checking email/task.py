def check_email(string):
    return ' ' not in string and 0 < string.rfind('@') + 1 < string.rfind('.')
