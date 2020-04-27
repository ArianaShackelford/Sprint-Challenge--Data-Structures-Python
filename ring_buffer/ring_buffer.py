from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity: # if the length of storage has not met capacity
            self.storage.add_to_head(item) # add the item to the head
            self.current = self.storage.head # set current to head
        elif self.storage.length == self.capacity: #if capacity is met
            self.storage.remove_from_tail() #remove the oldest item in the list
            self.storage.add_to_head(item)#add the new item to the head of the list
            if self.storage.tail == self.current: # if the current location is the tail
                self.current = self.storage.head # set current to head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []   
        # TODO: Your code here
        list_buffer_contents.append(self.current.value) # append current value to list buffer contents
        if self.current.next: # if there is another item after the current item,
            next = self.current.next# next is the next item
        else: # however if there is no item after the current item next is the list head
            next = self.storage.head
        
        while next != self.current:# while next does not equal the current item 
            list_buffer_contents.append(next.value) # append the value of next to the list buffer
            if next.next: # if next.next exists
                next = next.next# set next to next.next
            else:
                next = self.storage.head# else next is the list head
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
