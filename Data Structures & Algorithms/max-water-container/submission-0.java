class Solution {
    public int maxArea(int[] heights) {
        int maxarea=0,area=0,left=0,right=heights.length-1;
        while(left < right){
            area = (right-left)*Math.min(heights[left],heights[right]);
            if(area > maxarea){
                maxarea = area;
            }else{
                if(heights[left] < heights[right]){
                    left++;
                }else{
                    right--;
                }
            }
        }
        return maxarea;
    }
}
