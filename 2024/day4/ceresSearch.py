def matrixMaker(fileName):
    lRows = []
    with open(fileName) as file:
        for line in file:
            row = list(line.strip())
            lRows.append(row)

    positionMap = {}
    for row_index, row in enumerate(lRows):
        for col_index, char in enumerate(row):
            positionMap[(row_index, col_index)] = char
    return positionMap, len(lRows), len(lRows[0])


def matchCheck(x, m, a, s):
    return (x, m, a, s) == ("X", "M", "A", "S")


def xmasCount(positionMap, rows, cols):
    matches = 0

    # Vertical
    for col_index in range(cols):
        for row_index in range(rows - 3):
            if matchCheck(positionMap[(row_index, col_index)],
                          positionMap[(row_index + 1, col_index)],
                          positionMap[(row_index + 2, col_index)],
                          positionMap[(row_index + 3, col_index)]):
                matches += 1

    # Reverse Vertical
    for col_index in range(cols):
        for row_index in range(3, rows):
            if matchCheck(positionMap[(row_index, col_index)],
                          positionMap[(row_index - 1, col_index)],
                          positionMap[(row_index - 2, col_index)],
                          positionMap[(row_index - 3, col_index)]):
                matches += 1

    # Horizontal
    for row_index in range(rows):
        for col_index in range(cols - 3):
            if matchCheck(positionMap[(row_index, col_index)],
                          positionMap[(row_index, col_index + 1)],
                          positionMap[(row_index, col_index + 2)],
                          positionMap[(row_index, col_index + 3)]):
                matches += 1

    # Reverse Horizontal
    for row_index in range(rows):
        for col_index in range(3, cols):
            if matchCheck(positionMap[(row_index, col_index)],
                          positionMap[(row_index, col_index - 1)],
                          positionMap[(row_index, col_index - 2)],
                          positionMap[(row_index, col_index - 3)]):
                matches += 1

    # Diagonal (down-right)
    for row_index in range(rows - 3):
        for col_index in range(cols - 3):
            if matchCheck(positionMap[(row_index, col_index)],
                          positionMap[(row_index + 1, col_index + 1)],
                          positionMap[(row_index + 2, col_index + 2)],
                          positionMap[(row_index + 3, col_index + 3)]):
                matches += 1

    # Diagonal (down-left)
    for row_index in range(rows - 3):
        for col_index in range(3, cols):
            if matchCheck(positionMap[(row_index, col_index)],
                          positionMap[(row_index + 1, col_index - 1)],
                          positionMap[(row_index + 2, col_index - 2)],
                          positionMap[(row_index + 3, col_index - 3)]):
                matches += 1

    # Diagonal (up-right)
    for row_index in range(3, rows):
        for col_index in range(cols - 3):
            if matchCheck(positionMap[(row_index, col_index)],
                          positionMap[(row_index - 1, col_index + 1)],
                          positionMap[(row_index - 2, col_index + 2)],
                          positionMap[(row_index - 3, col_index + 3)]):
                matches += 1

    # Diagonal (up-left)
    for row_index in range(3, rows):
        for col_index in range(3, cols):
            if matchCheck(positionMap[(row_index, col_index)],
                          positionMap[(row_index - 1, col_index - 1)],
                          positionMap[(row_index - 2, col_index - 2)],
                          positionMap[(row_index - 3, col_index - 3)]):
                matches += 1

    print(matches)

def masCheck(c1, c2, c3):
    return (c1,c2,c3) == ("M", "A", "S") or (c1,c2,c3) == ("S","A","M")

def masCount(positionMap, rows, cols):
    matches = 0

    for (row, col), char in positionMap.items():
        if char == "A" and (
            row + 1 < rows 
            and col + 1 < cols 
            and row - 1 >= 0
            and col - 1 >= 0
        ):
            if masCheck(positionMap[(row-1,col-1)],
                        positionMap[(row,col)],
                        positionMap[(row+1,col+1)]) and masCheck(positionMap[(row+1,col-1)],
                         positionMap[(row,col)],
                         positionMap[(row-1,col+1)]):
                matches += 1
    print(matches) 

    

positionMap, rows, cols = matrixMaker("input.txt")
xmasCount(positionMap, rows, cols)
masCount(positionMap, rows, cols)
