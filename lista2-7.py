n, m, k = map(int, input().split()) #jogadores, empresarios, equipes
atletas = list(map(int, input().split()))
empresarios = list(map(int, input().split())) # número de times que os empresários estão gerenciando
empresario = [] # onde vou guardar cada (atleta x time) que pertence
empresarios_roubados = []
for i in range(m):
    empresario.append([])
for i in range(m):
    emp = list(map(int, input().split()))
    for j in emp:
        empresario[i].append(atletas[(j-1)])
equipes = [x+1 for x in range(k)] # compreensão de listas que vai criar uma listinha com os números dos times possíveis
for i in range(m):
    notduplicates = []
    [notduplicates.append(x) for x in empresario[i] if x not in notduplicates] # vai retirar as duplicatas dos times, só para contarmos os times presentes em cada gerenciamento
    c = 0
    for j in notduplicates:
        if j in equipes:
            c += 1
    if c == k:
        empresarios_roubados.append(i+1)
            
if len(empresarios_roubados) == 0:
    print("-1")
else:
    empresarios_roubados = list(map(str, empresarios_roubados))
    print(" ".join(empresarios_roubados))
