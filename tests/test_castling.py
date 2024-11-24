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

        # Sequence of moves to enable kingside castling
        moves = [
            ((7, 6), (5, 5)),  # White knight g1 -> f3
            ((1, 5), (2, 5)),  # Black pawn f7 -> f6
            ((6, 6), (5, 6)),  # White pawn g2 -> g3
            ((1, 6), (2, 6)),  # Black pawn g7 -> g6
            ((7, 5), (6, 6)),  # White bishop f1 -> g2
            ((1, 4), (2, 4)),  # Black pawn e7 -> e6
            ((7, 4), (7, 6))   # White king e1 -> g1 (kingside castling)
        ]

        # Execute each move in sequence
        for start, end in moves:
            self._execute_move(start, end)

        # Verify the final board state
        board, _, _ = self.engine.get_initial_board()
        print(f"DEBUG: Final board state after castling:\n{board}")
        self.assertEqual(board[7][6], "K", "King should be at g1 after castling.")
        self.assertEqual(board[7][5], "R", "Rook should be at f1 after castling.")
        self.assertEqual(board[7][4], "X", "e1 should be empty after castling.")
        self.assertEqual(board[7][7], "X", "h1 should be empty after castling.")

    def test_castling_queenside(self):
        print("DEBUG: Running test_castling_queenside...")

        # Sequence of moves to enable queenside castling
        moves = [
            ((7, 1), (5, 0)),  # White knight b1 -> a3
            ((1, 1), (2, 1)),  # Black pawn b7 -> b6
            ((6, 3), (5, 3)),  # White pawn d2 -> d3
            ((1, 2), (2, 2)),  # Black pawn c7 -> c6
            ((7, 2), (5, 4)),  # White bishop c1 -> e3
            ((1, 3), (2, 3)),  # Black pawn d7 -> d6
            ((7, 3), (6, 3)),  # White queen d1 -> d2
            ((1, 4), (2, 4)),  # Black pawn e7 -> e6
            ((7, 4), (7, 2))   # White king e1 -> c1 (queenside castling)
        ]

        # Execute each move in sequence
        for start, end in moves:
            self._execute_move(start, end)

        # Verify the final board state
        board, _, _ = self.engine.get_initial_board()
        print(f"DEBUG: Final board state after castling:\n{board}")
        self.assertEqual(board[7][2], "K", "King should be at c1 after castling.")
        self.assertEqual(board[7][3], "R", "Rook should be at d1 after castling.")
        self.assertEqual(board[7][4], "X", "e1 should be empty after castling.")
        self.assertEqual(board[7][0], "X", "a1 should be empty after castling.")

    def _execute_move(self, start, end):
        """Selects a piece and moves it."""
        row_start, col_start = start
        row_end, col_end = end

        # Select the piece
        game_condition, board, sides, highlights = self.engine.select_piece(row_start, col_start)
        if board is None or highlights is None:
            self.fail(f"Failed to select piece at {start}. Board or highlights are missing.")

        # Move the piece
        game_condition, board, sides, highlights = self.engine.move_piece(row_end, col_end)
        if board is None:
            self.fail(f"Failed to move piece from {start} to {end}. Board is missing.")
        print(f"DEBUG: Move from {start} to {end} completed. Game condition: {game_condition}")

if __name__ == "__main__":
    unittest.main()
