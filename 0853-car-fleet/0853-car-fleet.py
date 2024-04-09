class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_to_target = [(target - p) / s for p, s in zip(position, speed)]
        cars = sorted(zip(position, time_to_target), key=lambda x: x[0], reverse=True)
        stack = []
        
        for pos, time in cars:
            if not stack:
                stack.append(time)
            elif time > stack[-1]:  # If the current car is slower than the last in stack
                stack.append(time)
        
        return len(stack)  # The stack length is the number of fleets