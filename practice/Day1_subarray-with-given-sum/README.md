# Subarray with Given Sum

## Difficulty
Medium

## Category
Arrays, Prefix Sum

## Reference
Platform: LeetCode

Link: https://leetcode.com/problems/subarray-with-given-sum/

## Problem Description
Given an array of integers `nums` and an integer `target`, find the number of subarrays that sum up to `target`.

## Expectation
Return the count of subarrays that sum up to `target`.

## Constraints
- 1 <= nums.length <= 10^5
- 1 <= target <= 10^9
- -10^9 <= nums[i] <= 10^9

## Examples

### Example 1
Input: nums = [1, 2, 3], target = 3

Output: 2

Explanation: Subarrays [1, 2] and [3] sum up to 3.

### Example 2
Input: nums = [1, 1, 1], target = 2

Output: 2

Explanation: Subarrays [1, 1] sum up to 2.

### Example 3
Input: nums = [1, 2, 3, 4, 5], target = 5

Output: 2

Explanation: Subarrays [2, 3] and [5] sum up to 5.

## Brute Force Approach
Use two nested loops to generate all possible subarrays and check their sum.

Time Complexity: O(n^2)

Space Complexity: O(1)

## Optimal Solution Intuition
Use a HashMap to store the prefix sum and its frequency.

## Optimal Approach
Iterate through the array and update the prefix sum. Use the HashMap to find the number of subarrays that sum up to the target.

## Java Solution
```java

         public int subarraySum(int[] nums, int target) {
            int count = 0;
            int prefixSum = 0;
            HashMap<Integer, Integer> prefixSumMap = new HashMap<>();
            prefixSumMap.put(0, 1);
            for (int num : nums) {
               prefixSum += num;
               if (prefixSumMap.containsKey(prefixSum - target)) {
                  count += prefixSumMap.get(prefixSum - target);
               }
               prefixSumMap.put(prefixSum, prefixSumMap.getOrDefault(prefixSum, 0) + 1);
            }
            return count;
         }
      
```

Time Complexity: O(n)

Space Complexity: O(n)
