

if __name__ == '__main__':
    #Parte a)
    n = 2345678911111111
    inicio1=time.perf_counter()
    resultado_serial= primo(n)
    final1=time.perf_counter()
    print(final1-inicio1)
