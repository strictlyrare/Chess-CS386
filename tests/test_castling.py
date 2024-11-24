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

    def test_castling_kingside(self):
        print("DEBUG: Running test_castling_kingside...")

        # Sequence of moves for kingside castling
        moves = [
            ((7, 6), (5, 5)),  # Move white knight g1 -> f3
            ((1, 5), (2, 5)),  # Move black pawn f7 -> f6
            ((6, 6), (5, 6)),  # Move white pawn g2 -> g3
            ((1, 6), (2, 6)),  # Move black pawn g7 -> g6
            ((7, 5), (6, 6)),  # Move white bishop f1 -> g2
            ((1, 4), (2, 4)),  # Move black pawn e7 -> e6
            ((7, 4), (7, 6))   # Perform kingside castling (king e1 -> g1)
        ]

        retries = 5
        for start, end in moves:
            for attempt in range(retries):
                # Select the piece
                game_condition, board, sides, highlights = self.engine.select_piece(*start)
                time.sleep(1.0)
                game_condition, board, sides, highlights = self.engine.select_piece(*start)
                if not board or not highlights:
                    print(f"DEBUG: Select piece failed (attempt {attempt + 1}/{retries}). Retrying...")
                    time.sleep(1.0)
                    continue

                # Debugging board and highlights
                print(f"DEBUG: Board after selecting piece {start}:\n{board}")
                print(f"DEBUG: Highlights after selecting piece {start}:\n{highlights}")

                # Move the piece
                game_condition, board, sides, highlights = self.engine.move_piece(*end)
                time.sleep(1.0)
                game_condition, board, sides, highlights = self.engine.move_piece(*end)
                if board and board[end[0]][end[1]] != "X":
                    print(f"DEBUG: Successfully moved piece from {start} to {end}.")
                    break
                else:
                    print(f"DEBUG: Move failed (attempt {attempt + 1}/{retries}). Retrying...")
                    time.sleep(1.0)
            else:
                self.fail(f"Failed to move piece from {start} to {end} after {retries} retries.")

        # Verify final board state after castling
        board, _, _ = self.engine._get_output(24, include_condition=False)
        time.sleep(1.0)
        board, _, _ = self.engine._get_output(24, include_condition=False)
        print(f"DEBUG: Final board state after castling:\n{board}")
        self.assertEqual(board[7][6], "K", "King should be at g1 after castling.")
        self.assertEqual(board[7][5], "R", "Rook should be at f1 after castling.")
        self.assertEqual(board[7][4], "X", "e1 should be empty after castling.")
        self.assertEqual(board[7][7], "X", "h1 should be empty after castling.")

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
    
        retries = 5
        for start, end in moves:
            for attempt in range(retries):
                print(f"DEBUG: Attempting move from {start} to {end} (Attempt {attempt + 1}/{retries})")
    
                # Select the piece
                game_condition, board, sides, highlights = self.engine.select_piece(*start)
                print(f"DEBUG: Board after select_piece at {start}:\n{board}")
                print(f"DEBUG: Highlights at {start}:\n{highlights}")
                if not board or not highlights:
                    print("ERROR: No board or highlights returned. Retrying...")
                    time.sleep(1.0)
                    continue
    
                # Move the piece
                game_condition, board, sides, highlights = self.engine.move_piece(*end)
                print(f"DEBUG: Board after move_piece to {end}:\n{board}")
                if board and board[end[0]][end[1]] != "X":
                    print(f"DEBUG: Successfully moved piece from {start} to {end}.")
                    break
                else:
                    print(f"ERROR: Move to {end} failed. Retrying...")
                    time.sleep(1.0)
            else:
                self.fail(f"Failed to move piece from {start} to {end} after {retries} retries.")
    
        # Validate final board state
        board, sides, highlights = self.engine._get_output(24, include_condition=False)
        print(f"DEBUG: Final board state after castling:\n{board}")
        expected_positions = {
            (7, 2): "K",  # King at c1
            (7, 3): "R",  # Rook at d1
            (7, 4): "X",  # e1 empty
            (7, 0): "X"   # a1 empty
        }
        for position, expected_piece in expected_positions.items():
            actual_piece = board[position[0]][position[1]]
            self.assertEqual(actual_piece, expected_piece,
                             f"Expected {expected_piece} at {position}, but found {actual_piece}")

if __name__ == "__main__":
    unittest.main()
