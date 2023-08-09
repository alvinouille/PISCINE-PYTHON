class Evaluator:
    def zip_evaluate(words, coefs):
        res = 0
        sum = 0
        if len(words) != len(coefs):
            return -1
        res = zip(words, coefs)
        for i in res:
            length = len(i[0])
            sum = sum + (length * i[1])
        return sum
    
    def enumerate_evaluate(words, coefs):
        sum = 0
        if (len(words) != len(coefs)):
            return -1
        for count, value in enumerate(words):
            length = len(value)
            sum = sum + (length * coefs[count])
        return sum


if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 42.42]
    print(f"{Evaluator.zip_evaluate(words, coefs)}")
    print(f"{Evaluator.enumerate_evaluate(words, coefs)}")
