class set:

    def __init__(self):
        self.arr = [[], [], [], [], [], [], []]

    def hash(self, length, input):
        return input % length if input > 0 else -(input % length)
    
    def add(self, num):
        i = self.hash(len(self.arr), num)
        if num not in self.arr[i]:
            self.arr[i].append(num)
        return

    # run time: O(1)
    # space complex O(1)

    def remove(self, num):
        i = self.hash(len(self.arr), num)
        if num not in self.arr[i]:
            self.arr[i].pop(num)
        return

    # run time: O(1)
    # space complex O(1)

    def contains(self, num):
        i = self.hash(len(self.arr), num)
        return self.arr[i] == num

    # run time: O(1)
    # space complex O(1)

new_set = set()

new_set.add(5)

new_set.add(5)

new_set.add(1)

new_set.contains(1)

new_set.remove(1)