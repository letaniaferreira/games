class Queue(object):

    def __init__(self):

        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def __repr__ (self):
        return self.items



class Deque(object):
    def __init__(self):

        self.items = []

    def addFront(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def addRear(self, item):
        return self.items.append(item)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items ==[]
