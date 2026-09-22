class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None

    def create(self):
        n=int(input("enter the number of nodes:"))
        for i in range(n):
            data = int(input(f"Enter data for node{i+1}:"))
            new_node=Node(data)
            if self.head is None:
                self.head=new_node
                new_node.next=self.head
            else:
                temp = self.head
                while temp.next != self.head:
                    temp=temp.next
            temp.next=new_node
            new_node.next=self.head
        print("circular Linked list is created succesfully")

    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node
        print("Node inserted at beginning.")

        
    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        print("Node inserted at end.")


    def insert_position(self):
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))

        new_node = Node(data)

        # Insert at first position
        if pos == 1:
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                new_node.next = self.head
                temp.next = new_node
                self.head = new_node

            print("Node inserted at position", pos)
            return

        if self.head is None:
            print("Invalid position.")
            return

        temp = self.head

        for i in range(1, pos - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid position.")
                return

        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted at position", pos)

    def delete_by_value(self):
        value = int(input("Enter value to delete: "))
        if self.head is None:
            print("List is empty.")
            return
        if self.head.data == value and self.head.next == self.head:
            self.head = None
            print("Node deleted.")
            return
        if self.head.data == value:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            print("Node deleted.")
            return
        prev = self.head
        temp = self.head.next
        while temp != self.head:
            if temp.data == value:
                prev.next = temp.next
                print("Node deleted.")
                return
            prev = temp
            temp = temp.next
        print("Value not found.")

    def delete_first(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
            print("First node deleted.")
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next
        print("First node deleted.")

    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
            print("Last node deleted.")
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head
        print("Last node deleted.")

    def count_nodes(self):
        if self.head is None:
            print("Number of nodes: 0")
            return
        count = 0
        temp = self.head
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        print("Number of nodes:", count)

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(HEAD)")

    def traverse(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        print("Traversing the list:", end=" ")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

cll = CircularLinkedList()

while True:
    print("\n----- CIRCULAR LINKED LIST -----")
    print("1. Create")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific position")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display")
    print("10. Traverse")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()

    elif choice == 2:
        cll.insert_beginning()

    elif choice == 3:
        cll.insert_end()

    elif choice == 4:
        cll.insert_position()

    elif choice == 5:
        cll.delete_by_value()

    elif choice == 6:
        cll.delete_first()

    elif choice == 7:
        cll.delete_last()

    elif choice == 8:
        cll.count_nodes()

    elif choice == 9:
        cll.display()

    elif choice == 10:
        cll.traverse()

    elif choice == 11:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")