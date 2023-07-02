class FrontMiddleBackQueue:

    def __init__(self):
        """
        Use 2 queues
        """
        self.left = deque()
        self.right = deque()

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.left) == len(self.right):
            self.right.appendleft(val)
        else:
            self.left.append(val)

    def pushBack(self, val: int) -> None:
        if len(self.left) < len(self.right):
            self.left.append(self.right.popleft())
        self.right.append(val)

    def popFront(self) -> int:
        if not self.right:
            return -1
        if len(self.left) < len(self.right):
            self.left.append(self.right.popleft())
        return self.left.popleft()

    def popMiddle(self) -> int:
        if len(self.left) == len(self.right):
            if self.left:
                return self.left.pop()
            else:
                return -1
        else:
            if self.right:
                return self.right.popleft()
            else:
                return -1

    def popBack(self) -> int:
        if not self.right:
            return -1
        if len(self.left) == len(self.right):
            self.right.appendleft(self.left.pop())
        return self.right.pop()