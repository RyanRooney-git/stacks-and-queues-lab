def is_valid_parentheses(s: str) -> bool:
    """
    Validates (), {}, [] using a stack.
    """

    stack = []
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:

        if char in "({[":
            stack.append(char)

        elif char in ")}]":
            if not stack:
                return False
            if stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0