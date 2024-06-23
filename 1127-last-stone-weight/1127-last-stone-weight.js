/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    while (stones.length > 1) {
        stones.sort((a, b) => a - b);
        if (stones[stones.length - 1] === stones[stones.length - 2]) {
            stones.pop();
            stones.pop();
        } else {
            stones[stones.length - 2] = stones[stones.length - 1] - stones[stones.length - 2];
            stones.pop();
        }
    }
    if (stones.length === 1) {
        return stones[0];
    } if (stones.length === 0) {
        return 0
    }
    
};