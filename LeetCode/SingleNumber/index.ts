/*
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
*/

function singleNumber(nums: number[]): number {
  const numFrequency: { [key: number]: number } = {};

  for (const num of nums) {
    if (numFrequency[num]) {
      numFrequency[num]++;
    } else {
      numFrequency[num] = 1;
    }
  }

  for (const num in numFrequency) {
    if (numFrequency[num] === 1) {
      return parseInt(num, 10);
    }
  }

  return -1;
}
