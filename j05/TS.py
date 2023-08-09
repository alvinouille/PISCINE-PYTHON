import math

class TS:
    def mean(self, liste):
        n = 1 / len(liste)
        moy = n * sum(liste)
        return float(moy)
    
    def rang_med(self, liste, x):
        n = len(liste)
        if n % x != 0:
            return int((n + 1)/x)
        else:
            rang1 = n / x -1
            rang2 = n / x + 1
            return int(rang1), int(rang2)
    def median(self, liste):
        sorted_liste = sorted(liste)
        n = len(liste)
        if n % 2 != 0:
            return float(sorted_liste[self.rang_med(liste, 2) -1])
        else:
            val1, val2 = sorted_liste[self.rang_med(liste, 2) -1]
            return float((val1 + val2) / 2)
    
    def quartile(self, liste):
        sorted_liste = sorted(liste)
        n = len(liste)
        new = []
        q1 = sorted_liste[int(math.ceil(len(liste) /4 -1))]
        q2 = sorted_liste[int(math.ceil(len(liste) /4 *3 -1))]
        new.append(float(q1))
        new.append(float(q2))
        return new
    
    def percentile(self, liste, prc):
        sorted_liste = sorted(liste)
        n = len(liste)
        new = []
        p1 = sorted_liste[int(math.ceil(len(liste) / 100 * prc))]
        p2 = sorted_liste[int(math.floor(len(liste) / 100 * prc))]
        return (p1 + p2)/2
    
    def var(self, liste):
        n = len(liste)
        sum = 0
        mean = self.mean(liste)
        for nb in liste:
            print(mean, nb, sum)
            sum += (nb - mean) **2
        return float(sum / n)
    
    def std(self, liste):
        return (self.var(liste))**(1 / 2)

if __name__== '__main__':
    tstat = TS()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    print(tstat.median(a))
    print(tstat.quartile(a))
    print(tstat.percentile(a, 10))
    print(tstat.percentile(a, 15))
    print(tstat.percentile(a, 20))
    print(tstat.var(a))
    print(tstat.std(a))

    