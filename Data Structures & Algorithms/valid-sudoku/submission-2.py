class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        cols = defaultdict(set)
        subsquare = defaultdict(set)

        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele == ".":
                    continue
                
                if (ele in row[i] or ele in cols[j] or ele in subsquare[(i//3, j//3)]):
                    return False
                
                row[i].add(ele)
                cols[j].add(ele)
                subsquare[(i//3, j//3)].add(ele)

        return True