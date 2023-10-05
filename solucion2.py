lista_pesos=list(map(int,input().split()))
peso_max=int(input("Ingrese el peso máximo por gondola:"))
gondolas=0
m=len(lista_pesos)-1

def gondolas(lista_pesos,peso_max):
    lista_pesos.sort(reverse=True)

    for i in range(len(lista_pesos)):
        if i!=m:
            peso=lista_pesos[i]+lista_pesos[m]
        if i==m:
            peso=lista_pesos[i]
        if peso>peso_max:
            gondolas+=1
        if peso<=peso_max:
            m-=1
            gondolas+=1



    


    