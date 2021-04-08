"""

Implemente uma função que dada uma sequência de inteiros, determinar o
comprimento da maior sub-sequência (não necessariamente contígua) que se
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.
case1 = [5, 2, 7, 4, 3, 8]  # 3
case2 = [15, 27, 14, 38, 26, 55, 46, 65, 85]  # 6
"""


def crescente(lista):
    length = len(lista)
    if length < 2:
        return length

    dic = {}

    def get(key):
        return dic.get(key, 1) + 1

    # upper triangular matrix with diagonal
    for i in range(1, length):
        for j in range(0, i):
            if lista[j] < lista[i] and get(i) < get(j) + 1:
                dic[i] = get(j)

    return max(dic.values(), default=1)


def espaca(frase, palavras):
    length = len(frase)
    if length < 2:
        return frase

    palavras_que_comecam_com_a_letra = {}
    palavras_possiveis_na_posicao = {}

    def get(key):
        return palavras_que_comecam_com_a_letra.get(key, 0)

    # Organize words in a dict by starting letter (prob. can be done with sort. list)
    for palavra in palavras:
        if get(palavra[0]) == 0:
            palavras_que_comecam_com_a_letra[palavra[0]] = [palavra]
        else:
            palavras_que_comecam_com_a_letra[palavra[0]].append(palavra)
            palavras_que_comecam_com_a_letra[palavra[0]].sort(reverse=True)

    # Filter words that can't be laid out from position i
    for i in range(0, length):
        palavras_possiveis_na_posicao[i] = []
        for word in palavras_que_comecam_com_a_letra.get(frase[i], []):
            if frase[i:i + len(word)] == word:
                palavras_possiveis_na_posicao[i].append(word)

    # Filter words that cause empty spaces (words that cant fill the length)
    for i in range(0, length):
        for word in palavras_possiveis_na_posicao[i]:
            if i + len(word) < length and not palavras_possiveis_na_posicao[i + len(word)]:
                palavras_possiveis_na_posicao[i].remove(word)

    # remove overlapping words
    for i in range(0, length):
        for word in palavras_possiveis_na_posicao[i]:
            for j in range(i + 1, i + len(word)):
                palavras_possiveis_na_posicao[j] = []

    return ' '.join(
        [x[0] for x in palavras_possiveis_na_posicao.values() if x != []])  # , palavras_possiveis_na_posicao



