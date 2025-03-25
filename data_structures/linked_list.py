class _Node:
    def __init__(self):
        self.item = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def add(self, item):
        oldFirst = self.first
        self.first = _Node()
        self.first.item = item
        self.first.next = oldFirst

    def remove(self, item):
        if self.first.item == item:
            self.first = self.first.next
        
        previous = self.first
        next = self.first.next
        while next:
            if next.item == item:
                previous.next = next.next
                break
            previous = next
            next = next.next


    def __iter__(self):
        node = self.first
        while node is not None:
            yield node.item
            node = node.next

if __name__ == '__main__':
    linked_list = LinkedList()
    for x in range(5):
        linked_list.add(x)

    for x in [2, 4]:
        linked_list.remove(x)

    for x in linked_list:
        print(x)

