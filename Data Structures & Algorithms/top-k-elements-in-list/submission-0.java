class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> numMap = new HashMap<>();
        for(int num : nums){
           numMap.put(num, numMap.getOrDefault(num,1)+1);
        }
        PriorityQueue<Integer> heap = new PriorityQueue<>((a,b) -> numMap.get(a)-numMap.get(b));

        for (int num : numMap.keySet()) {
            heap.add(num);
            if (heap.size() > k) {
                heap.poll(); // Remove the element with the lowest frequency
            }
        }

        // Step 4: Extract the top k elements from the heap
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = heap.poll();
        }
        return result;
    }
}
