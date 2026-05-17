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