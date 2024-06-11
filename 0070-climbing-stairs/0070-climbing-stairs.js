/**
 * @param {number} n
 * @return {number}
 */

var stairsHelper = function(n, memo) {
    if (n in memo) {
        return memo[n];
    }
    memo[n] = stairsHelper(n - 1, memo) + stairsHelper(n - 2, memo);
    return memo[n];
}

var climbStairs = function(n) {
    let memo = {};
    memo[0] = 0;
    memo[1] = 1;
    memo[2] = 2;
    return stairsHelper(n, memo);
};