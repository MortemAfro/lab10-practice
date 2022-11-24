

if __name__ == '__main__':
    #Parte a)
    n = 2345678911111111
    inicio1=time.perf_counter()
    resultado_serial= primo(n)
    final1=time.perf_counter()
    print(final1-inicio1)

    #Parte B)

    #debo hallar si en el rango a,b hay un primo del numero
    raiz_n = math.sqrt(n)
    maximo = math.floor(raiz_n)

    a = maximo/2
    a = math.floor(a)

    lista1=[2,a]
    lista2 = [a+1,maximo]

    joined_vector = zip(lista1,lista2)

    inicio_paralelo1 = time.perf_counter()
    p = Pool(2)
    paralelo1 = p.starmap(funcion_nucleo, joined_vector)
    p.close()
    p.join()
    final_paralelo1= time.perf_counter()
    print(f"Tiempo de ejecución paralelo 2 procesos: {final_paralelo1-inicio_paralelo1} segundos")

    speedup1= (final1-inicio1)/(final_paralelo1-inicio_paralelo1)
    print(f"El speedup es: {speedup1}")
    
    if False in paralelo1:
      resultado_paralelo1 = False
    else:
      resultado_paralelo1 = True
    assert (resultado_serial==resultado_paralelo1)
