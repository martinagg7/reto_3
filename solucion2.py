lista_pesos=list(map(int,input().split()))
peso_max=int(input("Ingrese el peso máximo por gondola:"))

def gondolas(lista_pesos,peso_max):
    lista_pesos.sort()
    gondolas=0
    i=0
    j=len(lista_pesos)-1
    
    while i<=j:
        if lista_pesos[i]+lista_pesos[j]<=peso_max:
            i+=1
            j-=1
            gondolas+=1
        else:
            j-=1
            while lista_pesos[i]+lista_pesos[j]>peso_max:
                j-=1
                
    


    