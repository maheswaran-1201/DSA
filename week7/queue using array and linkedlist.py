array_queue = []
MAX_SIZE = 5

def array_enqueue():
    if len(array_queue) == MAX_SIZE:
        print("Array Queue Overflow")
    else:
        element = int(input("Enter element: "))
        array_queue.append(element)
        print(element, "inserted into Array Queue")

def array_dequeue():
    if len(array_queue) == 0:
        print("Array Queue Underflow")
    else:
        element = array_queue.pop(0)
        print(element, "deleted from Array Queue")


def array_peek():
    if len(array_queue) == 0:
        print("Array Queue is empty")
    else:
        print("Front element:", array_queue[0])


def array_display():
    if len(array_queue) == 0:
        print("Array Queue is empty")
    else:
        print("Array Queue elements:")
        for element in array_queue:
            print(element, end=" ")
        print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self):
        element = int(input("Enter element: "))
        new_node = Node(element)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(element, "inserted into Linked List Queue")

    def dequeue(self):
        if self.front is None:
            print("Linked List Queue Underflow")
        else:
            element = self.front.data
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            print(element, "deleted from Linked List Queue")

    def peek(self):
        if self.front is None:
            print("Linked List Queue is empty")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Linked List Queue is empty")
        else:
            temp = self.front

            print("Linked List Queue elements:")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()


linked_queue = LinkedQueue()


while True:
    print("\n========== QUEUE IMPLEMENTATION ==========")
    print("1. Queue using Array")
    print("2. Queue using Linked List")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        while True:
            print("\n----- ARRAY QUEUE -----")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Display")
            print("5. Back to Main Menu")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                array_enqueue()
            elif ch == 2:
                array_dequeue()
            elif ch == 3:
                array_peek()
            elif ch == 4:
                array_display()
            elif ch == 5:
                break
            else:
                print("Invalid choice")

    elif choice == 2:
        while True:
            print("\n----- LINKED LIST QUEUE -----")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Display")
            print("5. Back to Main Menu")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                linked_queue.enqueue()
            elif ch == 2:
                linked_queue.dequeue()
            elif ch == 3:
                linked_queue.peek()
            elif ch == 4:
                linked_queue.display()
            elif ch == 5:
                break
            else:
                print("Invalid choice")

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice")