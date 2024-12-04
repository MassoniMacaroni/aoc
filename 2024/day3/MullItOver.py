import re

def corruptFileCheck(fileName):
    total_sum = 0
    is_enabled = True
    tokens = []
    with open(fileName) as file:
        for line in file:
            tokens.extend(re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", line))

    print(tokens)
    for token in tokens:
        if token == "do()":
            is_enabled =  True
        elif token == "don't()":
            is_enabled = False
        elif token.startswith("mul") and is_enabled:
            match = re.match(r'mul\((\d{1,3}),(\d{1,3})\)',token)
            if match:
                num1, num2 = map(int,match.groups())
                total_sum += num1 * num2



    print(total_sum)

corruptFileCheck("input.txt")
