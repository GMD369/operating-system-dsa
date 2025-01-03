class Node:
    def __init__(self,size,allocated=False, nextAddress = None, task_name = None):
        self.size = size
        self.allocated = allocated
        self.next=nextAddress
        self.task_name = task_name

class LinkedListMemoryManager:
    def __init__(self):
        self.head = None
    
    # initialize memory:
    def initialize_Memory(self, size,block_size):
        for _ in range (size//block_size):
            self.add_block(block_size)
    
    # Add Block:
    def add_block(self, size):
        new_block = Node(size)
        if self.head is None:
            self.head = new_block
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_block
             
    # allocate:
    def allocate(self, size, item):
        current = self.head
        while current:
            if not current.allocated and current.size>= size:
                allocated_block = size
                remaining_size = current.size - allocated_block


                current.allocated = True
                current.size = allocated_block
                current.task_name = item['task_name'] if item else None

                if remaining_size > 0:
                    new_block_of_memory = Node(remaining_size,False,current.next)
                    current.next = new_block_of_memory
                return f"Allocated {size}MB."
            current = current.next
        return "No free block of that size available"
    
    # deallocate:
    def deallocate(self, size):
        current = self.head
        while current:
            if current.allocated and current.size == size:
                
                current.allocated = False

                if current.next and not current.next.allocated:
                    current.size += current.next.size
                    current.next = current.next.next

                if self.head != current:
                    previous = self.head
                    while previous.next != current:
                        previous = previous.next
                    if not previous.allocated:
                        previous.size += current.size
                        previous.next = current.next

                return f"Deallocated {size}MB."
            current = current.next
        return "No block to deallocate"
    
    # Display Memory:
    def display_memory(self):
        # Initialize result list with headers
        result = []
        header = f"{'Size':^10} | {'State':^10} | {'Task Name':^20}"
        divider = "-" * len(header)
        result.append(header)
        result.append(divider)

        # Traverse the memory blocks
        current = self.head
        while current:
            state = "Allocated" if current.allocated else "Free"
            task_name = current.task_name if current.allocated else ""
            result.append(f"{current.size:^10} | {state:^10} | {task_name:<20}")
            current = current.next

        # Join rows with newline for clean table display
        return "\n".join(result)


    

# # Initialize the memory manager
# manager = LinkedListMemoryManager()

# # Add memory blocks
# manager.add_block(50)   # Add a 50MB block
# manager.add_block(100)  # Add a 100MB block
# manager.add_block(200)  # Add a 200MB block

# # Display initial memory state
# print("Initial Memory State:")
# print(manager.display_memory())

# # Allocate memory
# print("\nAllocating 30MB:")
# print(manager.allocate(30))
# print(manager.display_memory())

# # Allocate more memory
# print("\nAllocating 120MB:")
# print(manager.allocate(120))
# print(manager.display_memory())

# # Deallocate memory
# print("\nDeallocating 120MB:")
# print(manager.deallocate(120))
# print(manager.display_memory())

# # Attempt to allocate more than available
# print("\nAllocating 300MB:")
# print(manager.allocate(300))
# print(manager.display_memory())


