#!/bin/python


def averybigsum(n, ar):
    nar, maxi = [], -1
    for i in range(n):
        t = [int(x) for x in str(ar[i])]
        lt = len(t)
        if maxi < lt: maxi = lt
        nar.append((t, lt))
    count, increment, result = 0, 0, []
    for i in range(maxi):
        sumi = 0
        count += 1
        for (n, l) in nar:
            index = l - count
            if index > -1: sumi += n[index]
        sumi += increment
        reminder = sumi % 10
        increment = sumi / 10
        result.append(str(reminder))
    if increment > 0: result.append(str(increment))
    return "".join(result[::-1])


if __name__ == "__main__":
    print averybigsum(5, map(long, "1000000001 1000000002 1000000003 1000000004 1000000005".strip().split(' ')))
