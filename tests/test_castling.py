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
    
            # Ensure input is sent as formatted strings (e.g., "7 1")
            start_str = f"{start[0]} {start[1]}"
            end_str = f"{end[0]} {end[1]}"
    
            # Select the piece
            print(f"DEBUG: Sending input to select piece at {start_str}.")
            self.engine.process.stdin.write(f"{start_str}\n")
            self.engine.process.stdin.flush()
            time.sleep(0.5)  # Allow engine to process
            
            # Fetch updated output after selection
            game_condition, board, sides, highlights = self.engine._get_output(24, include_condition=True)
            print(f"DEBUG: Board after selecting piece at {start_str}:\n{board}")
            print(f"DEBUG: Highlights after selecting piece:\n{highlights}")
    
            # Validate selection
            if not highlights or highlights[end[0]][end[1]] != "1":
                self.fail(f"Failed to select piece at {start_str}: target {end_str} not in valid highlights.")
    
            # Move the piece
            print(f"DEBUG: Sending input to move piece to {end_str}.")
            self.engine.process.stdin.write(f"{end_str}\n")
            self.engine.process.stdin.flush()
            time.sleep(0.5)  # Allow engine to process
            
            # Fetch updated output after movement
            game_condition, board, sides, highlights = self.engine._get_output(24, include_condition=True)
            print(f"DEBUG: Board after moving piece to {end_str}:\n{board}")
    
            # Validate movement
            if board[end[0]][end[1]] == "X":
                self.fail(f"Failed to move piece to {end_str}: board state did not reflect the move.")
    
            print(f"DEBUG: Successfully completed move from {start_str} to {end_str}.\n")
        
        print("DEBUG: Test completed successfully.")

if __name__ == "__main__":
    unittest.main()
