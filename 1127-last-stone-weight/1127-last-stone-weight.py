class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            s1, i1 = 0, 0
            s2, i2 = 0, 0
            for i, st in enumerate(stones):
                if st >= s1:
                    s2 = s1
                    i2 = i1
                    s1 = st
                    i1 = i
                elif st > s2:
                    s2 = st
                    i2 = i
            
            if s1 - s2 == 0:
                stones.pop(i1)
                stones.pop(i2)
            else:
                stones[i1] = s1 - s2
                stones.pop(i2)
    
        if len(stones) == 1:
            return stones[0] 
        else:
            return 0