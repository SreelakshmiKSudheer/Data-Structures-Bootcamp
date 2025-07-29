def equalStacks(h1, h2, h3):
    """
    Returns the maximum possible height of three stacks such that all stacks are of equal height
    after removing zero or more cylinders from the top of any stack.
    Each stack is represented as a list of integers, where each integer denotes the height of a cylinder.
    The function removes cylinders from the top of the tallest stack until all stacks are of equal height.
    Parameters:
        h1 (list of int): Heights of cylinders in the first stack (top at index 0).
        h2 (list of int): Heights of cylinders in the second stack (top at index 0).
        h3 (list of int): Heights of cylinders in the third stack (top at index 0).
    Returns:
        int: The maximum possible equal height of the three stacks.
    """
    # Calculate the total height of each stack
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)

    # Continue removing cylinders from the top of the tallest stack until all stacks are equal
    while not (s1 == s2 == s3):
        # If the first stack is the tallest (or tied for tallest), remove its top cylinder
        if s1 >= s2 and s1 >= s3:
            s1 -= h1.popleft()
        # If the second stack is the tallest (or tied for tallest), remove its top cylinder
        elif s2 >= s1 and s2 >= s3:
            s2 -= h2.popleft()
        # Otherwise, remove the top cylinder from the third stack
        else:
            s3 -= h3.popleft()

    # Return the maximum possible equal height
    return s1