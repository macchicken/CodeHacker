multiple5 = [i * 5 for i in range(1, 21)]


def solve(grades):
    result = []
    for g in [g for g in grades if -1 < g < 101]:
        if g < 38:
            result.append(g)
        else:
            t = g
            while True:
                if g in multiple5:
                    if g - t < 3:
                        result.append(g)
                    else:
                        result.append(t)
                    break
                else:
                    g += 1
    return result


if __name__ == "__main__":
    print solve([73, 67, 38, 33])
