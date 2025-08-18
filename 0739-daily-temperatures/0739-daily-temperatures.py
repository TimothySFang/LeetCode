class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        for index in range(len(temperatures)):
            while len(stack) != 0 and stack[-1][0] < temperatures[index]:
                temp = stack.pop()
                temperatures[temp[1]] = index - temp[1] 
            stack.append((temperatures[index], index))

        while len(stack) != 0:
            temp = stack.pop()
            temperatures[temp[1]] = 0

        return temperatures