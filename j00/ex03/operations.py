import sys

if len(sys.argv) <= 1:
    print("\tusage : python3 exe.py <nb1> <nb2>")
elif len(sys.argv) > 3:
    print("AssertionError : too many arguments")
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except:
        print("AssertionError : argument is not an integer")
        exit()
    print(f"Sum:\t    {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product:    {a * b}")
    try:
        print(f"Quotient:   {a / b}")
    except:
        print("ERROR (division by zero)")
    try:
        print(f"Remainder:  {a % b}")
    except:
        print("ERROR (modulo by zero)")    
