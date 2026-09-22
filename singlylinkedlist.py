class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlyLinkedList:
    def __init__(self):
        self.head=None

    def create(self):
        n=int(input("enter number of nodes:"))
        for i in range(n):
            data = int(input(f"enter data for node {i+1}:"))
            new_node=Node(data)
            if self.head is None:
                self.head=new_node
            else:
                temp=self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next=new_node
        print("linked list is created successfully:")

    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        print("Node inserted at beginning.")


    def insert_end(self):
        data= int(input("enter data:"))
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
        print("Node inserted at end.")

    def insert_position(self):
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))

        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            print("Node inserted.")
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
        temp.next = new_node

        print("Node inserted at position", pos)

    def delete_last(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            self.head = None
            print("Last node deleted.")
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None
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

        print("Linked List:", end=" ")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("NULL")

    def traverse(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        print("Traversing the list:")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()


sll = singlyLinkedList()

while True:
    print("\n----- SINGLY LINKED LIST -----")
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
        sll.create()

    elif choice == 2:
        sll.insert_beginning()

    elif choice == 3:
        sll.insert_end()

    elif choice == 4:
        sll.insert_position()

    elif choice == 5:
        sll.delete_by_value()

    elif choice == 6:
        sll.delete_first()

    elif choice == 7:
        sll.delete_last()

    elif choice == 8:
        sll.count_nodes()

    elif choice == 9:
        sll.display()

    elif choice == 10:
        sll.traverse()

    elif choice == 11:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
