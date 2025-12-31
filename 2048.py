def compress_and_merge(line):
    """
    Takes a list of 4 integers and applies 2048 merge rules
    in the forward direction.
    """
    # Remove zeros
    tiles = [x for x in line if x != 0]

    merged = []
    skip = False

    for i in range(len(tiles)):
        if skip:
            skip = False
            continue

        if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
            merged.append(tiles[i] * 2)
            skip = True
        else:
            merged.append(tiles[i])

    # Pad with zeros
    while len(merged) < 4:
        merged.append(0)

    return merged


def move_2048(board, direction):
    """
    board: 4x4 list
    direction:
        0 = left
        1 = up
        2 = right
        3 = down
    """
    new_board = [[0]*4 for _ in range(4)]

    if direction == 0:  # left
        for r in range(4):
            new_board[r] = compress_and_merge(board[r])

    elif direction == 2:  # right
        for r in range(4):
            reversed_row = board[r][::-1]
            merged = compress_and_merge(reversed_row)
            new_board[r] = merged[::-1]

    elif direction == 1:  # up
        for c in range(4):
            col = [board[r][c] for r in range(4)]
            merged = compress_and_merge(col)
            for r in range(4):
                new_board[r][c] = merged[r]

    elif direction == 3:  # down
        for c in range(4):
            col = [board[r][c] for r in range(4)][::-1]
            merged = compress_and_merge(col)
            merged = merged[::-1]
            for r in range(4):
                new_board[r][c] = merged[r]

    return new_board


# ---------- Input / Output ----------
board = [list(map(int, input().split())) for _ in range(4)]
direction = int(input())

result = move_2048(board, direction)

for row in result:
    print(*row)
