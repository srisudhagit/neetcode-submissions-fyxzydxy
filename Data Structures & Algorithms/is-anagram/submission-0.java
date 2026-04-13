class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> mapS = new HashMap<>();
        Map<Character, Integer> mapT = new HashMap<>();

        if(s.length() != t.length()){
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
           if(mapS.containsKey(ch)){
                int val = mapS.get(ch);
                mapS.replace(ch,val+1);
           }else{
                mapS.put(ch,1);
           }
        }

        for (int i = 0; i < t.length(); i++) {
            char ch = t.charAt(i);
           if(mapT.containsKey(ch)){
                int val = mapT.get(ch);
                mapT.replace(ch,val+1);
           }else{
                mapT.put(ch,1);
           }
        }

        for(Map.Entry<Character,Integer> entry : mapS.entrySet()){
            int value = entry.getValue();
            char ch = entry.getKey();
            if(mapT.containsKey(ch)){
                Integer valT = mapT.get(ch);
                if(valT != value){
                    return false;
                }
            }else{
                return false;
            }
        }
        return true;
    }
}
