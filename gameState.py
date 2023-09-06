
class GameState:

    def __init__(self):

        self.board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ]
    
    def check_if_full(board) -> bool:
        # iterates through the board and returns True if it is full
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    return False
                else:
                    return True
                

class Move:

    def check_valid_move(move, board) -> bool:
        # checks if the move is valid and returns a boolean
        if board[move[0]][move[1]] != "-":
            return False
        return True
