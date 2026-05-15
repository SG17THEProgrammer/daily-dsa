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