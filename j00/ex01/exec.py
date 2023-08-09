import sys

res = ""
i = len(sys.argv) -1
if len(sys.argv) == 1:
    print("\tusage: python3 exec.py string1 string2")
elif len(sys.argv) >= 2:
    while i > 0:
        res = res + "".join(reversed(sys.argv[i]))
        i = i - 1
        if i != 0:
            res = res + " "
    res = res.swapcase()
    print(res)
