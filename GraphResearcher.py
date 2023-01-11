def symm(inputArr, n):
    fl = 0
    for i in range(len(inputArr)):
        pair = list(reversed(inputArr[i]))
        for j in range(len(inputArr)):
            if pair == inputArr[j] and i != j:
                fl += 1
    if float(fl) == float(n) / 2:
        print("Симметричный")
    elif fl == 0:
        print("Несимметричный")
    else:
        print("Антисимметричный")


def refl(inputArr, n):
    fl = False
    count = 0
    for i in range(len(inputArr)):
        pair = inputArr[i]
        if pair[0] == pair[1]:
            fl = True
            count += 1
    if (n != count) and fl:
        print("Антирефлексивный")
    elif not fl:
        print("Нерефлексивный")
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
            if (pairj[0] != pairj[1]) and (pairi[0] != pairi[1]) and (pairi[1] == pairj[0]) and (pairi[0] != pairj[1]):
                ppair = [pairj[1], pairi[0]]
                if ppair in inputArr:
                    fl = True
                    elemArr.append(pairi[0])
                    elemArr.append(pairi[1])
                    elemArr.append(pairj[1])
                elif (pairj[0] != pairj[1]) and (pairi[0] != pairi[1]) and (pairi != pairj):
                    flnot = True
                print(pairi, pairj, ppair, fl, flnot)
            elif pairi[0] not in elemArr and pairi[1] not in elemArr and pairj[1] not in elemArr and (
                    pairj[0] != pairj[1]) and (
                    pairi[0] != pairi[1]) and (pairi != pairj):
                flnot = True
                print(pairi, pairj, fl, flnot)

    if fl and flnot:
        print("Антитранзитивный")
    elif fl and not (flnot):
        print("Транзитивный")
    else:
        print("Нетранзитивный")


strin = input()
inputArr = []
infoArr = [int(strin.split()[0]), int(strin.split()[1])]
for i in range(infoArr[0]):
    strin = input()
    inputArr.append([int(x) for x in strin.split()])

symm(inputArr, infoArr[0])
refl(inputArr, infoArr[1])
trnz(inputArr)
