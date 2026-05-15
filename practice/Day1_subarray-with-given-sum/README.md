# Subarray with Given Sum

## Difficulty
Medium

## Category
Arrays, Prefix Sum

## Reference
Platform: LeetCode

Link: https://leetcode.com/problems/subarray-sum-equals-k/

## Problem Description
Given an array of integers and an integer k, find the number of contiguous subarrays where the sum of the elements in the subarray is equal to k.

## Expectation
Return the count of such subarrays.

## Constraints
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

## Examples

### Example 1
Input: nums = [1,1,1], k = 2

Output: 2

Explanation: The subarrays are [1,1] and [1,1].

### Example 2
Input: nums = [1,2,3], k = 3

Output: 2

Explanation: The subarrays are [1,2] and [3].

### Example 3
Input: nums = [1,-1,0], k = 0

Output: 3

Explanation: The subarrays are [1,-1], [-1,0], and [0].

## Brute Force Approach
Use two nested loops to generate all possible subarrays and check if their sum is equal to k.

Time Complexity: O(n^2)

Space Complexity: O(1)

## Optimal Solution Intuition
Use a HashMap to store the prefix sums and their frequencies.

## Optimal Approach
Iterate through the array, calculate the prefix sum, and check if the difference between the current prefix sum and k exists in the HashMap.

## Java Solution
```java
import java.util.*;

public class SubarrayWithGivenSum {


      public int subarraySum(int[] nums, int k) {
         int count = 0;
         int sum = 0;
         HashMap<Integer, Integer> prefixSumCount = new HashMap<>();
         prefixSumCount.put(0, 1);
         for (int num : nums) {
            sum += num;
            count += prefixSumCount.getOrDefault(sum - k, 0);
            prefixSumCount.put(sum, prefixSumCount.getOrDefault(sum, 0) + 1);
         }
         return count;
      }
}
```

Time Complexity: O(n)

Space Complexity: O(n)
