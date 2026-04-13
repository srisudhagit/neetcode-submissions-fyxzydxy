class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numIndexMap = new HashMap<>();
        int pos=0;
        int[] retarr = new int[2];
        for(int num:nums){
            numIndexMap.put(target-num,pos);
            pos++;
        }

        for(int i=0;i<nums.length;i++){
            if(numIndexMap.containsKey(nums[i])){
               int val = numIndexMap.get(nums[i]);
               if(i != val){
                    retarr[0] = i;
                    retarr[1] = val;
                    return retarr;
               }
            }
        }
        retarr[0] = 0;
        retarr[1] = 0;
        return retarr;
    }
}
