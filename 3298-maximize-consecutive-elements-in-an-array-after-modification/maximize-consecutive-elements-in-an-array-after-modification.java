
import java.util.*;

class Solution {
    public int maxSelectedElements(int[] nums) {
        Arrays.sort(nums);

        Map<Integer, Integer> dp = new HashMap<>();

        int ans = 0;

        for (int x : nums) {

            int prev = dp.getOrDefault(x - 1, 0);
            int curr = dp.getOrDefault(x, 0);

            dp.put(x + 1, Math.max(
                dp.getOrDefault(x + 1, 0),
                curr + 1
            ));

            dp.put(x, Math.max(curr, prev + 1));

            ans = Math.max(ans, Math.max(curr + 1, prev + 1));
        }

        return ans;
    }
}
