class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character>[] row_hashset = new HashSet[9];
        HashSet<Character>[] col_hashset = new HashSet[9];
        HashSet<Character>[] subsquare_hashset = new HashSet[9];

        for(int i=0;i<9;i++){
            row_hashset[i] = new HashSet<>();
            col_hashset[i] = new HashSet<>();
            subsquare_hashset[i] = new HashSet<>();
        }

        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                char ele = board[i][j];
                if(ele == '.'){
                    continue;
                }
                int boxIndex = (i / 3) * 3 + (j / 3);
                if(row_hashset[i].contains(ele) || 
                   col_hashset[j].contains(ele) ||
                   subsquare_hashset[boxIndex].contains(ele)){
                    return false;
                } 
                row_hashset[i].add(ele);
                col_hashset[j].add(ele);
                subsquare_hashset[boxIndex].add(ele);
            }
        }
        return true;
    }
}
