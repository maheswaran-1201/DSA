class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self):
        element = int(input("Enter element: "))
        new_node = Node(element)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
            self.rear.next = self.front
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node

        print(element, "inserted into Circular Queue")

    def dequeue(self):
        if self.front is None:
            print("Circular Queue Underflow")
            return

        if self.front == self.rear:
            element = self.front.data
            self.front = None
            self.rear = None
            print(element, "deleted from Circular Queue")
            return

        element = self.front.data
        self.front = self.front.next
        self.rear.next = self.front
        print(element, "deleted from Circular Queue")

    def peek(self):
        if self.front is None:
            print("Circular Queue is empty")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Circular Queue is empty")
            return

        print("Circular Queue elements:")
        temp = self.front

        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front:
                break

        print()


circular_queue = CircularQueue()

while True:
    print("\n========== CIRCULAR LINKED LIST QUEUE ==========")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        circular_queue.enqueue()
    elif choice == 2:
        circular_queue.dequeue()
    elif choice == 3:
        circular_queue.peek()
    elif choice == 4:
        circular_queue.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")