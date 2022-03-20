
class hasher:

    def hash(length, input):
        return input % length if input > 0 else -(input % length)

print(hasher.hash(7, 61))

# run time: O(1)
# space complex: O(1)