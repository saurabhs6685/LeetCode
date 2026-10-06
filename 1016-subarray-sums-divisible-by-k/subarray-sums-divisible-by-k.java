class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int[] remainder = new int[k];
        remainder[0] = 1;

        int sum = 0;
        int answer = 0;

        for (int num : nums) {
            sum += num;

            int rem = sum % k;

            if (rem < 0) {
                rem += k;
            }

            answer += remainder[rem];
            remainder[rem]++;
        }

        return answer;
    }
}