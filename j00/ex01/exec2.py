import sys

res = ""
if len(sys.argv) >= 2:
    for i in sys.argv[:0:-1]:
        res = res + i[::-1]
        if i != sys.argv[1]:
            res = res + " "
    print(res.swapcase())
