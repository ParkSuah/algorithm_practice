def solution(s):
    answer = True
    stack = []

    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")" and len(stack) > 0:
            stack.pop()
        else:
            return False

    answer = False if len(stack) > 0 else True
    return answer
