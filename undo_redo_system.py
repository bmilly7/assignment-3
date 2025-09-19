# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None


    def push(self,data):
        new_action = Node(data)

        if not self.top:
            self.top = new_action
        else:
            new_action.next = self.top
            self.top = new_action

    def pop(self):
        if not self.top:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            return popped_node.data

    def print_stack(self):
        current = self.top
        if not current:
            print("stack is empty")
        else:
            while current:
                print(f'{current.data}')
                current = current.next








def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action)
            redo_stack = Stack()


            print(f"Action performed: {action}")
        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            popped = undo_stack.pop()
            if popped:
                redo_stack.push(popped)
                print(f"Undid action: {popped}")
            else:
                print("nothing to undo")
            

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            popped = redo_stack.pop()
            if popped:
                undo_stack.push(popped)
                print(f"redid action: {popped}")
            else:
                print("nothing to redo.")


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()




'''
Why is a stack the right choice for undo/redo?
Why is a queue better suited for the help desk?
How do your implementations differ from Python’s built-in lists?
Be sure to review Resource #3: When to Use a Stack or a Queue to help in answering these questions!


A stack is the right choice for undo/redo when you the most recent action needs to be handled first. For example for undo/redo
you are usually undoing or redoing the last action that you completed. This would make a stack useful because it follows the last in first
out principle. 

The queue is better suited for the help desk because in this situation fairness matters. The customers are treated first come first handled.
This meaning that the first in first out princilple is needed. 

From my understanding, using a linked list version of a stack or queue can be a lot faster than using a built in python list or array. 
This is because of how it handles memory. When removing items from a built in python list, the other elements in the list will need to be shifted.
Python list are generally fast for end operations and also random access since elements can be accessed by index



'''