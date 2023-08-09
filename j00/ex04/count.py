import sys

def text_analyzer(string = None):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    if string == None:
        string = input("What is the text to analyze?\n")
    
    string = str(string)
    if string.isnumeric():
            print("AssertionError: argument is not a string")
            exit()

    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    for i in string:
        if i.isalpha():
            if i.isupper():
                upper += 1
            else:
                lower += 1
        elif i.isspace():
            space += 1
        elif i.isprintable() and i.isnumeric() == 0:
            punctuation += 1
    print(f"The text contains {len(string)} character(s):\n- {upper} upper letter(s)\n- {lower} lower letter(s)\n- {punctuation} punctuation mark(s)\n- {space} space(s)")

if (__name__ == '__main__'):
    if len(sys.argv) == 1:
        text_analyzer()
    elif not len(sys.argv) > 2:
        text_analyzer(sys.argv[1])
    else:
        print("ERROR: too many arguments")