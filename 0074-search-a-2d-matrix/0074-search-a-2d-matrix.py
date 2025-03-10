class Solution:
    def binMatSearch(self, matrix: List[List[int]], target: int, left: int, right: int) -> int:
        if right < left or matrix[left][0] > target or matrix[right][-1] < target:
            return -1
        middle = left + ((right - left) // 2)
        if (matrix[middle][0] <= target <= matrix[middle][-1]):
            return middle
        elif (matrix[middle][0] > target):
            # search left
            return self.binMatSearch(matrix, target, left, middle - 1)
        else: 
            return self.binMatSearch(matrix, target, middle + 1, right)
    
    def binSearch(self, array: List[int], target: int, left: int, right: int) -> bool:
        if right < left:
            return False
        middle = left + ((right - left) // 2)

        if (array[middle] == target):
            return True
        elif (array[middle] < target):
            return self.binSearch(array, target, middle + 1, right)
        else:
            return self.binSearch(array, target, left, middle - 1)



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_ind = self.binMatSearch(matrix, target, 0, len(matrix) - 1)
        return self.binSearch(matrix[matrix_ind], target, 0, len(matrix[matrix_ind]) - 1)