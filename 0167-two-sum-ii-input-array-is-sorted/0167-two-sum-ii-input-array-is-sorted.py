class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st, ed = 0, len(numbers) - 1
        while st < ed:

            if numbers[st] + numbers[ed] == target:
                return [st + 1, ed + 1]
            if numbers[st] + numbers[ed] < target:
                st += 1
            elif numbers[st] + numbers[ed] > target:
                ed -= 1