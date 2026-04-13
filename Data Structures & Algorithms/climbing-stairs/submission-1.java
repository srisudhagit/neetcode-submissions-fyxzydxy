class Solution {
    public int climbStairs(int n) {
        int[] countNoOfWays = new int[n+1];
        countNoOfWays[0] = 0;
        countNoOfWays[1] = 1;
        if(n >=2 ){
            countNoOfWays[2] = 2;
        }
        for(int i=3;i<=n;i++){
            countNoOfWays[i] = countNoOfWays[i-1]+countNoOfWays[i-2];
        }
        return countNoOfWays[n];
    }
}
