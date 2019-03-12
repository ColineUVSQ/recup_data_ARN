'''
Created on 22 oct. 2018

@author: Coline Gi
'''
import itertools
from itertools import combinations

paires = []
for element in itertools.product([1,2,3,4],[1,2,3,4]):
   paires.append(element)
   
print(paires)


print(list(combinations(paires, 4)))

liste = []

for elt in list(combinations(paires,4)) :
    #print(elt)
    pas_bon = False
    i = 0
    while i < len(elt) :
        j = i + 1
        while j < len(elt) :
            if elt[i][0] == elt[j][0] or elt[i][1] == elt[j][1] :
                pas_bon = True
            j = j+1
        i = i+1
    if pas_bon == False :
       liste.append(elt) 

print(len(liste))        
print(liste)