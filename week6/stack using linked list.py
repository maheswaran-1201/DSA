class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into stack")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            data = self.top.data
            self.top = self.top.next
            print(data, "popped from stack")

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element is:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack elements are:")
            
            while temp is not None:
                print(temp.data)
                temp = temp.next

stack = Stack()

while True:
    print("\n--- STACK OPERATIONS ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to push: "))
        stack.push(element)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.peek()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")