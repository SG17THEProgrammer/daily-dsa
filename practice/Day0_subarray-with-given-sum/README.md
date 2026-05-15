# Subarray with Given Sum

## Difficulty
Medium

## Category
Arrays, Prefix Sum

## Reference
Platform: LeetCode

Link: https://leetcode.com/problems/subarray-with-given-sum/

## Problem Description
Given an array of integers and a target sum, find the number of subarrays that sum up to the target.

## Expectation
Write a function that returns the number of subarrays with the given sum.

## Constraints
- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
- -10^5 <= targetSum <= 10^5

## Examples

### Example 1
Input: nums = [1, 2, 3, 4, 5], targetSum = 5

Output: 2

Explanation: Subarrays [2, 3] and [5] sum up to 5.

### Example 2
Input: nums = [10, 2, -2, -20, 10], targetSum = -10

Output: 3

Explanation: Subarrays [10, 2, -2, -20], [2, -2, -20, 10], and [-2, -20, 10] sum up to -10.

### Example 3
Input: nums = [1, 1, 1, 1, 1], targetSum = 3

Output: 3

Explanation: Subarrays [1, 1, 1], [1, 1, 1], and [1, 1, 1] sum up to 3.

## Brute Force Approach
Generate all possible subarrays and check if their sum equals the target sum.

Time Complexity: O(n^3)

Space Complexity: O(1)

## Optimal Solution Intuition
Use a prefix sum array to store the cumulative sum of the array elements, then iterate over the array and use a hashmap to store the frequency of each prefix sum.

## Optimal Approach
Use the prefix sum array and hashmap to find the number of subarrays with the given sum.

## Java Solution
```java
import java.util.*;

public class SubarrayWithGivenSum {


      public int subarraySum(int[] nums, int targetSum) {
         int count = 0;
         int[] prefixSum = new int[nums.length + 1];
         HashMap<Integer, Integer> map = new HashMap<>();

         map.put(0, 1);
         prefixSum[0] = 0;

         for (int i = 1; i <= nums.length; i++) {
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1];
            if (map.containsKey(prefixSum[i] - targetSum)) {
               count += map.get(prefixSum[i] - targetSum);
            }
            map.put(prefixSum[i], map.getOrDefault(prefixSum[i], 0) + 1);
         }

         return count;
      }
      
}
```

Time Complexity: O(n)

Space Complexity: O(n)
