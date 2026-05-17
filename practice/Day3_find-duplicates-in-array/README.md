# Find Duplicates in Array

## Difficulty
Easy-Medium

## Category
Arrays, HashMaps

## Reference
Platform: LeetCode

Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/

## Problem Description
Given an array of integers, find all the elements that appear more than once in the array.

## Expectation
Return a list of all the elements that appear more than once in the array.

## Constraints
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5

## Examples

### Example 1
Input: [4,3,2,7,8,2,3,1]

Output: [2,3]

Explanation: The elements 2 and 3 appear more than once in the array.

### Example 2
Input: [1,2,3,4,5]

Output: []

Explanation: There are no duplicates in the array.

### Example 3
Input: [1,1,1,1,1]

Output: [1]

Explanation: The element 1 appears more than once in the array.

## Brute Force Approach
Compare each element with every other element in the array.

Time Complexity: O(n^2)

Space Complexity: O(1)

## Optimal Solution Intuition
Use a HashMap to store the frequency of each element in the array.

## Optimal Approach
Iterate over the array and store the frequency of each element in the HashMap. Then, iterate over the HashMap and add the elements with frequency greater than 1 to the result list.

## Java Solution
```java
import java.util.*;

public class FindDuplicatesInArray {


         import java.util.*;

         public class Solution {
            public List<Integer> findDuplicates(int[] nums) {
               List<Integer> result = new ArrayList<>();
               HashMap<Integer, Integer> frequencyMap = new HashMap<>();

               for (int num : nums) {
                  frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
               }

               for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
                  if (entry.getValue() > 1) {
                     result.add(entry.getKey());
                  }
               }

               return result;
            }
         }
      
}
```

Time Complexity: O(n)

Space Complexity: O(n)
