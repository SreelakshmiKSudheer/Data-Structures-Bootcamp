def isBalanced(s):
    """
    Determines if the input string of brackets is balanced.
    A string is considered balanced if:
    - Every opening bracket has a corresponding closing bracket of the same type.
    - Brackets are closed in the correct order.
    Supported brackets: (), {}, []
    Args:
        s (str): The string containing brackets to be checked.
    Returns:
        str: "YES" if the string is balanced, "NO" otherwise.
    Line by line comments:
        stack = []  # Initialize an empty stack to keep track of opening brackets.
        brackets = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets.
        for c in s:  # Iterate through each character in the string.
            if c in brackets.values():  # If character is an opening bracket.
                stack.append(c)  # Push opening bracket onto the stack.
            elif c in brackets:  # If character is a closing bracket.
                if not stack or stack[-1] != brackets[c]:  # If stack is empty or top doesn't match.
                    return "NO"  # String is not balanced.
                stack.pop()  # Pop the matched opening bracket from the stack.
        return "YES" if not stack else "NO"  # If stack is empty, all brackets are balanced.
    """
    # Write your code here
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in brackets.values():
            stack.append(c)
        elif c in brackets:
            if not stack or stack[-1] != brackets[c]:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"