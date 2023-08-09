import random

def shuf(liste):
    import random
    index = len(liste) - 1
    size = len(liste)
    while size > 0:
        i = random.randint(0, size -1)
        liste[index], liste[i] = liste[i], liste[index]
        size -= 1
    return liste

def generator(text, sep=" ", option=None):
    liste = []
    if isinstance(text, str):
        if text.isprintable:
            liste = text.split(sep)
            if option == "shuffle":
                new = shuf(liste)
                return new
            elif option == "unique":
                return list(dict.fromkeys(liste))
            elif option == "ordered":
                liste.sort()
                return liste
            elif option == None:
                return liste
            else:
                print("ERROR")
                return liste
    else:
        print("ERROR")
        return liste
    



