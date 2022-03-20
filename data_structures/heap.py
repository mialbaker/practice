

class heap:
    def __init__(self):
        #self.heap_array = list()
        self.heap_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def print_heap(self):
        for i in self.heap_array:
            print(i)

    def heap_push(self, value):
        self.heap_array.append(value)
        i = len(self.heap_array) - 1
        while i != None and i < len(self.heap_array):
            parent = self.bubble_up(i)
            if self.heap_array[i] < self.heap_array[parent]:
                save = self.heap_array[i]
                self.heap_array[i] = self.heap_array[parent]
                self.heap_array[parent] = save
                i = parent
            else:
                return
        return

    def heap_pop(self):
        if len(self.heap_array) == 0:
            return None
        else:
            i = 0
            while i != None and i < len(self.heap_array):
                i = self.bubble_down(i)
            return self.heap_array.pop(0)

    def bubble_down(self, index):
        # returns index of the smallest child
        if index >= len(self.heap_array):
            return None
        if (2 * index + 1) >= len(self.heap_array):
            return None
        if (2 * index + 2) >= len(self.heap_array):
            return 2 * index + 1
        if self.heap_array[2 * index + 1] <= self.heap_array[2 * index + 2]:
            return 2 * index + 1
        else:
            return 2 * index + 2
       

    def bubble_up(self, index):
        # returns index of the parent
        return index // 2

new_heap = heap()

print(new_heap.bubble_down(0))

test_heap = heap()

print(test_heap.bubble_down(2))

#print(test_heap.heap_pop())

print("**********")

##print(test_heap.print_heap())

print(test_heap.heap_push(6))

print(test_heap.print_heap())



