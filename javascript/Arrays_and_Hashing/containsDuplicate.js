/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
    var hash = new Set()

    for (const num of nums){
        if (hash.has(num)){
            return true
        }
        hash.add(num)
    }

    return false
};