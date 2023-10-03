#queremos encontrar todos los números distintos que hay en una lista  sin emplear sets, listas , etc

asistencia=int(input("Asistentes en la sala:"))
l=list(map(int,input().split()))

def pasar_lista():
    asistentes=0
    l.sort()
    for i in range(len(l)-1):
        if l[i]!=l[i+1]:
            asistentes+=1
    asistentes+=1#tenemos que sumar siempre uno del ultimo  elemento
    return asistentes
