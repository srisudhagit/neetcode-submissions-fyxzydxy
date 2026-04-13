class Solution {
    public int missingNumber(int[] nums) {
        int len = nums.length;
        int xor_array=0, xor_nums=0;
        for(int i=0;i<len;i++){
            xor_array ^= nums[i];
        }
        for(int i=1;i<=len;i++){
            xor_nums ^= i;
        }
        return xor_nums^xor_array;
    }
}
