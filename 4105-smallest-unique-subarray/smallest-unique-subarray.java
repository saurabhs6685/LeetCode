
import java.util.*;

class Solution {
    public int smallestUniqueSubarray(int[] nums) {
        int n = nums.length;
        int N = n + 1;

        int[] a = new int[N];
        for (int i = 0; i < n; i++) {
            a[i] = nums[i];
        }

        int[] sa = new int[N];
        int[] rank = new int[N];
        int[] temp = new int[N];
        int[] count = new int[Math.max(N, 100001)];

        for (int x : a) {
            count[x]++;
        }

        for (int i = 1; i < count.length; i++) {
            count[i] += count[i - 1];
        }

        for (int i = N - 1; i >= 0; i--) {
            sa[--count[a[i]]] = i;
        }

        int classes = 1;
        rank[sa[0]] = 0;

        for (int i = 1; i < N; i++) {
            if (a[sa[i]] != a[sa[i - 1]]) {
                classes++;
            }
            rank[sa[i]] = classes - 1;
        }

        for (int len = 1; len < N; len <<= 1) {
            for (int i = 0; i < N; i++) {
                temp[i] = sa[i] - len;
                if (temp[i] < 0) {
                    temp[i] += N;
                }
            }

            Arrays.fill(count, 0);

            for (int i = 0; i < N; i++) {
                count[rank[temp[i]]]++;
            }

            for (int i = 1; i < classes; i++) {
                count[i] += count[i - 1];
            }

            for (int i = N - 1; i >= 0; i--) {
                int x = temp[i];
                sa[--count[rank[x]]] = x;
            }

            int[] newRank = new int[N];
            int newClasses = 1;
            newRank[sa[0]] = 0;

            for (int i = 1; i < N; i++) {
                int cur = sa[i];
                int prev = sa[i - 1];

                if (rank[cur] != rank[prev] ||
                    rank[(cur + len) % N] != rank[(prev + len) % N]) {
                    newClasses++;
                }

                newRank[cur] = newClasses - 1;
            }

            rank = newRank;
            classes = newClasses;

            if (classes == N) {
                break;
            }
        }

        int[] pos = new int[N];

        for (int i = 0; i < N; i++) {
            pos[sa[i]] = i;
        }

        int[] lcp = new int[N];
        int h = 0;

        for (int i = 0; i < N; i++) {
            int k = pos[i];

            if (k == 0) {
                continue;
            }

            int j = sa[k - 1];

            while (i + h < N && j + h < N &&
                   a[i + h] == a[j + h]) {
                h++;
            }

            lcp[k] = h;

            if (h > 0) {
                h--;
            }
        }

        int ans = n;

        for (int k = 1; k < N; k++) {
            int i = sa[k];

            if (i == n) {
                continue;
            }

            int longest = Math.max(
                lcp[k],
                k + 1 < N ? lcp[k + 1] : 0
            );

            int len = longest + 1;

            if (len <= n - i) {
                ans = Math.min(ans, len);
            }
        }

        return ans;
    }
}
