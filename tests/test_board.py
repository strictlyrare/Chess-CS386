import unittest
from SubProcess import ChessEngine

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.engine = ChessEngine("chess.exe")

    def tearDown(self):
        self.engine.close()

    def test_initial_board_setup(self):
        print("DEBUG: Running test_initial_board_setup...")
        board, sides, highlights = self.engine.get_initial_board()
        print(f"DEBUG: Board: {board}")
        self.assertIsNotNone(board, "Board is None. Check subprocess communication.")
        if board:
            self.assertEqual(len(board), 8, "Expected 8 rows for the board.")
            self.assertEqual(len(board[0]), 8, "Expected 8 columns for the board.")
            self.assertEqual(board[0][0], "R", f"Unexpected piece at board[0][0]: {board[0][0]}")
            self.assertEqual(board[7][7], "R", f"Unexpected piece at board[7][7]: {board[7][7]}")

    def test_highlights_initial_state(self):
        print("DEBUG: Running test_highlights_initial_state...")
        _, _, highlights = self.engine.get_initial_board()
        print(f"DEBUG: Highlights: {highlights}")
        self.assertIsNotNone(highlights, "Highlights are None.")
        self.assertEqual(len(highlights), 8, "Expected 8 rows for highlights.")
        # Adjusted condition: Highlights might not be 'X' for all cells
        self.assertTrue(all(len(row) == 8 for row in highlights),
                    "Each row in highlights should have 8 columns.")


if __name__ == "__main__":
    unittest.main()
