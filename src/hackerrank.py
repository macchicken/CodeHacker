import sys


def getsmallestpositiveint(strnum):
    if strnum is None or len(strnum) == 0:
        return 0
    i = 1
    strnum = ",{},".format(strnum)
    while True:
        if strnum.find(",{},".format(str(i))) == -1:
            return i
        else:
            i += 1


def getnumofone(inputnum):
    if inputnum is None or inputnum == 0:
        return 0
    inputnum = inputnum + 1
    counter = 0
    for i in range(1, inputnum):
        strnum = str(i)
        lennum = len(strnum)
        for j in range(lennum):
            if strnum[j] == "1":
                counter += 1
    return counter


# Values that go beyond the maximum representable usually wrap around. So, for example, if you hold 256, it will wrap around to 0, 257 will give you 1, etc, or, if your machine uses signed characters, instead of 256, max value will be 127, and 128 wraps around to the most negative value (that is, -128 with 8 bit characters, assuming a 2's complement representation). If these values happen to represent a valid printable character, then that's what you get.
# Note that it is generally not safe to assume that overflowed values wrap around: the C standard doesn't require this to happen, so, technically, a program relying on that trick has undefined behavior.
def checkanagram(str1, str2):
    if str1 is None or str2 is None:
        return 0
    len1 = len(str1)
    len2 = len(str2)
    if len1 != len2:
        return 0
    adict = {}
    bdict = {}
    for i in range(258):
        adict[i] = 0
        bdict[i] = 0
    for i in range(len1):
        adict[ord(str1[i])] += 1
        bdict[ord(str2[i])] += 1
    for akey in adict.keys():
        if adict[akey] != bdict[akey]: return 0
    return 1


if __name__ == '__main__':
    # print getsmallestpositiveint(sys.argv[1])
    # print getnumofone(int(sys.argv[1]))
    print checkanagram(sys.argv[1], sys.argv[2])
