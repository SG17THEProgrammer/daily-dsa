
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
      