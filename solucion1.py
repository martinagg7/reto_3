asistentes = 182909303
asistentes_str=str(asistentes )
asistentes_distintos=0
for i in range(len(asistentes_str)-1):
    if(asistentes_str[i])!=(asistentes_str[i+1]):
        asistentes_distintos+=1

asistentes_distintos+=1
print(asistentes_distintos)
