class Solution {
    public boolean isPalindrome(String s) {
        int fpos=0, lpos=s.length()-1;
        Character fch,lch;
        boolean ispalindrome=false;
        while(fpos < lpos){
            fch = s.charAt(fpos);
            lch = s.charAt(lpos);
            if((Character.isLetterOrDigit(fch)) && (Character.isLetterOrDigit(lch))){
                    System.out.println(fch+" "+lch);
                    if(Character.toUpperCase(fch) != Character.toUpperCase(lch)){
                        return false;
                    }
                    fpos++;
                    lpos--;
            }else{
                if(!(Character.isLetterOrDigit(fch))){
                    fpos++;
                }else{
                    lpos--;
                }
            }
           
        }
        return true;
    }
}
