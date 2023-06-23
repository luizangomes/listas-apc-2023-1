n,m = map(int, input().split())
Q = int(input())

lista_de_listas = []

#inicializando uma lista
for _ in range(n):
    lista_de_listas.append([0]*m)
    
for i in range(Q):
    x, y = map(int, input().split()) # recebe as coordenadas
    for i in range(n):
        for j in range(m):
            if i == (x-1):
                 lista_de_listas[i][j] += 1
            elif j == (y-1):
                lista_de_listas[i][j] += 1
    
cont = 0 
maxx = -1
for i in range(n):
    for j in range(m):
        if maxx < lista_de_listas[i][j]:
            maxx = lista_de_listas[i][j] 
for i in range(n):
    for j in range(m):
        if int(lista_de_listas[i][j]) == maxx:
            cont += 1
        
print(cont)
