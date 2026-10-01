class Solution:
    def isValidSudoku(self, board):
        
        # Check rows
        for row in board:
            numbers = []
            
            for value in row:
                if value != '.':
                    if value in numbers:
                        return False
                    numbers.append(value)

        # Check columns
        for col in range(9):
            numbers = []
            
            for row in range(9):
                value = board[row][col]
                
                if value != '.':
                    if value in numbers:
                        return False
                    numbers.append(value)

        # Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                
                numbers = []
                
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        
                        value = board[i][j]
                        
                        if value != '.':
                            if value in numbers:
                                return False
                            numbers.append(value)

        return True