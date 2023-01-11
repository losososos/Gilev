def symm(inputArr):
    vcount = 0
    count = 0
    for i in (inputArr):
        if i[0] != i[1]:
            count += 1
    for i in range(len(inputArr)):
        pair = list(reversed(inputArr[i]))
        for j in range(len(inputArr)):
            if pair[0] != pair[1] and pair == inputArr[j] and i != j:
                vcount += 1
    if vcount == count:
        print("Симметричный")
    elif vcount == 0:
        print("Антисимметричный")
    else:
        print("Несимметричный")


def refl(inputArr, n):
    fl = False
    count = 0
    for i in range(len(inputArr)):
        pair = inputArr[i]
        if pair[0] == pair[1]:
            fl = True
            count += 1
    if (n != count) and fl:
        print("Нерефлексивный")
    elif not fl:
        print("Антирефлексивный")
    elif fl and (n == count):
        print("Рефлексивный")


def trnz(inputArr):
    fl = False
    flnot = False
    elemArr = []
    for i in range(len(inputArr)):
        for j in range(len(inputArr)):
            pairi = inputArr[i]
            pairj = inputArr[j]
            if pairj[0] != pairj[1] and pairi[0] != pairi[1] and pairi != pairj and pairi[1] == pairj[0] and pairi[0] != pairj[1]:
                ppair = [pairi[0], pairj[1]]
                if ppair in inputArr:
                    fl = True
                    elemArr.append(pairi[0])
                    elemArr.append(pairi[1])
                    elemArr.append(pairj[1])
                else:
                    flnot = True
                if pairi[0] not in elemArr and pairi[1] not in elemArr and pairj[1] not in elemArr:
                    flnot = True
    if fl and flnot:
        print("Нетранзитивный")
    elif fl and not (flnot):
        print("Транзитивный")
    else:
        print("Антитранзитивный")


strin = input()
inputArr = []
infoArr = [int(strin.split()[0]), int(strin.split()[1])]
for i in range(infoArr[0]):
    strin = input()
    inputArr.append([int(x) for x in strin.split()])

symm(inputArr)
refl(inputArr, infoArr[1])
trnz(inputArr)
