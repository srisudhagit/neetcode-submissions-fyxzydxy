class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length=0,longestlength=0;
        HashMap<Character,Boolean> hmap = new HashMap<>();
        int start=0,i=0;
        while(i<s.length()){
            char ch = s.charAt(i);
            if(hmap.containsKey(ch)){
                if(length > longestlength){
                    longestlength = length;     
                }
                start++;
                i = start;
                length = 0;
                hmap.clear();
                continue;              
            }else{
                hmap.put(ch,true);
                length++;
                i++;
            }
        }
        return Math.max(longestlength,length);
    }
}
