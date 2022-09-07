def isValid(s: str) -> bool:
    leftSymbols = []
    for c in s:
        if c in ['(', '{', '[']:
            leftSymbols.append(c)
        elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
            leftSymbols.pop()
        elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
            leftSymbols.pop()
        elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
            leftSymbols.pop()
        else:
            return False
    return leftSymbols == []


if _name_ == '_main_':
    print(isValid("{}[]"))
    print(isValid("[}{]"))