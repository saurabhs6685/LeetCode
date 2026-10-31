
class Solution {
    public int uniquePaths(int[][] grid) {
        int MOD = 1_000_000_007;
        int n = grid[0].length;

        long[] dp = new long[n + 1];

        // Starting position
        dp[1] = 1;

        for (int[] row : grid) {
            long left = 0;

            for (int j = 0; j < n; j++) {
                if (row[j] == 0) {
                    // Empty cell
                    long ways = (dp[j + 1] + left) % MOD;

                    dp[j + 1] = ways;
                    left = ways;

                } else {
                    // Mirror cell: swap directions
                    long temp = dp[j + 1];

                    dp[j + 1] = left;
                    left = temp;
                }
            }
        }

        return (int) dp[n];
    }
}
