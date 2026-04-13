class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> resultSet = new HashSet<List<Integer>>();
        List<List<Integer>> resultList = new ArrayList<List<Integer>>();

        Arrays.sort(nums);
        for(int i=0;i<nums.length-2;i++){
            int left = i+1;
            int right = nums.length-1;
            while(left < right){
                List<Integer> output = new ArrayList<>();
                int finalsum = nums[i] + nums[left] + nums[right];
                if(finalsum == 0){
                    output.add(nums[i]);
                    output.add(nums[left]);
                    output.add(nums[right]);
                    resultSet.add(output);
                   // output.clear();
                    System.out.println(nums[i]+" "+nums[left]+" "+nums[right]+" "+finalsum);
                    left++;
                    right--;
                }else if(finalsum > 0){
                    right--;
                }else{
                    left++;
                }
            }
        }
        resultList.addAll(resultSet);
        return resultList;
    }
}
