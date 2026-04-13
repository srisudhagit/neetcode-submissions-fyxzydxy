class Solution {
    public int lastStoneWeight(int[] stones) {
        List<Integer> stoneslist = new ArrayList<>();
        Integer[] stonesWrapper = new Integer[stones.length];
        for (int i = 0; i < stones.length; i++) {
            stonesWrapper[i] = stones[i];
        }
        Collections.addAll(stoneslist,stonesWrapper);
        while(stoneslist.size() >= 2){
            Collections.sort(stoneslist);
            Integer firstMax = stoneslist.get(stoneslist.size()-1);
            Integer secondMax = stoneslist.get(stoneslist.size()-2); 
            stoneslist.remove(firstMax);
            stoneslist.remove(secondMax);
            stoneslist.add(firstMax-secondMax);
        }
        if(stoneslist.size() == 0){
            return 0;
        }else{
            return stoneslist.get(0);
        }
    }
}
