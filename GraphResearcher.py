def symm(inputArr, n):
    fl = 0
    for i in range(len(inputArr)):
        pair = list(reversed(inputArr[i]))

        for j in range(i + 1, len(inputArr)):
            if pair == inputArr[j]:
                fl += 1
    if fl == 0:
        print("Антисимметричный")
    elif (n % 2 != 0) and (fl > 0):
        print("Несимметричный")
    elif n / 2 == fl:
        print("Симметричный")


def refl(inputArr, m):
    fl = False
    count = 0
    vert = [i for i in range(1, m + 1)]
    for i in range(len(inputArr)):
        pair = inputArr[i]
        if pair[0] == pair[1]:
            fl = True
            count += 1
    if (len(vert) != count) and fl:
        print("Нерефлексивный")
    elif not fl:
        print("Антирефлексивный")
    elif fl and (len(vert) == count):
        print("Рефлексивный")


def trnz(inputArr):
    fl = False
    flnot = False
    for i in range(len(inputArr)):
        for j in range(i + 1, len(inputArr)):
            pairi = inputArr[i]
            pairj = inputArr[j]
            if (pairi[1] == pairj[0]) and not (pairi[0] == pairj[1]):
                ppair = []
                ppair.append(pairi[0])
                ppair.append(pairj[1])
                if ppair in inputArr:
                    fl = True
                else:
                    flnot = True
            else:
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

symm(inputArr, infoArr[0])
refl(inputArr, infoArr[1])
trnz(inputArr)
