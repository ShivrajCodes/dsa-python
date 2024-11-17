class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Delete from the beginning
    def delete_from_beginning(self):
        if not self.head:
            print("List is empty. Nothing to delete.")
            return
        self.head = self.head.next

    # Delete from the end
    def delete_from_end(self):
        if not self.head:
            print("List is empty. Nothing to delete.")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next and temp.next.next:
            temp = temp.next
        temp.next = None

    # Delete from any position
    def delete_from_any(self, position):
        if not self.head:
            print("List is empty. Nothing to delete.")
            return
        if position <= 0:
            print("Invalid position.")
            return
        if position == 1:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(position - 2):
            if not temp.next:
                print("Position out of bounds.")
                return
            temp = temp.next
        if not temp.next:
            print("Position out of bounds.")
            return
        temp.next = temp.next.next

    # Count the number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # Display the list
    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Separate odd and even nodes
    def separate_odd_even(self):
        if not self.head:
            print("List is empty.")
            return
        odd_list = []
        even_list = []
        temp = self.head
        while temp:
            if temp.data % 2 == 0:
                even_list.append(temp.data)
            else:
                odd_list.append(temp.data)
            temp = temp.next
        print("Odd nodes:", odd_list)
        print("Even nodes:", even_list)

# Menu-driven program
def main():
    linked_list = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Insert at the beginning")
        print("2. Insert at the end")
        print("3. Delete from the beginning")
        print("4. Delete from the end")
        print("5. Delete from any position")
        print("6. Display the list")
        print("7. Count the number of nodes")
        print("8. Separate odd and even nodes")
        print("9. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter the data to insert: "))
            linked_list.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter the data to insert: "))
            linked_list.insert_at_end(data)
        elif choice == 3:
            linked_list.delete_from_beginning()
        elif choice == 4:
            linked_list.delete_from_end()
        elif choice == 5:
            position = int(input("Enter the position to delete: "))
            linked_list.delete_from_any(position)
        elif choice == 6:
            linked_list.display()
        elif choice == 7:
            print("Number of nodes:", linked_list.count_nodes())
        elif choice == 8:
            linked_list.separate_odd_even()
        elif choice == 9:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
