class Solution {
    public int maxProfit(int[] prices) {
       int profit=0,maxprofit=0,start=0,end=0;
       for(int i=1;i<prices.length;i++){
         profit = prices[i]-prices[start];
         if(profit < 0){
            int temp = end+1;
            start = temp;
            end = start;
         }else{
            end++;
            if(profit > maxprofit){
               maxprofit = profit;
            }
         }
         System.out.println("start "+start+" end "+end+ " profit "+profit);
       }
       return maxprofit;
    }
}
