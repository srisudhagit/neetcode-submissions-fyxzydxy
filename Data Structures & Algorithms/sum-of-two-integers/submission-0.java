class Solution {
    public int getSum(int a, int b) {
        while(b != 0){
            // take the carry forward
            int temp = (a & b) << 1;
            // add the number
            a = a ^ b;
            // carry moves to the prev digit
            b = temp;
        }
        return a;
    }
}
