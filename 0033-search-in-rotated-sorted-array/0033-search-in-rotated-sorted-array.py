class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def customBinSearch(start, end):
            middle = ((end - start) // 2) + start
            curr = nums[middle]

            if curr == target:
                return middle
            if end <= start:
                return -1

            if nums[start] <= curr:
                if nums[start] <= target < curr:
                    return customBinSearch(start, middle - 1)
                else:
                    return customBinSearch(middle + 1, end)
            else:
                # right is sorted (middle is in the sorted section)
                if curr < target <= nums[end]:
                    return customBinSearch(middle + 1, end)
                else:
                    return customBinSearch(start, middle - 1)

        return customBinSearch(0, len(nums) - 1)

