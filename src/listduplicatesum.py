import time


def duplicatelistsum(arr):
    if arr[0] == 0:
        return 0
    elif arr[0] == 1:
        return arr[1]
    seen, duplicates, uniques = [], [], []
    for a in arr[1:]:
        if a not in seen:
            c = arr[1:].count(a)
            if c > 1:
                seen.append(a)
                duplicates.append((a, c))
            else:
                uniques.append(a)
    for (d, c) in duplicates:
        for ic in range(c):
            t = d + 1
            while t in uniques:
                t += 1
            uniques.append(t)
    print uniques
    return sum(uniques)


if __name__ == "__main__":
    for i in range(5):
        time.sleep(2)
        print duplicatelistsum([4, 1, 2, 2, 4])
