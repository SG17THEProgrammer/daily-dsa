
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
      