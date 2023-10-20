# Get file input
with open('input.txt') as f:
    input_lines = [line.strip() for line in f.readlines()]

# Part One
directions = {
    'U': (0, 1),
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, -1)
}
tailset = set()
# change nodes to get nodes in linkedlist
num_nodes = 9
class Node:
    def __init__(self, id = 'H') -> None:
        self.id = id
        self.prev = None
        self.curr = [0, 0]
        self.next = None
class DoublyLinkedList:
    def __init__(self, n) -> None:
        i = 0
        self.head = Node()
        ref = self.head
        while i < n:
            prev = self.head
            nxt = Node(i + 1)
            nxt.prev = prev
            self.head.next = nxt
            self.head = self.head.next
            i += 1
        self.head = ref
    def showLLNodes(self):
        ref = self.head
        while self.head:
            print(self.head.id, self.head.prev.id if self.head.prev else '', self.head.next.id if self.head.next else '')
            self.head = self.head.next
        self.head = ref
    def moveHead(self, direction, steps):
        for i in range(steps):
            self.head.curr[0] += directions[direction][0]
            self.head.curr[1] += directions[direction][1]

            ref = self.head
            self.head = self.head.next

            while self.head:
                curr = self.head
                prev = self.head.prev
                x_diff = prev.curr[0] - curr.curr[0]
                y_diff = prev.curr[1] - curr.curr[1]

                if abs(x_diff) > 1 or abs(y_diff) > 1:
                    if x_diff == 0:
                        if y_diff > 0:
                            self.head.curr[1] += 1
                        elif y_diff < 0:
                            self.head.curr[1] -= 1
                    elif y_diff == 0:
                        if x_diff > 0:
                            self.head.curr[0] += 1
                        if x_diff < 0:
                            self.head.curr[0] -= 1
                    elif x_diff > 0:
                        self.head.curr[0] += 1
                        if y_diff > 0:
                            self.head.curr[1] += 1
                        elif y_diff < 0:
                            self.head.curr[1] -= 1
                    elif x_diff < 0:
                        self.head.curr[0] -= 1
                        if y_diff > 0:
                            self.head.curr[1] += 1
                        elif y_diff < 0:
                            self.head.curr[1] -= 1
                if self.head.id == num_nodes:
                    tailset.add((self.head.curr[0], self.head.curr[1]))

                self.head = self.head.next
            self.head = ref

dll = DoublyLinkedList(num_nodes)

for line in input_lines:
    direction, steps = line.split(' ')
    dll.moveHead(direction, int(steps))

# print(tailset)
print(len(tailset)) # Part One Answer: 5874, Part Two Answer: 2467