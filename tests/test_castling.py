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
        
        # Define the sequence of moves
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
    
            # Select the piece
            game_condition, board, sides, highlights = self.engine.select_piece(*start)
            time.sleep(0.5)  # Allow engine to process
            
            # Retrieve the latest outputs
            game_condition, board, sides, highlights = self.engine.get_output()
            print(f"DEBUG: Updated board state after selecting piece at {start}:\n{board}")
            print(f"DEBUG: Updated highlights after selecting piece at {start}:\n{highlights}")
    
            # Validate selection
            if not highlights or highlights[end[0]][end[1]] != "1":
                self.fail(f"Failed to select piece at {start}: target {end} not in valid highlights.")
    
            # Move the piece
            print(f"DEBUG: Attempting to move piece to {end}.")
            game_condition, board, sides, highlights = self.engine.move_piece(*end)
            time.sleep(0.5)  # Allow engine to process
            
            # Retrieve the latest outputs
            game_condition, board, sides, highlights = self.engine.get_output()
            print(f"DEBUG: Updated board state after moving piece to {end}:\n{board}")
            
            # Validate movement
            if board[end[0]][end[1]] == "X":
                self.fail(f"Failed to move piece to {end}: board state did not reflect the move.")
    
            print(f"DEBUG: Successfully completed move from {start} to {end}.\n")
        
        print("DEBUG: Test completed successfully.")

if __name__ == "__main__":
    unittest.main()
