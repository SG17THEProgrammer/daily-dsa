
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
      