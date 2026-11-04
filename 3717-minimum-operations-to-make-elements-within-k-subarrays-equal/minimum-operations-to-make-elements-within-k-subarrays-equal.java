import java.util.*;

class Solution {
    public long minOperations(int[] nums, int x, int k) {
        int n = nums.length;

        TreeMap<Integer, Integer> left = new TreeMap<>();
        TreeMap<Integer, Integer> right = new TreeMap<>();

        long leftSum = 0, rightSum = 0;
        int leftSize = 0, rightSize = 0;

        long[] cost = new long[n - x + 1];

        // Calculate cost for every window
        for (int i = 0; i < n; i++) {
            int val = nums[i];

            if (left.isEmpty() || val <= left.lastKey()) {
                left.merge(val, 1, Integer::sum);
                leftSum += val;
                leftSize++;
            } else {
                right.merge(val, 1, Integer::sum);
                rightSum += val;
                rightSize++;
            }

            // Balance the two halves
            while (leftSize > rightSize + 1) {
                int v = left.lastKey();
                remove(left, v);

                leftSum -= v;
                leftSize--;

                right.merge(v, 1, Integer::sum);
                rightSum += v;
                rightSize++;
            }

            while (leftSize < rightSize) {
                int v = right.firstKey();
                remove(right, v);

                rightSum -= v;
                rightSize--;

                left.merge(v, 1, Integer::sum);
                leftSum += v;
                leftSize++;
            }

            // Remove the element outside the window
            if (i >= x) {
                int out = nums[i - x];

                if (left.containsKey(out)) {
                    remove(left, out);
                    leftSum -= out;
                    leftSize--;
                } else {
                    remove(right, out);
                    rightSum -= out;
                    rightSize--;
                }

                while (leftSize > rightSize + 1) {
                    int v = left.lastKey();
                    remove(left, v);
                    leftSum -= v;
                    leftSize--;

                    right.merge(v, 1, Integer::sum);
                    rightSum += v;
                    rightSize++;
                }

                while (leftSize < rightSize) {
                    int v = right.firstKey();
                    remove(right, v);
                    rightSum -= v;
                    rightSize--;

                    left.merge(v, 1, Integer::sum);
                    leftSum += v;
                    leftSize++;
                }
            }

            if (i >= x - 1) {
                long median = left.lastKey();

                cost[i - x + 1] =
                    median * leftSize - leftSum
                    + rightSum - median * rightSize;
            }
        }

        // DP for selecting k non-overlapping windows
        long INF = Long.MAX_VALUE / 4;

        long[][] dp = new long[k + 1][n + 1];

        for (int j = 1; j <= k; j++) {
            Arrays.fill(dp[j], INF);
        }

        for (int i = 1; i <= n; i++) {
            dp[0][i] = 0;
        }

        for (int j = 1; j <= k; j++) {
            for (int i = 1; i <= n; i++) {

                // Skip current element
                dp[j][i] = dp[j][i - 1];

                // Select window ending at i - 1
                if (i >= x && dp[j - 1][i - x] != INF) {
                    dp[j][i] = Math.min(
                        dp[j][i],
                        dp[j - 1][i - x] + cost[i - x]
                    );
                }
            }
        }

        return dp[k][n];
    }

    private void remove(TreeMap<Integer, Integer> map, int val) {
        int count = map.get(val);

        if (count == 1) {
            map.remove(val);
        } else {
            map.put(val, count - 1);
        }
    }
}