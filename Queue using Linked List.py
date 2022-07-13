class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.Head = None
        self.Last = None

    def enqueue(self, data):
        if self.Last is None:
            self.Head = Node(data)
            self.Last = self.head
        else:
            self.Last.next = Node(data)
            self.Last = self.Last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.Head.data
            self.Head = self.Head.next
            return to_return


b_queue = Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'enqueue':
        b_queue.enqueue(int(do[1]))
    elif operation == 'dequeue':
        dequeued = b_queue.dequeue()
        if dequeued is None:
            print('Queue is empty.')
        else:
            print('Dequeued element: ', int(dequeued))
    elif operation == 'quit':
        break




