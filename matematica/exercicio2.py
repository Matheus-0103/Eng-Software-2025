# definição de listas
lista1 ={1, 2, 3, 4, 5}
lista2 ={4, 5, 6, 7, 8}

# contagem dos elementos
apenas_lista1 = (lista1 - lista2)
apenas_lista2 = (lista2 - lista1)
intersecao = len(lista1 & lista2)

# exibir os resultados
print("diagrama de venn (representação textual)")
print("apenas lista 1:", apenas_lista1, "elementos")
print("apenas lista 2:", apenas_lista2, "elementos")
print("interseção:", intersecao, "elementos")


