conj1 = {1, 2, 3, 4}
conj2 = {3, 4, 5, 6}

print("Primeiro conjunto: ", conj1)
print("Segundo conjunto: ", conj2)

uniao = conj1.union(conj2)
intersec = conj1.intersection(conj2)
difer = conj1.difference(conj2)

print("Resultado a união: ", uniao)
print("Resultado a intersecção: ", intersec)
print("Resultado a diferença: ", difer)