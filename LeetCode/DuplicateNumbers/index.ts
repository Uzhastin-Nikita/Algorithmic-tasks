/*Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
*/

const containsDuplicate = (nums: number[]): boolean => {
  const uniqueNumbers = new Set<number>();

  for (const num of nums) {
    if (uniqueNumbers.has(num)) {
      return true;
    }
    uniqueNumbers.add(num);
  }

  return false;
};
