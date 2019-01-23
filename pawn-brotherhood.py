def safe_pawns(pawns):
    ploc = set()
    safeCount = 0
    for p in pawns:
        row  = int(p[1]) - 1
        col = ord(p[0]) - 97
        ploc.add((row, col))
    for row, col in ploc:
        safe = safe = any(((row - 1, col - 1) in ploc, (row - 1, col + 1) in ploc))
        if safe:
            safeCount += 1
    return safeCount  