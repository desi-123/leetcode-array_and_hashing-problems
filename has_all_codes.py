def hasAllCodes(s, k):
    codeSet = set()

    for i in range(len(s) - k + 1):
        codeSet.add(s[i: i + k])

    return len(codeSet) == 2 ** k