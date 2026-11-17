
import java.util.Arrays;

class Solution {
    public int minimumChanges(String s, int k) {
        int n = s.length();
        int INF = 1000000000;

        int[][] cost = new int[n][n];

        // Step 1: Calculate cost for every substring
        for (int len = 2; len <= n; len++) {
            for (int l = 0; l + len <= n; l++) {

                int best = INF;

                // Try all proper divisors
                for (int d = 1; d < len; d++) {
                    if (len % d != 0) continue;

                    int changes = 0;
                    int groups = len / d;

                    // Each group must be a palindrome
                    for (int r = 0; r < d; r++) {
                        for (int x = 0; x < groups / 2; x++) {

                            int a = l + r + x * d;
                            int b = l + r + (groups - 1 - x) * d;

                            if (s.charAt(a) != s.charAt(b)) {
                                changes++;
                            }
                        }
                    }

                    best = Math.min(best, changes);
                }

                cost[l][l + len - 1] = best;
            }
        }

        // Step 2: Dynamic Programming
        // dp[i][j] = minimum changes for first i chars
        // divided into exactly j semi-palindromes

        int[][] dp = new int[n + 1][k + 1];

        for (int[] row : dp) {
            Arrays.fill(row, INF);
        }

        dp[0][0] = 0;

        for (int j = 1; j <= k; j++) {
            for (int i = 2 * j; i <= n; i++) {

                for (int p = 2 * (j - 1); p <= i - 2; p++) {

                    dp[i][j] = Math.min(
                        dp[i][j],
                        dp[p][j - 1] + cost[p][i - 1]
                    );
                }
            }
        }

        return dp[n][k];
    }
}
