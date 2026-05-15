# Subarray with Given Sum

## Difficulty
Medium

## Category
arrays, Prefix Sum

## Reference
Platform: LeetCode

Link: https://leetcode.com/problems/subarray-with-given-sum/

## Problem Description
Given an array of integers and a target sum, find the length of the shortest subarray that sums up to the target sum.

## Expectation
Return the length of the shortest subarray that sums up to the target sum. If no such subarray exists, return -1.

## Constraints
- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
- -10^9 <= targetSum <= 10^9

## Examples

### Example 1
Input: [1, 4, 20, 3, 10, 5]

Output: 2

Explanation: The subarray [4, 20] sums up to 24, which is the target sum.

### Example 2
Input: [1, 1, 1, 1, 1]

Output: 5

Explanation: The subarray [1, 1, 1, 1, 1] sums up to 5, which is the target sum.

### Example 3
Input: [1, 2, 3, 4, 5]

Output: -1

Explanation: No subarray sums up to the target sum.

## Brute Force Approach
Generate all possible subarrays and calculate their sums.

Time Complexity: O(n^2)

Space Complexity: O(1)

## Optimal Solution Intuition
Use the prefix sum technique to efficiently calculate the sum of subarrays.

## Optimal Approach
Calculate the prefix sum array and then use a HashMap to store the prefix sums and their indices.

## Java Solution
```java
import java.util.*;

public class SubarrayWithGivenSum {


         public int shortestSubarray(int[] nums, int targetSum) {
            int n = nums.length;
            int[] prefixSum = new int[n + 1];
            for (int i = 0; i < n; i++) {
               prefixSum[i + 1] = prefixSum[i] + nums[i];
            }
            int minLength = Integer.MAX_VALUE;
            for (int i = 0; i < n; i++) {
               for (int j = i; j < n; j++) {
                  int sum = prefixSum[j + 1] - prefixSum[i];
                  if (sum == targetSum) {
                     minLength = Math.min(minLength, j - i + 1);
                  }
               }
            }
            return minLength == Integer.MAX_VALUE ? -1 : minLength;
         }
      
}
```

Time Complexity: O(n^2)

Space Complexity: O(n)
