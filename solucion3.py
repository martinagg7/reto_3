secuencia= map(list(int, input().split()))

# en una variable llamada "total_peliculas" guardamos el primer elemento del int que representa el número de películas totales
total_peliculas = secuencia[0]

#  listas vacías"I" y "F" que representan respectivamente las horas de inicio y la de final de cada pelicula
I = []
F = []
for i in range(1, len(secuencia), 2):
    I.append(secuencia[i])
    if i + 1 < len(secuencia):
        F.append(secuencia[i + 1])

# ordenamos las listas "I" y "F" de menor a mayor
I.sort()#hora de inicio de la pelicula
F.sort()#hora final

contador_general_peliculas = 1#suponemos que minimo podemos ver una

for i in range (len(I)-1):
    I=I[i+1]
    F=F[i]
    c=i+1
    contador_aux=1
    while c<=len(I):
        if (I<F):
            c+=1
        if (I>=F):
            F=F[c]
            c+=1
            contador_aux+=1
        if c<=len(I):
            I=I[c]
        if contador_aux>contador_general_peliculas:
            contador_general_peliculas=contador_aux
print(contador_general_peliculas)