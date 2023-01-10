def abc(num, lenth):
    strnum = bin(num)[2:]
    while len(strnum) != lenth:
        if len(strnum) < lenth:
            strnum = '0' + strnum
    return strnum

n = int(input())
inputArr = []
for i in range(2 ** n):
    strin = input()
    inputArr.append([int(x) for x in strin.split()])

calcArr = []
lettArr = []

for i in range(n):
    lettArr.append(chr(65 + i))

for i in range(len(inputArr)):
    calcArr.append(inputArr[i][len(inputArr[i]) - 1])

if calcArr[0] == 1:
    print(1, end='')

for i in range(1, 2 ** n):
    lett = ''

    for j in range(len(calcArr) - 1):
        tempArr = calcArr
        if (tempArr[j] or tempArr[j + 1]) == 1:
            calcArr[j] = 1
        else:
            calcArr[j] = 0
    if calcArr[0] == 1:
        for k in range(len(abc(i, len(lettArr)))):
            if abc(i, len(lettArr))[k] == '1':
                lett = lett + lettArr[k]
        print(" + ", lett,  end='')
