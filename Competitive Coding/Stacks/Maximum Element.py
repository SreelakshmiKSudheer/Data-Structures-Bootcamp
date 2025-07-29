def getMax(operations):
    # Write your code here
    stack = []
    maxStack = []
    result = []
    for operation in operations:
        op = list(map(int, operation.split()))
        if op[0] == 1:
            val = op[1]
            stack.append(val)
            if not maxStack or val >= maxStack[-1]:
                maxStack.append(val)
        elif op[0] == 2:
            rem = stack.pop()
            if rem == maxStack[-1]:
                maxStack.pop()
        elif op[0] == 3:
            result.append(maxStack[-1])

    return result
