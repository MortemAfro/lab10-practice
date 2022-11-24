

    #Parte b)

    lista1=[1,2501,5001,7501]
    lista2=[2500,5000,7500,10000]

    joined_vector= zip(lista1,lista2)   
    
    inicio2= time.perf_counter()    
    p = Pool(4)             
    paralelo= p.starmap(funcion_nucleo, joined_vector)
    p.close()
    p.join()
    final2= time.perf_counter()
    tiempo2=final2-inicio2
    #print(resultado)

    suma=0
    for i in paralelo:
        suma=suma+i
    resultado_paralelo=suma
    assert (resultado_serial==resultado_paralelo)
    
    
    spped_up= tiempo1/tiempo2
    print(spped_up)
