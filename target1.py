def funcion(x):
    sumatoria=0
    for i in range(1,10001):
        sumatoria= sumatoria + i*(pow(x,i))
    
    return sumatoria

def funcion_nucleo(a,b):
    x=2022
    sumatoria=0
    for i in range(a,b+1):
        sumatoria = sumatoria + i*(pow(x,i))
    
    return sumatoria
