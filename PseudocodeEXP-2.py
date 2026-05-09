# Stack
create Stack class
    initialize items as empty list
    
    define is_empty() method
        return length of items is 0
        
    define push(item) method
        append item to items
        
    define pop() method
        if is_empty() is False
            return and remove last item from items
        else
            raise IndexError
            
    define peek() method
        if is_empty() is False
            return last item in items
        else
            raise IndexError
            
    define size() method
        return length of items

# Queue
create Queue class
    initialize items as empty deque
    
    define is_empty() method
        return length of items is 0
        
    define enqueue(item) method
        append item to items
        
    define dequeue() method
        if is_empty() is False
            return and remove first item from items
        else
            raise IndexError
            
    define size() method
        return length of items
        
# Linked List 
create Node class
    initialize data and next pointer
    
create LinkedList class
    initialize head as None
    
    define is_empty() method
        return head is None
        
    define append(data) method
        create new node with data
        if is_empty()
            set head to new node
        else
            traverse to last node and set next to new node
            
    define display() method
        initialize empty list
        traverse linked list from head
            append data to list
        print linked list
        
# Testing
create and use instances of Stack, Queue, and LinkedList
