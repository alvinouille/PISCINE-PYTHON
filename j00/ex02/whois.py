import sys

if len(sys.argv) <= 1:
    print("\tusage : python3 exe.py nb")
elif len(sys.argv) > 2:
    print("AssertionError : more than one argument are provided")
else:
    try:
        nb = int(sys.argv[1])
    except:
        print("AssertionError : argument is not an integer")
    else:
        if nb == 0:
            print("I'm Zero.")
        else:
            print("I'm Even.") if nb % 2 == 0 else print("I'm Odd.")

