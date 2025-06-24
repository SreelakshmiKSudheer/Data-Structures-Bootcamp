def display(stack, top):
    print("\nStack:", end=" ")
    i = 0
    while i <= top:
        print(stack[i], end=" ")
        i += 1
    print()

def push(stack, top, size):
    if top[0] == size - 1:
        print("\nStack overflow\n")
    else:
        item = int(input("Item to push: "))
        top[0] += 1
        if len(stack) > top[0]:
            stack[top[0]] = item
        else:
            stack.append(item)
        display(stack, top[0])

def pop(stack, top):
    if top[0] == -1:
        print("\nStack underflow\n")
    else:
        top[0] -= 1
        if top[0] == -1:
            print("\nStack is now empty\n")
        else:
            display(stack, top[0])

def main():
    size = int(input("Enter size of stack: "))
    stack = []
    top = [-1]  # Use list to make top mutable

    while True:
        print("\n1. Push   2. Pop   3. exit\n")
        choice = int(input("Choice : "))
        if choice == 1:
            push(stack, top, size)
        elif choice == 2:
            pop(stack, top)
        elif choice == 3:
            break

if __name__ == "__main__":
    main()
