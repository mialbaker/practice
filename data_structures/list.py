
### NODE FOR LIST ###

class list_node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


### DEFINE LIST CLASS ###

# call it list
class list:
# store the head and tail of the list in member variables
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

        # run time: O(1)
        # space complexity: O(1)

# define add_node(value) function
    # every time you add a node, create a new list_node with given value and assign the next/prev members to proper values
    def add_node(self, value):
        if self.head == None:
            new_node = list_node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = list_node(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

        # run time: O(1)
        # space complexity: O(1)


    def print_list(self):
        if self.head == None:
            return
        curr_node = self.head
        while curr_node != self.tail:
            print(curr_node.value)
            curr_node = curr_node.next
        print(self.tail.value)

        # run time: O(n)
        # space complexity: O(1)

    def get_sum(self):
        sum = 0
        curr_node = self.head
        while curr_node != self.tail:
            sum += curr_node.value
            curr_node = curr_node.next
        sum += self.tail.value
        return sum

        # run time: O(n)
        # space complexity: O(1)


    def get_value(self, index):
        curr_node = self.head
        curr_index = 0

        # edge case: [1, 2, 3, 4], index = 3
        # [1, 2], index = 3
        while curr_node != None and curr_index < index:
            curr_node = curr_node.next
            curr_index += 1
        return None if curr_node is None else curr_node.value

        # run time: O(n)
        # space complexity: O(1)
        
    def reverse(self):
        if self.head == None:
            return
        if self.head == self.tail:
            return 
        head = self.head 
        tail = self.tail
        curr_node = self.head
        while curr_node != None:
            next = curr_node.next
            prev = curr_node.prev
            curr_node.prev = curr_node.next
            curr_node.next = prev
            curr_node = next
        self.head = tail
        self.tail = head

        # run time: O(n)
        # space complexity: O(1)
        

a = list()

a.add_node(5)

a.add_node(6)

a.add_node(9)

a.print_list()

print(a.get_sum())

print(a.get_value(0))

print(a.get_value(2))

b = list()

b.add_node(3)

print(b.get_value(0))

print('***********')

a.print_list()

a.reverse()

a.print_list()

print('***********')
c = list()
c.add_node(1)
c.add_node(2)
c.add_node(3)
c.add_node(4)
c.reverse()
c.print_list()

print('***********')
d = list()
d.add_node(11)
d.add_node(21)
d.reverse()
d.print_list()

print('***********')
e = list()
e.reverse()
e.print_list()

# define get_sum() function to sum all values currently in list

# define get(index) function that returns the value of the node at given index (from 0 to n - 1)

# advanced: define reverse() function that reverses the whole list so that the tail is now the head (LC problem)

