class Solution:
    def findMin(self, nums: List[int]) -> int:


        def custom_binsearch(nums, start, end):
            middle = ((end - start) // 2) + start
            middle_val, start_val, end_val = nums[middle], nums[start], nums[end]

            # print(start_val, end_val, middle_val)
            if end_val < start_val and middle_val < start_val:
                # either search left or return, idk yet
                return custom_binsearch(nums, start, middle)
            elif end_val < start_val and middle_val >= start_val:
                # search right
                return custom_binsearch(nums, middle + 1, end)
            else:
                return start_val

        return custom_binsearch(nums, 0, len(nums) - 1)