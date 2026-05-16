# Longest Common Prefix

## Difficulty
Easy-Medium

## Category
Strings, Two Pointers

## Reference
Platform: LeetCode

Link: https://leetcode.com/problems/longest-common-prefix/

## Problem Description
Given an array of strings, find the longest common prefix among all the strings in the array.

## Expectation
Return the longest common prefix as a string.

## Constraints
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.

## Examples

### Example 1
Input: ["flower","flow","flight"]

Output: "fl"

Explanation: The longest common prefix among the three strings is "fl".

### Example 2
Input: ["dog","racecar","car"]

Output: ""

Explanation: There is no common prefix among the three strings.

### Example 3
Input: ["a"]

Output: "a"

Explanation: The longest common prefix among the single string is the string itself.

## Brute Force Approach
Compare each character of the first string with the corresponding character of the other strings.

Time Complexity: O(n * m)

Space Complexity: O(1)

## Optimal Solution Intuition
Use two pointers to compare the characters of the strings.

## Optimal Approach
Compare the characters of the strings from left to right and update the common prefix accordingly.

## Java Solution
```java
import java.util.*;

public class LongestCommonPrefix {

public String longestCommonPrefix(String[] strs) {
    if (strs.length == 0) return "";
    String prefix = strs[0];
    for (int i = 1; i < strs.length; i++) {
        while (strs[i].indexOf(prefix) != 0) {
            prefix = prefix.substring(0, prefix.length() - 1);
            if (prefix.isEmpty()) return "";
        }
    }
    return prefix;
}
}
```

Time Complexity: O(n * m)

Space Complexity: O(1)
