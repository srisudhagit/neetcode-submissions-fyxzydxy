class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] ret = new int[2];
        int ptr1=0, ptr2=numbers.length-1;
        while(ptr1 < ptr2){
            int sum = numbers[ptr1]+numbers[ptr2];
            if(sum == target){
                ret[0] = ptr1+1;
                ret[1] = ptr2+1;
                return ret;
            }else if(sum < target){
                ptr1++;
            }else{
                ptr2--;
            }
        }
        return ret;
    }
}
