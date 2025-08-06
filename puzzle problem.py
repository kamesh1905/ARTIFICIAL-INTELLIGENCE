from collections import deque

goal = "123456780"  # Goal as string, 0 is the blank

# Moves: up, down, left, right
moves = {
    0: [1, 3],       1: [0, 2, 4],      2: [1, 5],
    3: [0, 4, 6],    4: [1, 3, 5, 7],   5: [2, 4, 8],
    6: [3, 7],       7: [4, 6, 8],      8: [5, 7]
}

def bfs(start):
    start = ''.join(str(num) for row in start for num in row)
    visited = set()
    queue = deque([(start, [])])

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]

        visited.add(state)
        zero = state.index('0')

        for move in moves[zero]:
            lst = list(state)
            lst[zero], lst[move] = lst[move], lst[zero]
            new_state = ''.join(lst)

            if new_state not in visited:
                queue.append((new_state, path + [state]))

    return None

# Example
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = bfs(start_state)

for state in solution:
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print("---")
