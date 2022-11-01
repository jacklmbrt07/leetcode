/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  let n = nums.length;
  const expectedSum = (n * (n + 1)) / 2;
  var actualsum = 0;

  nums.forEach((num) => {
    actualsum += num;
  });

  return expectedSum - actualsum;
};
