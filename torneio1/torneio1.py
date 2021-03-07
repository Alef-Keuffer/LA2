"""

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.

"""


def formata(co):
    # Clean input
    co = " ".join(co.split())  # remove extra spaces
    co1 = (co
           .replace('{ ', '{')
           .replace("; ", ";")
           .replace(" ;", ";")
           .replace('}', '}'))
    # Find the parts that I will format
    li = [x for x in range(len(co1)) if co1[x] in {'{', ';', '}'}]
    # li = list(filter(lambda x: co1[x] in {'{', ';', '}'}, [x for x in range(len(co1))]))
    # Format those parts
    for i in range(len(li)):
        if i == 0:
            re = co1[:li[i] + 1]
        elif i < len(li):
            ind = '  ' * (co1[:li[i]].count('{') - co1[:li[i] + 1].count('}'))
            re += '\n' + ind + co1[li[i - 1] + 1: li[i] + 1]
        else:
            re += '\n' + co1[li[i - 1] + 1:]
    return re


"""

Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.

input
    d1[uc] = horario = (dia da semana, hora de inicio, duracao)
    d2[aluno] = {uc}

output
    [(aluno, total de horas semanais)]
        1. horas > horas
        2. numero < numero

ucs = {"la2": ("quarta", 16, 2), "pi": ("terca", 15, 1), "cp": ("terca", 14, 2), "so": ("quinta", 9, 3)}
alunos = {5000: {"la2", "cp"}, 2000: {"la2", "cp", "pi"}, 3000: {"cp", "poo"}, 1000: {"la2", "cp", "so"}}

ucs = {"la2": ("quarta", 16, 2), "pi": ("terca", 15, 1)}
alunos = {5000: {"la2", "pi"}, 2000: {"pi", "la2"}}
"""


def conflict(ucs):
    li = sorted(ucs.items(), key=lambda x: x[1][1])  # Sort by start time
    li.sort(key=lambda x: x[1][0])  # Sort by day
    return [li[i] for i in range(1, len(li)) if
            li[i - 1][1][0] == li[i][1][0]  # same day
            and li[i - 1][1][1] < li[i][1][1] + li[i][1][2]  # start(i-1) < end(i)
            and li[i][1][1] < li[i - 1][1][1] + li[i - 1][1][2]]  # start(i) < end(i-1)


def horario(ucs, alunos):
    # get ucs incompatible ucs pairs
    conf = conflict(ucs)
    re = []
    for aluno in alunos:
        # if uc exists and is not conflicting
        if not [x for x in alunos[aluno] if x not in ucs] \
                and not [x for x in conf if x[0] in alunos[aluno] and x[1] in alunos[aluno]]:
            re.append((aluno, sum([ucs[x][2] for x in alunos[aluno]])))
    re.sort(key=lambda x: x[0])
    re.sort(key=lambda x: x[1], reverse=True)
    return re


"""
def conflict(ucs):
    li = sorted(ucs.items(), key=lambda x: (x[1][1], x[1][2]))
    li.sort(key=lambda x: x[1][0])
    return set(filter(lambda i:
                      li[i - 1][1][0] == li[i][1][0]  # same day
                      and li[i - 1][1][1] < li[i][1][1] + li[i][1][2]  # start(i-1) < end(i)
                      and li[i][1][1] < li[i - 1][1][1] + li[i - 1][1][2]  # start(i) < end(i-1)
                      , range(1, len(li))))


def horario(ucs, alunos):
    conf = conflict(ucs)
    re = []
    for aluno in alunos:
        conflicting = list(filter(lambda x: x[0] in alunos[aluno] and x[1] in alunos[aluno], conf))
        non_existent = list(filter(lambda x: x not in ucs, alunos[aluno]))
        if not non_existent and not conflicting:
            t = sum(map(lambda x: ucs[x][2], alunos[aluno]))
            re.append((aluno, t))
    re.sort(key=lambda x: x[0])
    re.sort(key=lambda x: x[1], reverse=True)
    return re
"""

"""
def conflict(ucs):
    conf = set()
    li = sorted(ucs.items(), key=lambda x: (x[1][1], x[1][2]))
    li.sort(key=lambda x: x[1][0])
    conf2 = set(filter(lambda i: li[i - 1][1][0] == li[i][1][0] \
                                 and li[i - 1][1][1] < li[i][1][1] + li[i][1][2] \
                                 and li[i][1][1] < li[i - 1][1][1] + li[i - 1][1][2], range(1,len(li))))
    for i in range(1, len(li)):
        if li[i - 1][1][0] == li[i][1][0]:
            if li[i - 1][1][1] < li[i][1][1] + li[i][1][2] and li[i][1][1] < li[i - 1][1][1] + li[i - 1][1][2]:
                conf.add((li[i - 1][0], li[i][0]))
    return conf2
"""
