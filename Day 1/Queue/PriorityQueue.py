f = [] #pointers for front elements
r = [] #pointers for rear elements
pq = [] #priority queue
np = 0 #number of priorities
size = 0 #single queue size

def display():
    print("\nQueue : ")
    for i in range(np):
        if f[i] != -1:
            for j in range(f[i], r[i]+1):
                print(pq[i][j], end=" ")
        print()
    print()

def enqueue():
    global pq, f, r
    while True:
        priority = int(input("\nEnter priority : "))
        if priority > np:
            print(f"Only {np} priorities !")
        else:
            break

    if r[priority - 1] == size - 1:
        print(f"\nQueue overflow for priority {priority}")
    else:
        item = int(input("Enter item to insert : "))
        r[priority - 1] += 1
        pq[priority - 1][r[priority - 1]] = item
        if r[priority - 1] == 0:
            f[priority - 1] = 0
        display()

def dequeue():
    global f, r
    for i in range(np):
        if f[i] != -1:
            f[i] += 1
            if f[i] > r[i]:
                f[i] = -1
                r[i] = -1
            display()
            break
    else:
        print("\nQueue underflow")

def main():
    global size, np, f, r, pq

    size = int(input("Enter size of queue : "))
    np = int(input("Enter number of priorities : "))

    f = [-1] * np
    r = [-1] * np
    pq = [[0] * size for _ in range(np)]

    while True:
        print("\nChoices : \n1. Insert item\n2. Delete item\n3. Exit")
        choice = int(input("Enter desired choice[1/2/3] : "))
        if choice == 1:
            enqueue()
        elif choice == 2:
            dequeue()
        elif choice == 3:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
