class Solution:
    def binSearch(self, nums: List[int], left: int, right: int, target: int) -> int:
        if left > right:
            return -1
        middle = ((left + right) // 2)
        if target == nums[middle]:
            return middle
        elif nums[middle] < target:
            return self.binSearch(nums, middle + 1, right, target)
        else:
            return self.binSearch(nums, left, middle - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums, 0, len(nums) - 1, target)
        
