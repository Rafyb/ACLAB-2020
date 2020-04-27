def Ligne(file):
    line = file.readline()
    if not line:
        exit()
    return line.strip()

def Donnee(S, N, L):
    if S > 10 or N > 10:
        return 0

    i = 0
    while i < len(L):
        if int(L[i]) > 100:
            return 0
        i = i + 1

    if (len(L) - 1) != int(L[0]):
        return 0

    return 1

def Combinations(res, stamps):
    list = []
    for elem in res:
        for stamp in stamps:
            list.append(elem + ' ' + stamp)
    return list

def PossibleCombination(number, orderedList):
    values = orderedList.split()
    values = [int(i) for i in values]
    if number == sum(values):
        return True
    return False

def FindMaxCoverage(maxStamps, setsOfStamps, stamps):
    coverage = 0
    i = 2
    j = 1
    del(stamps[0])
    res = stamps
    allCombinations = []
    allCombinations.append(res)
    while i < maxStamps + 1:
        while j < i:
            res = Combinations(res, stamps)
            j = j + 1
        allCombinations.append(res)
        i = i + 1
    i = 1
    while True:
        possible = False
        j = 0
        while j < len(allCombinations) and possible is False:
            k = 0
            while k < len(allCombinations[j]):
                if PossibleCombination(i, allCombinations[j][k]) is True:
                    possible = True
                k = k + 1
            j = j + 1
        if possible is False:
            return i - 1
        i = i + 1
    return 0

def Stamps(filename):
    file = open(filename, 'r')

    while True:
        coverage = 0
        case = 1
        max = 0
        while case == 1:
            maxStamps = int(Ligne(file))
            setsOfStamps = int(Ligne(file))
            while setsOfStamps > 0:
                stamps = Ligne(file).split()
                if Donnee(maxStamps, setsOfStamps, stamps) == 0:
                    print('Donnees erronnees')
                    break
                tmp = FindMaxCoverage(maxStamps, setsOfStamps, stamps)
                if tmp >= max:
                    max = tmp
                setsOfStamps = setsOfStamps - 1
            print("")
            print"max coverage = " + str(max) + " : ",
            for val in stamps:
                print val,
            case = case + 1
Stamps('test.txt')