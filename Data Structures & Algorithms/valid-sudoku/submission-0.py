class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r] or
                   board[r][c] in cols[c] or 
                   board[r][c] in squares[(r // 3, c // 3)]):
                   return False
                else:
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[r // 3, c // 3].add(board[r][c])
        return True

'''
Splits a sudoku board into a 9x9 grid 
AND
3x3 grid

9x9 to keep track of the rows and collums
Each row and collumn had a new set created with

{Row/Collumn number 0 - 8: Numbers inside that row or collumn}
{Square number 0 - 2: Numbers inside the square}

    0       1       2.  <---- Square number   
    0 1 2.  3 4 5.  6 7 8 <---- Collumn numbers
  | - - - | - - - | - - - |
0 | - - - | - - - | - - - |
  | - - - | - - - | - - - |
  -------------------------
  | - - - | - - - | - - - |
1 | - - - | - - - | - - - |
  | - - - | - - - | - - - |
  -------------------------
  | - - - | - - - | - - - |
2 | - - - | - - - | - - - |
  | - - - | - - - | - - - |


'''
                    