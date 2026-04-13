class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] proArray = new int[nums.length];
        int left_product=1,right_product;
        for(int i=0;i<nums.length;i++){
            proArray[i] = left_product;
            left_product = left_product*nums[i];
        }
       right_product = 1;
        for(int i=nums.length-1; i >= 0;i--){
            int new_product = proArray[i];
            new_product *= right_product;
            proArray[i] = new_product;
            right_product = right_product*nums[i];
        }
        return proArray;
    }
}  
