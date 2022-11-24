import math
import time
from multiprocessing import Pool
import matplotlib.pyplot as plt

def primo(numero):

    raiz_n = math.sqrt(numero)
    maximo = math.floor(raiz_n)
    primo=0
    for i in range(2,maximo+1):
        if (numero % i == 0):
            primo = primo + 1
    if (primo==0 and numero>1) :
        return True
    else:
        return False


def funcion_nucleo(a,b):
    x=2345678911111111
    sumatoria=0
    for i in range(a,b+1):
        sumatoria = sumatoria + i*(pow(x,i))
    
    return sumatoria
