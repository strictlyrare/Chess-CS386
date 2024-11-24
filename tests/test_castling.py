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
            ((7, 1), (5, 0)),
            ((1, 1), (2, 1)),
            ((6, 3), (5, 3)),
            ((1, 2), (2, 2)),
            ((7, 2), (5, 4)),
            ((1, 3), (2, 3)),
            ((7, 3), (6, 3)),
            ((1, 4), (2, 4)),
            ((7, 4), (7, 2))
        ]
    
        for start, end in moves:
            print(f"DEBUG: Processing move from {start} to {end}.")
            start_str = f"{start[0]} {start[1]}"
            end_str = f"{end[0]} {end[1]}"
    
            # Select the piece
            print(f"DEBUG: Sending input to select piece at {start_str}.")
            self.engine.process.stdin.write(f"{start_str}\n")
            self.engine.process.stdin.flush()
            time.sleep(0.5)
    
            # Fetch outputs after selection
            game_condition, output_lines = self.engine._get_output(24, include_condition=True)
    
            # Parse board, sides, and highlights from `output_lines`
            board_rows = output_lines[:8]
            sides_rows = output_lines[8:16]
            highlights_rows = output_lines[16:24]
            print(f"DEBUG: Raw highlights_rows received from C:\n{highlights_rows}")

            board = [row.split() for row in board_rows]
            sides = [row.split() for row in sides_rows]
            highlights = [row.split() for row in highlights_rows]
    
            # Validate selection
            if not highlights or highlights[end[0]][end[1]] != "1":
                print(f"DEBUG: Highlights array dimensions: {len(highlights)}x{len(highlights[0]) if highlights else 0}")
                print(f"DEBUG: Highlights array at failure point:\n{highlights}")
                print(f"DEBUG: Expected value '1' at Highlights[{end[0]}][{end[1]}], but found: "
                      f"'{highlights[end[0]][end[1]] if highlights else 'No highlights'}'.")
                print(f"DEBUG: Raw highlights_rows received from C:\n{highlights_rows}")
                self.fail(f"Failed to select piece at {start_str}: target {end_str} not in valid highlights.")
    
            # Move the piece
            print(f"DEBUG: Attempting to move piece to {end}.")
            self.engine.process.stdin.write(f"{end_str}\n")
            self.engine.process.stdin.flush()
            time.sleep(0.5)
    
            # Fetch outputs after movement
            game_condition, output_lines = self.engine._get_output(24, include_condition=True)
    
            # Parse board, sides, and highlights again
            board_rows = output_lines[:8]
            sides_rows = output_lines[8:16]
            highlights_rows = output_lines[16:24]
    
            board = [row.split() for row in board_rows]
    
            if board[end[0]][end[1]] == "X":
                self.fail(f"Failed to move piece to {end_str}: board state did not reflect the move.")
    
            print(f"DEBUG: Successfully completed move from {start_str} to {end_str}.\n")
    
        print("DEBUG: Test completed successfully.")

if __name__ == "__main__":
    unittest.main()
