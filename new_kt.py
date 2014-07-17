def select(L, j):
    if len(L) < 10:
        L.sort()
        return L[j]
    S = []
    lIndex = 0
    while lIndex+5 < len(L)-1:
        S.append(L[lIndex:lIndex+5])
        lIndex += 5
    print lIndex
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        Meds.append(select(subList, int((len(subList)-1)/2)))
    med = select(Meds, int((len(Meds)-1)/2))
    L1 = []
    L2 = []
    L3 = []
    for i in L:
        if i < med:
            L1.append(i)
        elif i > med:
            L3.append(i)
        else:
            L2.append(i)
    if j < len(L1):
        return select(L1, j)
    elif j < len(L2) + len(L1):
        return L2[0]
    else:
        return select(L3, j-len(L1)-len(L2))
a = [1,2,3,4,4,5,6,12,17,20]
print select(a,3)