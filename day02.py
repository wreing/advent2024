from types import NoneType

def getSafeArray(reports):
    r = []
    for levels in reports.splitlines():
        curR = 0
        curD = ''
        levels = levels.split()
        for i in range(len(levels)):
            # if first element pass
            if i == 0:
                pass
            if i == 1:
                j = 0
                a, b = int(levels[j]), int(levels[i])
                if a < b:
                    curD = 'i'
                elif a > b:
                    curD = 'd'
            if i > 0 :
                a, b = int(levels[j]), int(levels[i])
                if abs(a - b) < 1 or abs(a - b) > 3:
                    curR += 1
                    j = j - 1
                elif a > b and curD == 'i':
                    curR += 1
                    j = j - 1
                elif a < b and curD == 'd':
                    curR += 1
                    j = j - 1
                j = j + 1
        r.append(curR)
    return r


def isSafe(report):
    """Check if a report is safe based on the original rules."""

    # Increasing
    if all( 1 <= int(report[i + 1]) - int(report[i]) <= 3 for i in range(len(report)-1)):
        return True

    # Decreasing
    if all( -1 >= int(report[i + 1]) - int(report[i]) >= -3 for i in range(len(report)-1)):
        return True

    return False

def isSafeRemoveOne(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if isSafe(modified_report):
            return True
    return False




def day02_1(reports: str ):
    r = getSafeArray(reports)
    print(r)
    return r.count(0)

def day02_2(reports: str ):
    ct = 0
    for r in reports.splitlines():
        if isSafe(r.split()) or isSafeRemoveOne(r.split()):
            ct += 1
    return ct
