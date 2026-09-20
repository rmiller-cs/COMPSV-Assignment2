# Represents each customer in the waitlist
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    
    
# Used to manage the waitlist
class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, name):
        node = Node(name)

        node.next = self.head
        self.head = node

    def add_end(self, name):
        node = Node(name)

        if self.head is None:
            self.head = node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def remove(self, name):
        current = self.head

        if current:
            if current.value == name:
                self.head = current.next
                return
        
        while current:
            if current.value == name:
                prev.next = current.next
                return
            prev = current
            current = current.next
        print(name, "is not in the waitlist.")
        
    def print_list(self):
        name = self.head

        if not name:
            return
        else:
            while name:
                print("# -", name.value)
                name = name.next

        print()

    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''


# Interface for managing the waitlist
def waitlist_generator():
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
        
        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)
        
        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)
                
        elif choice == "4":
            print("# Current waitlist:")
            waitlist.print_list()
            
        elif choice == "5":
            print("Exiting waitlist manager.")
            break

        else:
            print("Invalid option. Please choose 1-5.")


# Calls the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200-300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?

The list is made up of individual nodes linked together. Each node references the next node in line.
The list and the nodes that make up the list are represented by two classes.
If someone wants to add to the start of the list, the new data becomes the head of the list.
Otherwise, the method must start from the head and traverse the list to wherever the new data needs to be added.
If something needs to be removed, the method starts from the head until it reaches the node that needs to be removed.
Then, the pointer for the previous node is made to point to the node after the deleted one, removing it from the chain.
The head refers to the start of the linked list, which makes it very important.
Anything that modifies the linked list starts at the head and must traverse the list to where it needs to be.
The benefits from a linked list are that modifying the list takes comparatively less work compared to a normal python list.
For anything that has an unknown size or will need to be modified frequently, a linked list will be beneficial.
'''
