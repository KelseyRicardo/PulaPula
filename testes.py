fila = ["carlos", "dora", "alex"]
print(fila)
fila.pop(0)
print(fila)
fila.remove("dora")
print(fila)
fila = dict()
print(fila)
fila["carlos"] = 5
print(fila)
lista = ["carlos", "t2"]
n = fila[lista[0]]
print("teste", n)
fila["carlos"] = 5.5 + n
print("teste2 ", fila["carlos"])
fila["carlos"] += 5.5
print("teste3 ", fila["carlos"])
print(fila.get("carlos"))
print(fila["carlos"]+5.5)
print(fila.keys())
print(list(fila.keys()))
lista1 = ["dudu", "carlos"]
if  "dudu" in lista1:
    print("True")
if lista1[0] not in fila.keys():
    print("True")
else: print("False")
