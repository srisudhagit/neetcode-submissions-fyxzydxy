class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> outputmap = new HashMap<>();
        for(String str : strs){
            String keyStr = getKeyString(str);
            if(!outputmap.containsKey(keyStr)){
                outputmap.put(keyStr, new ArrayList<>());
            }
            outputmap.get(keyStr).add(str);
        }
        return new ArrayList<>(outputmap.values());
    }

    public String getKeyString(String str){
        int[] output = new int[26];
        for(char c : str.toCharArray()){
            output[c-'a']++;
        }
        return Arrays.toString(output);
    }
}
