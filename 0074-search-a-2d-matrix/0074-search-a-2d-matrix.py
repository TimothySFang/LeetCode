class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums, left, right):
            middle = (left + right) // 2
            if left > right:
                return False
            if nums[middle] == target:
                return True
            elif target < nums[middle]:
                # search left
                return binarySearch(nums, left, middle - 1)
            elif target > nums[middle]:
                return binarySearch(nums, middle + 1, right)

        def binSearchRow(mat):
            if not mat:
                return False
            middle = (len(mat) - 1) // 2
            if target >= mat[middle][0] and target <= mat[middle][-1]:
                #found it
                return binarySearch(mat[middle], 0, len(mat[middle]) - 1)
            elif target < mat[middle][0]:
                # search left
                return binSearchRow(mat[: middle])
            elif target > mat[middle][-1]:
                # search right
                return binSearchRow(mat[middle + 1 :])
            
        return binSearchRow(matrix)