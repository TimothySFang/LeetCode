class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  
        # 999 + 1 = 1000
        # 9 + 1 = 10
        for i in range(len(digits) - 1, -1, -1):
            print(i)
            if digits[i] < 9:
                digits[i] += 1
                break
            elif i == 0:
                digits[i] = 0
                digits.insert(0, 1)
                break
            else: 
                digits[i] = 0

        return digits