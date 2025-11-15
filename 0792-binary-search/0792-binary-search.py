class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # middle = left + (right - left) // 2
            # For capped int languages like Java
            middle = (left + right) // 2


            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                left = middle + 1

            elif nums[middle] > target:
                right = middle - 1
        return -1