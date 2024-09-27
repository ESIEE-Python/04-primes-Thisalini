"""tester si un nombre est un nombre premier"""
from math import sqrt

####Fonction secondaire

def isprime(p):
    """dire si P est un nombre premier
    arg:p est supérieur à 1"""
    if p>1:
        for i in range (2,1+int(sqrt(p))):
            if p%i ==0:
                return False
        return True
    return False

####Fonction principale

def main():
    """Dire si p est un nombre premier
    arg : p un nombre supérieur à 1"""
    for n in range(100):
        if isprime(n):
            print(n,end=", ")
    print()

if __name__ == "__main__":
    main()
