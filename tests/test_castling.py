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

        retries = 5  # Number of retries for each operation

        # Step 1: Move white knight from g1 to f3
        knight_start = (7, 6)  # g1
        knight_end = (5, 5)    # f3

        for attempt in range(retries):
            game_condition, board, sides, highlights = self.engine.select_piece(*knight_start)

            if not board or not highlights:
                print(f"DEBUG: Select piece failed to return data (attempt {attempt + 1}/{retries}). Retrying...")
                time.sleep(1.0)
                continue

            # Debug statement for current board and highlights
            print(f"DEBUG: Board after selecting knight (attempt {attempt + 1}):\n{board}")
            print(f"DEBUG: Highlights after selecting knight (attempt {attempt + 1}):\n{highlights}")

            highlighted_positions = [(r, c) for r, row in enumerate(highlights) for c, v in enumerate(row) if v == "1"]
            if knight_end not in highlighted_positions:
                print("DEBUG: f3 is not highlighted as a valid move for the knight.")
                time.sleep(1.0)
                continue

            # Move the piece and verify
            game_condition, board, sides, highlights = self.engine.move_piece(*knight_end)
            print(f"DEBUG: Board after moving knight (attempt {attempt + 1}):\n{board}")

            if board and board[knight_end[0]][knight_end[1]] == "G" and board[knight_start[0]][knight_start[1]] == "X":
                print("DEBUG: Knight successfully moved to f3.")
                break
            else:
                print(f"DEBUG: Knight move to f3 failed (attempt {attempt + 1}/{retries}). Retrying...")
                time.sleep(1.0)
        else:
            self.fail("Knight move to f3 failed.")

        # Step 2: Black move to maintain turn order (move black pawn from e7 to e5)
        black_pawn_start = (1, 4)  # e7
        black_pawn_end = (3, 4)    # e5

        for attempt in range(retries):
            game_condition, board, sides, highlights = self.engine.select_piece(*black_pawn_start)

            if not board or not highlights:
                print(f"DEBUG: Select piece failed for black pawn (attempt {attempt + 1}/{retries}). Retrying...")
                time.sleep(1.0)
                continue

            # Move the piece and verify
            game_condition, board, sides, highlights = self.engine.move_piece(*black_pawn_end)
            print(f"DEBUG: Board after moving black pawn (attempt {attempt + 1}):\n{board}")

            if board and board[black_pawn_end[0]][black_pawn_end[1]] == "P" and board[black_pawn_start[0]][black_pawn_start[1]] == "X":
                print("DEBUG: Black pawn successfully moved to e5.")
                break
            else:
                print(f"DEBUG: Black pawn move failed (attempt {attempt + 1}/{retries}). Retrying...")
                time.sleep(1.0)
        else:
            self.fail("Black pawn move failed.")

        # Step 3: Move white bishop from f1 to e2
        bishop_start = (7, 5)  # f1
        bishop_end = (6, 4)    # e2

        for attempt in range(retries):
            game_condition, board, sides, highlights = self.engine.select_piece(*bishop_start)

            if not board or not highlights:
                print(f"DEBUG: Select piece failed for white bishop (attempt {attempt + 1}/{retries}). Retrying...")
                time.sleep(1.0)
                continue

            # Move the piece and verify
            game_condition, board, sides, highlights = self.engine.move_piece(*bishop_end)
            print(f"DEBUG: Board after moving bishop (attempt {attempt + 1}):\n{board}")

            if board and board[bishop_end[0]][bishop_end[1]] == "B" and board[bishop_start[0]][bishop_start[1]] == "X":
                print("DEBUG: Bishop successfully moved to e2.")
                break
            else:
                print(f"DEBUG: Bishop move to e2 failed (attempt {attempt + 1}/{retries}). Retrying...")
                time.sleep(1.0)
        else:
            self.fail("Bishop move to e2 failed.")

        # Step 4: Perform kingside castling
        king_start = (7, 4)  # e1
        king_castling_target = (7, 6)  # g1 (king moves)
        rook_castling_target = (7, 5)  # f1 (rook moves)

        for attempt in range(retries):
            game_condition, board, sides, highlights = self.engine.select_piece(*king_start)

            if not board or not highlights:
                print(f"DEBUG: Select piece failed for king (attempt {attempt + 1}/{retries}). Retrying...")
                time.sleep(1.0)
                continue

            # Move the king to complete the castling
            game_condition, board, sides, highlights = self.engine.move_piece(*king_castling_target)
            print(f"DEBUG: Board after castling move (attempt {attempt + 1}):\n{board}")

            if board and board[king_castling_target[0]][king_castling_target[1]] == "K" and board[rook_castling_target[0]][rook_castling_target[1]] == "R":
                print("DEBUG: Kingside castling successfully performed.")
                break
            else:
                print(f"DEBUG: Castling move failed (attempt {attempt + 1}/{retries}). Retrying...")
                time.sleep(1.0)
        else:
            self.fail("Kingside castling failed.")

        # Step 5: Verify final board state
        print(f"DEBUG: Final board state after castling:\n{board}")
        self.assertEqual(board[7][6], "K", "King should be at g1 after castling.")
        self.assertEqual(board[7][5], "R", "Rook should be at f1 after castling.")
        self.assertEqual(board[7][4], "X", "e1 should be empty after castling.")
        self.assertEqual(board[7][7], "X", "h1 should be empty after castling.")

    def test_castling_queenside(self):
        print("DEBUG: Running test_castling_queenside...")

        # Step 1: Clear the path for queenside castling
        # Move queen (d1) out of the way
        self.engine.select_piece(7, 3)  # Select queen at d1
        time.sleep(0.5)
        game_condition, board, _, _ = self.engine.move_piece(4, 3)  # Move queen to d4
        time.sleep(0.5)
        print(f"DEBUG: Board after moving queen to d4:\n{board}")

        self.assertEqual(board[4][3], "Q", "Queen should have moved to d4.")  # Ensure the queen has moved
        self.assertEqual(board[7][3], "X", "d1 should be empty after the queen moves.")  # Ensure d1 is empty

        # Move bishop (c1) out of the way
        self.engine.select_piece(7, 2)  # Select bishop at c1
        time.sleep(0.5)
        game_condition, board, _, _ = self.engine.move_piece(5, 0)  # Move bishop to a3
        time.sleep(0.5)
        print(f"DEBUG: Board after moving bishop to a3:\n{board}")

        self.assertEqual(board[5][0], "B", "Bishop should have moved to a3.")  # Ensure the bishop has moved
        self.assertEqual(board[7][2], "X", "c1 should be empty after the bishop moves.")  # Ensure c1 is empty

        # Step 2: Select the king and rook for castling
        moves = [(7, 4), (7, 0)]  # Select king and rook on the queenside
        for row, col in moves:
            game_condition, _, _, _ = self.engine.select_piece(row, col)
            # Introduce a delay to allow the C engine to update
            time.sleep(0.5)
            print(f"DEBUG: Selected piece at ({row}, {col}) with game_condition: {game_condition}")

        # Step 3: Move the king to castle
        game_condition, board, _, _ = self.engine.move_piece(7, 2)
        # Introduce a delay to ensure the board is updated
        time.sleep(0.5)

        # Step 4: Assertions
        print(f"DEBUG: Board after attempting to castle queenside:\n{board}")
        self.assertEqual(game_condition, 0, "Game condition should indicate valid move.")
        self.assertEqual(board[7][2], "K", "King should have moved to c1.")
        self.assertEqual(board[7][3], "R", "Rook should have moved to d1.")

if __name__ == "__main__":
    unittest.main()
