import unittest
import time
from SubProcess import ChessEngine

class TestCastling(unittest.TestCase):
    def setUp(self):
        # Initialize the chess engine subprocess
        self.engine = ChessEngine("chess.exe")

    def tearDown(self):
        # Close the chess engine subprocess
        self.engine.close()

    def test_castling_queenside(self):
        print("DEBUG: Running test_castling_queenside...")
    
        moves = [
            ((7, 1), (5, 0)),  # Move white knight b1 -> a3
            ((1, 1), (2, 1)),  # Move black pawn b7 -> b6
            ((6, 3), (5, 3)),  # Move white pawn d2 -> d3
            ((1, 2), (2, 2)),  # Move black pawn c7 -> c6
            ((7, 2), (5, 4)),  # Move white bishop c1 -> e3
            ((1, 3), (2, 3)),  # Move black pawn d7 -> d6
            ((7, 3), (6, 3)),  # Move white queen d1 -> d2
            ((1, 4), (2, 4)),  # Move black pawn e7 -> e6
            ((7, 4), (7, 2))   # Perform queenside castling (king e1 -> c1)
        ]
    
        for start, end in moves:
            print(f"DEBUG: Processing move from {start} to {end}.")
    
            # Use select_piece method
            print(f"DEBUG: Selecting piece at {start}.")
            game_condition, board, sides, highlights = self.engine.select_piece(*start)
    
            # Validate selection
            if not highlights or highlights[end[0]][end[1]] != "1":
                print(f"ERROR: Failed to select piece at {start}.")
                print(f"DEBUG: Highlights array:\n{highlights}")
                self.fail(f"Failed to select piece at {start}. Target move {end} not in highlights.")
    
            # Use move_piece method
            print(f"DEBUG: Moving piece to {end}.")
            game_condition, board, sides, highlights = self.engine.move_piece(*end)
    
            # Validate movement
            if board[end[0]][end[1]] == "X":
                print(f"ERROR: Piece not moved to {end}. Board state:\n{board}")
                self.fail(f"Failed to move piece to {end}.")
    
            print(f"DEBUG: Successfully moved piece from {start} to {end}. Board state:\n{board}")
    
        print("DEBUG: Test completed successfully.")

if __name__ == "__main__":
    unittest.main()
