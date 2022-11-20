class FifoPriorityQueue:
    """
    I need to do this because the Python implementation of the PQ uses a heap, which doesn't maintain the order of
    elements with the same priority
    """
    def __init__(self):
        self.queue = [] # list of tuples of format (priority, item)

    def put(self, priority, item):
        n = len(self.queue)

        for i in range(0, n):
            if priority < self.queue[i][0]:
                self.queue.insert(i, (priority, item))
                return

        self.queue.append((priority, item))

    def get(self):
        return self.queue.pop(0)[1]

    def is_empty(self):
        return len(self.queue) == 0
