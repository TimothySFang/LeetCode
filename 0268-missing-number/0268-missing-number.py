from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_all = 0

        # XOR all expected values: 0..n
        for i in range(n + 1):
            xor_all ^= i

        # XOR with all values in the list
        for num in nums:
            xor_all ^= num

        return xor_all
