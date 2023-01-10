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
        print("Антитранзитивный")
    elif fl and not (flnot):
        print("Нетранзитивный")
    else:
        print("Транзитивный")


strin = input()
inputArr = []
infoArr = [int(strin.split()[0]), int(strin.split()[1])]
for i in range(infoArr[0]):
    strin = input()
    inputArr.append([int(x) for x in strin.split()])

symm(inputArr, infoArr[0])
refl(inputArr, infoArr[1])
trnz(inputArr)
