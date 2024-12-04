def validReportCount(fileName):
    safeReports = 0
    with open(fileName) as file:
        for line in file:
            report = list(map(int, line.split()))
            if reportValidator(report):
                safeReports += 1
    return safeReports

def reportValidator(report):
    if not report:
        return False

    # Check the report as-is
    if isSafe(report):
        return True

    # Simulate removing each level
    for i in range(len(report)):
        modifiedReport = report[:i] + report[i+1:]  # Remove the level at index i
        if isSafe(modifiedReport):
            return True

    return False


def isSafe(report):
    if not report:
        return False

    ascending = True
    descending = True
    validDifference = True

    previous = report[0]
    for num in report[1:]:
        if num < previous:
            ascending = False
        if num > previous:
            descending = False
        if abs(num - previous) < 1 or abs(num - previous) > 3:
            validDifference = False
        previous = num

    return (ascending or descending) and validDifference


print(validReportCount("input.txt"))

