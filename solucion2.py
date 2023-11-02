 
def gondola(niños,peso_max):
    niños.sort()
    l=len(niños)
    inicio=0
    final=l-1
    gondolas=0


    while inicio<=final:

        if inicio==final:
            gondolas+=1
            final-=1

        if niños[inicio]+niños[final]<=peso_max:
            inicio+=1
            final-=1
            gondolas+=1

        else:
            final-=1
            gondolas+=1



    


    
