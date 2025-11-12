class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos_count = neg_count = curr_max = nums[0]

        for n in nums[1:]:
            if n < 0:
                # temp = neg_count
                # neg_count = pos_count
                # pos_count = temp
                pos_count, neg_count = neg_count, pos_count
            pos_count = max(n, pos_count * n)
            neg_count = min(n, neg_count * n)
            curr_max = max(pos_count, curr_max)
        return curr_max