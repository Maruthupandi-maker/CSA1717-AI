# Simple two-player Tic Tac Toe
board = [" "] * 9
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
moves = [0, 4, 1, 3, 2]  # Sample moves: X wins across the top row

def show():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6: print("--+---+--")

print("TIC TAC TOE - SAMPLE GAME")
for turn, pos in enumerate(moves):
    mark = "X" if turn % 2 == 0 else "O"
    board[pos] = mark
    print(f"Move {turn+1}: {mark} at cell {pos+1}")
    if any(all(board[i] == mark for i in line) for line in wins):
        print(f"Player {mark} wins!")
        break
show()
