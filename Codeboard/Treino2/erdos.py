'''13
O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em
pareceria com outros autores.

O número de Erdos de Paul Erdos é 0.

Para qualquer outro autor, o seu número de Erdos é igual ao menor
número de Erdos de todos os seus co-autores mais 1.

forall a in U\{'Paul Erdos'}: EN(a) = min(map(EN,CO[a])) + 1

Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado
valor.

A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.

'''

def erdos(art,limit):
    art1 = [x for x in art.values()]
    en = {'Paul Erdos':0}
    s = {'Paul Erdos'}
    b = next(filter(lambda x: x.intersection(s) != set() and x.intersection(s)!=x,art1),None)
    while b:
        for a in b:
            if a not in s:
                en[a] = en[min(b,key=lambda x: en.get(x,float('inf')))] + 1
                s.add(a)
        b = next(filter(lambda x: x.intersection(s) != set() and x.intersection(s)!=x,art1),None)
    return sorted(sorted(list(filter(lambda x: en[x] <= limit,en.keys())),key = lambda x: str.lower(x) ),key=lambda x:en[x])