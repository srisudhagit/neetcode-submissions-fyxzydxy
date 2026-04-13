class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> numQueue = new PriorityQueue<>(Comparator.reverseOrder());
        for(int num : nums){
            numQueue.offer(num);
        }

        for(int i=1;i<k;i++){
            numQueue.poll();
        }

        return numQueue.poll();
    }
}
