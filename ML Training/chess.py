import tkinter as tk

# Board size
SIZE = 8
CELL_SIZE = 80

# Pieces (simple text symbols)
pieces = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙"
}

# Initial board
board = [
    list("rnbqkbnr"),
    list("pppppppp"),
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    list("PPPPPPPP"),
    list("RNBQKBNR"),
]

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=SIZE*CELL_SIZE, height=SIZE*CELL_SIZE)
        self.canvas.pack()

        self.selected = None
        self.turn = "white"

        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        self.canvas.delete("all")

        for row in range(SIZE):
            for col in range(SIZE):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                color = "#EEEED2" if (row + col) % 2 == 0 else "#769656"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

                piece = board[row][col]
                if piece:
                    self.canvas.create_text(
                        x1 + CELL_SIZE//2,
                        y1 + CELL_SIZE//2,
                        text=pieces[piece],
                        font=("Arial", 32)
                    )

    def on_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE

        if self.selected:
            self.move_piece(self.selected, (row, col))
            self.selected = None
        else:
            piece = board[row][col]
            if piece:
                if (piece.isupper() and self.turn == "white") or \
                   (piece.islower() and self.turn == "black"):
                    self.selected = (row, col)

    def move_piece(self, start, end):
        sr, sc = start
        er, ec = end

        piece = board[sr][sc]

        # Basic rule: allow any move (you can improve later)
        board[er][ec] = piece
        board[sr][sc] = ""

        # Switch turn
        self.turn = "black" if self.turn == "white" else "white"

        self.draw_board()


# Run app
root = tk.Tk()
root.title("Chess Game - 2 Player")
game = ChessGame(root)
root.mainloop()