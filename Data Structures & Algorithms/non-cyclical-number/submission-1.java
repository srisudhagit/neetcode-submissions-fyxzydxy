class Solution {
    public boolean isHappy(int n) {
            int sum=0,temp=n,rem;
            List<Integer> values = new ArrayList<>();
            while(true){
                sum = 0;
                while(temp > 0){
                    rem = temp%10;
                    temp = temp/10;
                    sum += rem*rem;
                }
                 if(sum == 1){
                    return true;
                }else{
                    if(values.contains(sum)){
                        return false;
                    }
                    values.add(sum);
                    temp = sum;
                }
                System.out.println(sum);
            }
        }
}
