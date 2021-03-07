"""

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.

"""


def formata(co):
    # Clean input
    co1 = (" ".join(co.split())
           .replace('{ ', '{')
           .replace("; ", ";")
           .replace(" ;", ";")
           .replace('} ', '}'))
    # Find the parts that I will format
    li = [x for x in range(len(co1)) if co1[x] in {'{', ';', '}'}]
    # li = list(filter(lambda x: co1[x] in {'{', ';', '}'}, [x for x in range(len(co1))]))
    # Format those parts
    re = co1
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

"""


def conflict(ucs):
    li = sorted(ucs.items(), key=lambda x: x[1][1])  # Sort by start time
    li.sort(key=lambda x: x[1][0])  # Sort by day
    return [(li[i - 1][0], li[i][0]) for i in range(1, len(li)) if
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
