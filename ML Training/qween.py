import tkinter as tk

N = 8

class NQueenGame:
    def __init__(self, root):
        self.root = root
        self.root.title("N-Queens Game (Play Mode)")

        self.board = [[0]*N for _ in range(N)]
        self.cells = []

        self.create_board()

        tk.Button(root, text="Reset", command=self.reset).grid(row=N, column=0, columnspan=N, sticky="we")

    # ---------------- UI ---------------- #
    def create_board(self):
        for i in range(N):
            row_cells = []
            for j in range(N):
                color = "white" if (i+j)%2 == 0 else "gray"

                lbl = tk.Label(
                    self.root,
                    width=3,
                    height=1,
                    bg=color,
                    font=("Arial", 18),
                    borderwidth=1,
                    relief="solid"
                )

                lbl.grid(row=i, column=j)

                # Click event
                lbl.bind("<Button-1>", lambda e, r=i, c=j: self.toggle_queen(r, c))

                row_cells.append(lbl)
            self.cells.append(row_cells)

    def update_board(self):
        for i in range(N):
            for j in range(N):
                if self.board[i][j] == 1:
                    self.cells[i][j].config(text="Q", fg="red")
                else:
                    self.cells[i][j].config(text="")

    def reset(self):
        self.board = [[0]*N for _ in range(N)]
        self.update_board()

    # ---------------- GAME LOGIC ---------------- #
    def isSafe(self, row, col):
        # Row check
        for i in range(N):
            if self.board[row][i] == 1:
                return False

        # Column check
        for i in range(N):
            if self.board[i][col] == 1:
                return False

        # Diagonal (top-left to bottom-right)
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i < N and j < N:
            if self.board[i][j] == 1:
                return False
            i += 1
            j += 1

        # Diagonal (top-right to bottom-left)
        i, j = row, col
        while i >= 0 and j < N:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        i, j = row, col
        while i < N and j >= 0:
            if self.board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True

    def toggle_queen(self, row, col):
        if self.board[row][col] == 1:
            # Remove queen
            self.board[row][col] = 0
        else:
            # Check safety before placing
            if self.isSafe(row, col):
                self.board[row][col] = 1
            else:
                print("❌ Invalid move!")

        self.update_board()
        self.check_win()

    def check_win(self):
        count = sum(sum(row) for row in self.board)

        if count == N:
            print("🎉 You solved N-Queens!")


# ---------------- RUN ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    game = NQueenGame(root)
    root.mainloop()
