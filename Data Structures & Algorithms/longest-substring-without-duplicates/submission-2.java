class Solution {
    public int lengthOfLongestSubstring(String s) {       
        int res=0,l=0;
        HashSet<Character> hashset = new HashSet<>();

        for(int r=0;r<s.length();r++){
                //remove from the left
                while(hashset.contains(s.charAt(r))){
                    hashset.remove(s.charAt(l));
                    l++;
                }
                //add from the right
                hashset.add(s.charAt(r));
                res = Math.max(res,r-l+1);
        }
            return res;   
        }
    }
