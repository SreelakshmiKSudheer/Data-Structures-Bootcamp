def textEditor(operations):
    """
    Simulates a simple text editor with undo functionality.
    The editor supports the following operations:
        1 x : Append string x to the end of the current text.
        2 k : Delete the last k characters from the current text.
        3 k : Print the k-th character of the current text (1-based index).
        4   : Undo the last append or delete operation, reverting the text to its previous state.
    Args:
        operations (List[List[str]]): A list of operations, where each operation is represented as a list.
            - For '1' and '2', the second element is a string (to append) or an integer (number of characters to delete).
            - For '3', the second element is an integer (position to print).
            - For '4', the list contains only one element.
    Returns:
        None. The function prints output for '3' operations directly.
    """
    stack = []  # Stack to keep track of previous states for undo functionality
    s = ""      # Current text in the editor
    
    for op in operations:
        if op[0] == '1':  # Append operation
            stack.append(s)      # Save current state before modifying
            s += op[1]           # Append the given string to current text
        elif op[0] == '2':  # Delete operation
            stack.append(s)      # Save current state before modifying
            k = int(op[1])       # Number of characters to delete
            s = s[:-k]           # Remove last k characters
        elif op[0] == '3':  # Print operation
            k = int(op[1])       # Position to print (1-based index)
            print(s[k-1])        # Print the k-th character
        elif op[0] == '4':  # Undo operation
            s = stack.pop()      # Revert to previous state