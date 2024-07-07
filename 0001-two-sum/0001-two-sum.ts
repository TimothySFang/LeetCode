function twoSum(nums: number[], target: number): number[] {
    type Dictionary = {
        [key:number]:number;
    }

    let myDictionary: Dictionary = {};
    
    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i]
        if (complement in myDictionary) {
            return [i, myDictionary[complement]];
        } else {
            myDictionary[nums[i]] = i;
        }
    }
};