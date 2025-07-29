def getMax(operations):
    # Write your code here
    # stack = []
    # maxStack = []
    # result = []
    # for operation in operations:
    #     op = list(map(int, operation.split()))
    #     if op[0] == 1:
    #         val = op[1]
    #         stack.append(val)
    #         if not maxStack or val >= maxStack[-1]:
    #             maxStack.append(val)
    #     elif op[0] == 2:
    #         rem = stack.pop()
    #         if rem == maxStack[-1]:
    #             maxStack.pop()
    #     elif op[0] == 3:
    #         result.append(maxStack[-1])
    
    
    stack = []  # Initialize an empty stack to store elements
    result = []  # Initialize a list to store results of 'max' queries

    for operation in operations:  # Iterate through each operation
        op = list(map(int, operation.split()))  # Split operation into integers
        if op[0] == 1:  # If operation is '1', push value onto stack
            val = op[1]
            stack.append(val)
        elif op[0] == 2:  # If operation is '2', pop top element from stack
            stack.pop()
        elif op[0] == 3:  # If operation is '3', append current max to result
            result.append(max(stack))

    return result