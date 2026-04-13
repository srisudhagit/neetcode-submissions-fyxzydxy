class Solution {
    public boolean checkInclusion(String s1, String s2) {
        boolean containsPerm = false;
        for(int k=0;k<s2.length()-s1.length()+1;k++){
            String sub = String.valueOf(s2.charAt(k));
            if(s1.contains(sub)){
                containsPerm = isPermutation(s1, s2.substring(k,k+s1.length()));
                System.out.println(containsPerm);
            }
            if(containsPerm){
                return true;
            }
        }
        return false;
    }

    boolean isPermutation(String s1, String s2){
        System.out.println(s1+" "+s2);
        HashMap<Character, Integer> hmap = new HashMap<>();
        for(int i=0;i<s1.length();i++){
            hmap.put(s1.charAt(i), hmap.getOrDefault(s1.charAt(i),0)+1);
        }

        for(int i=0;i<s2.length();i++){
            char ch = s2.charAt(i);
            if(!hmap.containsKey(ch)){
                return false;
            }else{
                hmap.put(ch,hmap.get(ch)-1);
                if(hmap.get(ch) == 0){
                    hmap.remove(ch);
                }
            }
        }
       return hmap.isEmpty();
    }
}
