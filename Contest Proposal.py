tcase = int(input())

for i in range(tcase):
    n = int(input())

    inputa = input().split()
    inputb = input().split()

    a = []
    b = []
    for x in inputa:
        a.append(int(x))

    for y in inputb:
        b.append(int(y))

    if len(a) == 1 and a[0] <= b[0]:
        print(0)
    elif len(a) == 1 and a[0] > b[0]:
        print(1)

    else:
        cou = 0
        tot = 0
        while cou < len(a):
            if a[cou] > b[cou]:
                a.remove(a[-1])
                a.append(b[0])
                a.sort()
                tot += 1

            else:
                cou += 1

        print(tot)