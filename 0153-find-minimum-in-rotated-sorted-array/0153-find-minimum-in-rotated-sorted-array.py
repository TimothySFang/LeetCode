from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        def custom_binsearch(nums, start, end):
            # If current window is already sorted, the start is the min
            if nums[start] <= nums[end]:
                return nums[start]
            # If narrowed to one element, return it
            if start == end:
                return nums[start]

            mid = start + (end - start) // 2
            start_val, mid_val = nums[start], nums[mid]

            if mid_val >= start_val:
                # Left half [start..mid] is sorted -> min is in right half
                return custom_binsearch(nums, mid + 1, end)
            else:
                # Pivot/min is in left half (including mid)
                return custom_binsearch(nums, start, mid)

        return custom_binsearch(nums, 0, len(nums) - 1)
