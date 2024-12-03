from collections import defaultdict


def day01_1(content: str ):
    list1 = []
    list2 = []
    delta = []
    for i in content.splitlines():
        a,b = i.split()
        list1.append(int(a))
        list2.append(int(b))
    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        delta.append(abs(int(list1[i]) - int(list2[i])))

    return sum(delta)

def day01_2(content: str ):
    list1 = []
    freq2 = defaultdict(int)
    for i in content.splitlines():
        a, b = i.split()
        list1.append(a)
        freq2[b] += 1

    similarityScore = 0
    for e in list1:
        print(e, freq2[e])
        similarityScore += int(e)*freq2[e]

    return similarityScore







