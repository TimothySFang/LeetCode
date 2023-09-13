class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_value = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if (len(self.min_value) > 0):
            self.min_value.append(min(self.min_value[-1], val))
        else:
            self.min_value.append(val)
        self.stack.append(val)
        return

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_value.pop()
        return

    def top(self):
        """
        :rtype: int
        """

        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_value[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()