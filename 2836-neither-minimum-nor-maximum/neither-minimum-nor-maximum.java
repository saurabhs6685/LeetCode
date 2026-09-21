import java.util.Arrays;

class Solution {
    public int findNonMinOrMax(int[] nums) {
        if (nums.length < 3) {
            return -1;
        }

        // Take only the first 3 distinct elements
        int[] sub = {nums[0], nums[1], nums[2]};
        Arrays.sort(sub);

        // The middle element is neither the minimum nor the maximum
        return sub[1];
    }
}