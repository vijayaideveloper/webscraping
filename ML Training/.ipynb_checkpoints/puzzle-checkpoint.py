import tkinter as tk
from collections import deque
import random
import time

# Goal state
goal = [1,2,3,4,5,6,7,8,0]

# ---------------- BFS LOGIC ---------------- #
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)

    moves = {
        0: [1,3],
        1: [0,2,4],
        2: [1,5],
        3: [0,4,6],
        4: [1,3,5,7],
        5: [2,4,8],
        6: [3,7],
        7: [6,4,8],
        8: [7,5]
    }

    for move in moves[idx]:
        new_state = state[:]
        new_state[idx], new_state[move] = new_state[move], new_state[idx]
        neighbors.append(new_state)

    return neighbors


def bfs(start):
    queue = deque([(start, [])])
    visited = set()
    visited.add(tuple(start))

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in visited:
                visited.add(tuple(neighbor))
                queue.append((neighbor, path + [state]))

    return None


# ---------------- GUI ---------------- #
class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8 Puzzle Game")

        self.state = [1,2,3,4,5,6,7,8,0]

        self.buttons = []
        self.create_grid()

        tk.Button(root, text="Shuffle", command=self.shuffle).grid(row=4, column=0, columnspan=2, sticky="we")
        tk.Button(root, text="Solve", command=self.solve).grid(row=4, column=2, columnspan=2, sticky="we")

    def create_grid(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=("Arial", 20), width=4, height=2,
                            command=lambda i=i: self.move_tile(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)
        self.update_grid()

    def update_grid(self):
        for i in range(9):
            value = self.state[i]
            if value == 0:
                self.buttons[i].config(text="", bg="lightgray")
            else:
                self.buttons[i].config(text=str(value), bg="white")

    def move_tile(self, i):
        idx = self.state.index(0)

        # valid moves
        valid_moves = {
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4,6],
            4: [1,3,5,7],
            5: [2,4,8],
            6: [3,7],
            7: [6,4,8],
            8: [7,5]
        }

        if i in valid_moves[idx]:
            self.state[idx], self.state[i] = self.state[i], self.state[idx]
            self.update_grid()

            if self.state == goal:
                print("🎉 You solved it!")

    def shuffle(self):
        temp = self.state[:]
        for _ in range(50):
            neighbors = get_neighbors(temp)
            temp = random.choice(neighbors)
        self.state = temp
        self.update_grid()

    def solve(self):
        print("Solving... please wait")
        solution = bfs(self.state)

        if solution:
            self.animate(solution)
        else:
            print("No solution!")

    def animate(self, solution):
        def step(i):
            if i < len(solution):
                self.state = solution[i]
                self.update_grid()
                self.root.after(300, lambda: step(i+1))

        step(0)


# ---------------- RUN ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()