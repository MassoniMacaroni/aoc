def splitIntoLists(fileName):
    col1 = []
    col2 = []

    with open(fileName) as file:
        for line in file:
            col1Val, col2Val = line.split()
            col1.append(col1Val)
            col2.append(col2Val)

    col1.sort()
    col2.sort()

    return col1,col2

def differenceFinder(col1,col2):
    difference = 0
    for i in range(len(col1)):
       difference += abs(int(col1[i]) - int(col2[i]))
    print("difference: ",difference)


def similarityFinder(col1,col2):
    similarity = 0
    for num1 in col1:
        for num2 in col2:
            if num1 == num2:
                similarity += int(num2)
    print("similarity: ",similarity)

differenceFinder(*splitIntoLists("input.txt"))
similarityFinder(*splitIntoLists("input.txt"))
