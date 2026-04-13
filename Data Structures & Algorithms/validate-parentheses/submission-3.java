class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> bracketMap = new HashMap<>();

        bracketMap.put(')','(');
        bracketMap.put(']','[');
        bracketMap.put('}','{');

        for(int i = 0;i< s.length();i++){
            Character ch = s.charAt(i);
            if(bracketMap.containsKey(ch)){
                if(!stack.isEmpty() && bracketMap.get(ch) ==  stack.peek()) {
                    stack.pop();
                } else{
                    return false;
                }
            }else{
                stack.push(ch);
            }
        }
        return stack.empty();
    }
}
