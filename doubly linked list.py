class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def create(self):
        n=int(input("enter the number of nodes"))
        for i in range(n):
            data = int(input(f"enter data for node{i+1}:"))
            new_node= Node(data)
            if self.head is None:
                self.head=new_node
            else:
                temp = self.head

                while temp.next is not None:
                    temp = temp.next
                temp.next= new_node
                new_node.prev=temp

        print("doubly linked list created successfully")

    def insert_beginning(self):
        data = int(input("enter the data:"))
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head = new_node
        print("node inserted at beginning")
        
    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print("Node inserted at end.")

    def insert_position(self):
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))
        new_node = Node(data)
        if pos == 1:
            if self.head is not None:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            print("Node inserted at position", pos)
            return
        temp = self.head
        for i in range(1, pos - 1):
            if temp is None:
                print("Invalid position.")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position.")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        print("Node inserted at position", pos)

    def delete_by_value(self):
        value = int(input("Enter value to delete: "))
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp is not None and temp.data != value:
            temp = temp.next
        if temp is None:
            print("Value not found.")
            return
        if temp == self.head:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
        else:
            temp.prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = temp.prev
        print("Node deleted.")
        
    def delete_first(self):
        if self.head is None:
            print("List is empty.")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        print("First node deleted.")

    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        if temp.next is None:
            self.head = None
            print("Last node deleted.")
            return
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None
        print("Last node deleted.")

    def count_nodes(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        print("Number of nodes:", count)

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        print("Doubly Linked List:", end=" ")
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")

    def traverse(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        print("Forward Traversal:", end=" ")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

dll=DoublyLinkedList()
while True:
    print("\n----- DOUBLY LINKED LIST -----")
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
        dll.create()

    elif choice == 2:
        dll.insert_beginning()

    elif choice == 3:
        dll.insert_end()

    elif choice == 4:
        dll.insert_position()

    elif choice == 5:
        dll.delete_by_value()

    elif choice == 6:
        dll.delete_first()

    elif choice == 7:
        dll.delete_last()

    elif choice == 8:
        dll.count_nodes()

    elif choice == 9:
        dll.display()

    elif choice == 10:
        dll.traverse()

    elif choice == 11:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")


