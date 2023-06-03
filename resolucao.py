def decimal2bin(n):
    code = bin(n)
    code = code[2:]
    code = code.zfill(8)
    return str(code)

def reverse(s):
    rev = s[::-1]
    return rev

# Essa função vai decodificar, encontrar quem é o *1* e quem é o *0* da Direita pra Esquerda, padrão Little Endian
def decodifica(codeBinario, codeUnario):
    decimal = len(codeUnario)
    if decimal % 2 == 0:
        # Se o resto é zero, então começamos na primeira posição pois é um número par:
        # a primeira posição da direita a esquerda: 2**0 == 1 deve ser igual a 0.
        zero = codeBinario[len(codeBinario)-1]
        for i in codeBinario:
            if i != zero:
                um = i
                break
    else:
        # Se o resto é um, então começamos na primeira posição pois é um número ímpar:
        # a primeira posição da direita a esquerda 2**0 == 1 deve ser igual a 1.
        um = codeBinario[len(codeBinario)-1]
        for i in codeBinario:
            if i != um:
                zero = i
                break
    return zero, um
    
def converte2alien(zero, um, code):
    decimal = int(code)
    binário = decimal2bin(decimal)
    alien = ""
    for i in binário:
        if i == "0":
            alien += zero
        elif i == "1":
            alien += um
    return alien

def converte2decimal(zero, um, code):
    decimal = "0b"
    for i in code:
        if i == zero:
            decimal += "0"
        elif i == um:
            decimal += "1"
    return int(decimal, 2)

def isBigEndian(códigoBinárioAlien, códigoUnárioAlien):
    decimal = len(códigoUnárioAlien)
    if decimal % 2 == 0:
        zero = códigoBinárioAlien[len(códigoBinárioAlien)-1]
        for i in códigoBinárioAlien:
            if i != zero:
                um = i
                break
    else:
        um = códigoBinárioAlien[len(códigoBinárioAlien)-1]
        for i in códigoBinárioAlien:
            if i != um:
                zero = i
                break
    binario = "0b"
    for i in códigoBinárioAlien:
        if i == zero:
            binario += "0"
        elif i == um:
            binario += "1"
    #checa se a conversão tá correta   
    if int(binario, 2) != decimal:
        return True
    if int(binario, 2) == decimal:
        return False   
    
def BigEndian2LittleEndian(códigoBinárioAlien):
    return reverse(códigoBinárioAlien)

def LittleEndian2BigEndian(códigoBinárioAlien):
    return reverse(códigoBinárioAlien)
    
códigoBinário, códigoUnário = input().split()
n = len(códigoUnário)
bigEndian = isBigEndian(códigoBinário, códigoUnário)
if bigEndian:
    códigoBinário = BigEndian2LittleEndian(códigoBinário)
zero, um = decodifica(códigoBinário, códigoUnário)
# Lembrando que:
##### Direita -> Esquerda ===> Little Endian
##### Esquerda -> Direita ==> Big Endian
# Se for Little Endian não mexemos, mas se for mexemos pra inverter a leitura do código,
# e na hora de imprimir deveríamos também de forma reversa, pois tratamos o código sempre como little endian
for i in range(n):
    code = input()
    if code.isdigit():
        if bigEndian:
            # Precisamos inverter o código que recolhemos, pois estamos sempre fazendo os códigos em Little Endian
            print(BigEndian2LittleEndian(converte2alien(zero, um, code)))
        else:
            print(converte2alien(zero, um, code))
    else:
        if bigEndian:
            # Precisamos inverter o código que recolhemos, pois estamos sempre fazendo os códigos em Little Endian
            code = BigEndian2LittleEndian(code)
            print(converte2decimal(zero, um, code))
        else:
            print(converte2decimal(zero, um, code))
