class Solution {
    public int findMin(int[] nums) {
        int len = nums.length;
        int mid, low = 0, high = len-1;
        while(low <= high){
            if(nums[low] <= nums[high]){
                return nums[low];
            }
            mid = (low+high)/2;
            if(nums[low] <= nums[mid]){
                low = mid+1;
            }else{
                high = mid;
            }
        }
        return -1;
    }
}
