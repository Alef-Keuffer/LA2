from math import floor, sqrt

"""Neste problem pretende-se que defina uma função que, dada uma string com palavras,devolva uma lista com as 
palavras nela contidas ordenada por ordem de frequência,da mais alta para a mais baixa. Palavras com a mesma 
frequência devem ser listadaspor ordem alfabética. """


def frequencia(text):
    text = text.split()
    s = list(set(text))
    s.sort(key=str.lower)  # use s.sort() to get points in codeboard
    s.sort(key=text.count, reverse=True)
    return s


"""
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
"""


def repete(word, n):
    if n == 0:
        return ''
    if len(set(word)) == 1:
        return word + word[0] * (n - 1)
    i = 0
    j = len(word) - 1
    while i <= j:
        if word[i] == word[j]:
            j -= 1
        i += 1
    return word[0:i] * n + word[i:]


"""
Pretende-se que implemente uma função que detecte códigos ISBN inválidos.
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos,
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
"""


def soma(text):
    text = list(map(int, text))
    s = 0
    for i in range(len(text)):
        if i % 2 == 0:
            s += text[i]
        else:
            s += 3 * text[i]
    return s % 10 == 0


def isbn(livros):
    d = []
    for x in livros.items():
        if not soma(x[1]):
            d.append(x)
    d = list(map(lambda s: s[0], d))
    d.sort(key=str.lower)
    return d


"""
Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto,
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.
"""


def aloca(prefs):
    unnavailable = set()
    deallocated = []
    for student in sorted(prefs.keys()):
        # Did line 22 based on:
        # https://stackoverflow.com/questions/58785493/stop-loop-with-list-comprehension-when-find-the-first-true
        # Didn't want to use list comprehension, but didn't know an alternative.
        # Later, I read the documentation on next.
        project = next(
            filter(lambda x: x not in unnavailable, prefs[student]), None)
        if project == None:
            deallocated.append(student)
        else:
            unnavailable.add(project)
    return deallocated


"""Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada por ordem crescente do 
número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos, 
devem ser listadas por ordem lexicográfica do nome completo. 


Apelidos como Castelo Branco ou Paço de Arcos devem contar como um só?
"""


# Vi resolução de Pedro Pereira
# Não pensei em forma mais simples de resolver


def apelidos(nomes):
    nomes.sort(key=str.lower)
    nomes.sort(key=lambda completo: len(completo.split()))
    return nomes


"""
Podemos usar um (multi) grafo para representar um mapa de uma cidade:
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos).

Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome. 

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, listando para 
cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga. 

Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com
"""


def cruzamentos(ruas):
    c = {}
    for x in ruas:
        if x[0] not in c:
            c[x[0]] = 0
        if x[-1] not in c:
            c[x[-1]] = 0
        if x[0] == x[-1]:
            c[x[0]] -= 1
        c[x[0]] += 1
        c[x[-1]] += 1
    d = sorted(c.items(), key=lambda s: (s[0]))
    return sorted(d, key=lambda s: (s[1]))


"""
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
"""


def trial_div(n):
    # Adapted from "Fundamentals of Algorithmics"
    if n % 2 == 0:
        return 2
    m = 3
    while m <= floor(sqrt(n)):
        if n % m == 0:
            return m
        m += 2
    return n


def factoriza(n):
    if n < 2:
        return 0
    t = 0
    f = trial_div(n)
    while n != 1:
        t += f
        while n % f == 0:
            n //= f
        f = trial_div(n)
    return t


"""
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita
  'H' - parar e regressar à posição inicial virado para cima

Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, 
máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo onde se movimentou desde o início da sequência 
de comandos ou desde o último comando 'H'. 

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
"""


def update_minmax(m, p):
    m[0] = min(m[0], p[0], p[2])  # minx
    m[1] = min(m[1], p[1], p[3])  # miny
    m[2] = max(m[2], p[0], p[2])  # maxx
    m[3] = max(m[3], p[1], p[3])  # maxy


def robot(comandos):
    v = [0, 1]  # direction vector
    p = [0, 0, 0, 0]  # p[0:2] = current position, p[2:4] = start position
    m = [0, 0, 0, 0]  # min-max vector
    s = []
    for d in comandos:
        if d == "H":
            s.append(tuple(m))
            v = [0, 1]
            p = [0, 0, 0, 0]
            m = [0, 0, 0, 0]
        if d == "A":
            p = [p[0] + v[0], p[1] + v[1], p[2], p[3]]
            update_minmax(m, p)
        if d == "E":
            v = [-v[1], v[0]]
        if d == "D":
            v = [v[1], -v[0]]
    return s


"""
Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.
"""


def is_in_dictionary(t, s, p):
    if t[0] not in s:
        s[t[0]] = 0
        p[t[0]] = 0
    if t[2] not in s:
        s[t[2]] = 0
        p[t[2]] = 0


def tabela(jogos):
    s = {}  # score
    p = {}
    for t in jogos:
        is_in_dictionary(t, s, p)
        p[t[0]] += t[1] - t[3]
        p[t[2]] += t[3] - t[1]
        if t[1] > t[3]:
            s[t[0]] += 3
        elif t[1] < t[3]:
            s[t[2]] += 3
        else:
            s[t[0]] += 1
            s[t[2]] += 1

    table = sorted(s.items(), key=lambda x: x[0].lower())
    table.sort(key=lambda x: p[x[0]], reverse=True)
    table.sort(key=lambda x: s[x[0]], reverse=True)
    return table


"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""


def merge(old, new):
    merged = ""
    if len(old) != len(new):
        return new  # Contradição
    for old, new in zip(old, new):
        merged += new if new != "*" else old
    return merged


def num_of_revealed_char(s):
    return len(list(filter(lambda x: x != '*', s)))


def hacker(log):
    p = {}
    for x in log:
        if x[1] in p:
            p[x[1]] = merge(p[x[1]], x[0])
        else:
            p[x[1]] = x[0]
    r = sorted(p.items(), key=lambda s: s[0])  # r = sorted(p.items(), key=lambda x: x[0].lower())
    r = sorted(
        [(x[1], x[0]) for x in r],
        key=lambda s: num_of_revealed_char(s[0]),
        reverse=True)
    # r.sort(key = lambda x: num_of_revealed_char(x[1]), reverse = True)
    return r
