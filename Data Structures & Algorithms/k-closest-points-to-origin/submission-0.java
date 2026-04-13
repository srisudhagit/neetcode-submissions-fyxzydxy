class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> distQue = new PriorityQueue<>((a,b) -> Double.compare(distance(b),distance(a)));
        int[][] result = new int[k][2];
        for(int[] point : points){
            distQue.offer(point);
            if(distQue.size() > k){
                distQue.poll();
            }
        }

       int pos=0;
       while(!distQue.isEmpty()){
            result[pos++] = distQue.poll();
        }

        return result;
    }

    public double distance(int[] a){
        return a[0]*a[0]+a[1]*a[1];
    }
}
