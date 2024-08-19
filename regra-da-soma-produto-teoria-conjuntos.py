#regra da soma teoria dos conjuntos
#aplicado quando se quer verificar a se um elemento ou outro elemento pertencente à conjunto, de acordo com a Cardinalidade dos elementos. Em probabilidades se verifica a ocorrência de um ou outro elemento
A ={4, 9,10,2}
B ={6, 15,2,8}
a_intersection_b = A.intersection (B)
a_uniao_b = len(A) + len(B) - len(a_intersection_b) 
print(a_uniao_b)

#regra do produ teoria dos conjuntos
#aplicado quando se quer verificar a se um elemento e outro elemento pertencente à conjunto, de acordo com a Cardinalidade dos elementos. Em probabilidades se verifica a ocorrência de um e outro elemento simultaneamente. 
# se a intersecção em b for zero, é um disjunto, ou seja os elementos ou eventos são independentes


def conjunto_disjunto(a, b):
    if len(a.intersection(b))==0:
       return len(a) * len(b)
    else:
     return len(a) * len(b) - len(a_intersection_b) 
  
print(conjunto_disjunto(A, B))
