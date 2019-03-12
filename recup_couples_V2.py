'''
Created on 13 nov. 2018

@author: coline
'''
import os
import pickle
import time
import itertools
from itertools import combinations

import multiprocessing
 
liste = ['5J7L_DA_191_3', '5J7L_DA_191_4', '5FDU_1A_301_1', '5J7L_DA_301_2', '5DM6_X_334_1', '5FDU_1A_334_2', '4V9F_0_335_1', '5J7L_DA_335_2', '3JCS_1_137_4', '4V88_A5_290_1', '4V88_A6_314_2', '5J7L_DA_218_3', '4V9F_0_251_2', '1FJG_A_62_8', '5J7L_DA_137_1', '4V9F_0_118_1', '4V9F_0_62_2', '5J7L_DA_271_2', '4V9F_0_224_1', '5DM6_X_197_1', '3GX5_A_138_6', '1FJG_A_317_2', '5J5B_BA_317_1', '1FJG_A_326_1', '5DM6_X_137_3', '5J5B_BA_314_1', '4V9F_0_134_6', '4V9F_0_328_1', '4V9F_0_197_2', '4V9F_0_62_16', '5J7L_DA_282_2', '4V88_A5_137_2', '5FDU_1A_224_3']

 
#############################################################################
def exectimeout(timeout, fonc, *args, **kwargs):
    """exécute fonc(args, kwargs), avec le temps maxi timeout"""
    pool = multiprocessing.Pool(processes=1) # crée 1 processus
    poolexec = pool.apply_async(func=fonc, *args, **kwargs) # eval. asynchrone
    try:
        poolexec.get(timeout=timeout)
        result = poolexec.get()
        pool.terminate()
        return result
    except multiprocessing.TimeoutError:
        pool.terminate()
        raise # renvoi de l'exception à l'appelant
 

def recherche_couples(couples_possibles, chaines_1, chaines_2):
   
    for num_chaine in range(0, 4) :
        print(chaines_1[num_chaine])
        print(chaines_2[num_chaine])
        paires = []
        try :
            for element in itertools.product(chaines_1[num_chaine][1:],chaines_2[num_chaine][1:]):
                paires.append(element)
        except MemoryError as error :
            couples_possibles.append("memory error 1")
            break

        paires_epurees = []
        ## voir si les deux sommets qu'on superpose ont les bonnes proprietes
        for elt in paires :
            if graphe1.nodes[elt[0]]["type"] == graphe2.nodes[elt[1]]["type"] : #and (abs(graphe1.nodes[elt[0]]["poids"] - graphe2.nodes[elt[1]]["poids"]) < 2) :  
                paires_epurees.append(elt)
#         print(len(paires_epurees))
#         print(paires_epurees)

        liste = []
        new_couples = []
        new_chaine = []
        liste_epuree = []
        k = 0
        #for i in range(1, min(len(chaines_1[num_chaine])-1, len(chaines_2[num_chaine])-1 ) +1) :
        while min(len(chaines_1[num_chaine])-1, len(chaines_2[num_chaine])-1 )-k >= 1 :
#             print(min(len(chaines_1[num_chaine])-1, len(chaines_2[num_chaine])-1 )-k)
#             print(num_chaine)
            num_l = len(liste)
            try :
                combinaisons = list(combinations(paires_epurees,min(len(chaines_1[num_chaine])-1, len(chaines_2[num_chaine])-1 )-k))
            except MemoryError as error  :
                couples_possibles.append("memory error 2")
                break
#             print(len(combinaisons))
#             print(combinaisons)
              
            for elt in combinaisons : ##voir si un sommet n est pas superpose avec deux autres sommets distincts
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

#             print(len(liste))
#             print(liste)
            num_co = len(new_couples)
            
            for chaine in liste[num_l:] :
                #print(chaine)
                new_ch = []
                for couple in chaine :
                    new_ch.append(couple)
                new_couples.append(new_ch)
#             print("new couples")
#             print(len(new_couples))
#             print(new_couples)

            num_ca = len(new_chaine) 
            for possib in new_couples[num_co:] :
                    #print(possib)
                    incompatibles = {}
                    for i in range(len(possib)) :
                        for j in range(i+1, len(possib)) :
                            if (graphe1.nodes[possib[i][0]]["position"] < graphe1.nodes[possib[j][0]]["position"] and graphe2.nodes[possib[i][1]]["position"] > graphe2.nodes[possib[j][1]]["position"]) or (graphe1.nodes[possib[i][0]]["position"] > graphe1.nodes[possib[j][0]]["position"] and graphe2.nodes[possib[i][1]]["position"] < graphe2.nodes[possib[j][1]]["position"]) :
                                if possib[i] not in incompatibles.keys() :
                                    incompatibles.update({possib[i]  : [possib[j]]})
                                else :
                                    incompatibles[possib[i]].append(possib[j])
    #                             print(incompatibles)
    #                             for elt in incompatibles.keys() : 
    #                                 print(len(incompatibles[elt]))
    #                                 if max < len(incompatibles[elt]) :
    #                                     max = len(incompatibles[elt])
                    if len(incompatibles) == 0 :
                        new_chaine.append(possib)
    #print(max)
#                     num_ch = len(new_chaine)
#                     new_chaine.append([])
#     #                 print("incomp")
#     #                 print(incompatibles)
#     #                 print("debut")
#     #                 print(new_chaine)
#                     traites = []
#                     for i in range(len(possib)) :
#                         #print("i")
#                         #print(possib[i])
#                         if possib[i] not in traites :
#                             if possib[i] in incompatibles.keys():
#                                 if len(incompatibles[possib[i]]) == 1 : 
#                                     #print("ramousnif")
#                                     new_chaine[len(new_chaine)-1].append(possib[i])
#                                     new_chaine.append([])
#                                     new_chaine[len(new_chaine)-1].append(incompatibles[possib[i]][0])
#                                     ### une chaine avec le incomp, et une chaine avec son incompatible
#                                 else :
#                                     new_chaine.append([])
#                                     new_chaine[len(new_chaine)-1].append(possib[i])
#                                     for k in range(len(incompatibles[possib[i]])) :
#                                         print("k")
#                                         
#                                         incomp1 = incompatibles[possib[i]][k]
#                                         #print(incomp1)
#                                         peut_ajouter = False
#                                         new_possib = num_ch
#                                         while new_possib < len(new_chaine) and peut_ajouter == False :
#                                             peut_ajouter = True
#                                             for elt in new_chaine[new_possib] :
#                                                 if (incomp1 in incompatibles.keys() and elt in incompatibles[incomp1]) or (elt in incompatibles.keys() and incomp1 in incompatibles[elt]) :
#                                                     peut_ajouter = False
#                                             new_possib += 1
#                                         if new_possib == len(new_chaine) :
#                                             new_chaine.append([])
#                                             new_chaine[len(new_chaine)-1].append(incomp1)
#                                         else :
#                                             new_chaine[new_possib-1].append(incomp1)
#                                         #print(new_chaine)
#                                         traites.append(incomp1)
#                     for i in range(len(possib)) :
#                         incomp = False
#                         for cle in incompatibles.keys() :
#                             if possib[i] in incompatibles[cle] :
#                                 incomp = True
#                         if possib[i] not in incompatibles.keys() and incomp == False :
#                             for new_possib in range(num_ch, len(new_chaine)) :
#                                 new_chaine[new_possib].append(possib[i])
#             print("new_chaine")
#             print(new_chaine) 
            
            
            a_enlever = []
            for i in range(0,len(new_chaine)) :
                for j in range(0, len(new_chaine)) :
                        if j != i :
                            nb_existe_deja = 0
                            for m in range(0, len(new_chaine[i])) :
                                for l in range(0, len(new_chaine[j])) :
                                    if new_chaine[i][m][0] == new_chaine[j][l][0] and new_chaine[i][m][1] == new_chaine[j][l][1]  :
                                        nb_existe_deja += 1
                            if nb_existe_deja == len(new_chaine[i]) and i not in a_enlever :
                                if len(new_chaine[i]) == len(new_chaine[j]) :
                                    a_enlever.append(j)
                                else :
                                    a_enlever.append(i)
            for i in range(num_ca, len(new_chaine)) :
                if i not in a_enlever :
                    liste_epuree.append(new_chaine[i])
            
            k = k+1  
            
        couples_possibles.append(liste_epuree)
        print("couples_possibles")
        print(couples_possibles)
    return couples_possibles
        

# for fic1 in range(len(os.listdir("graphes_extension"))) :
#     element1 = os.listdir("graphes_extension")[fic1]
#     if "pickle" in element1 :
element1 = "fichier_5J7L_DA_272_2.pickle"
# with open("fichiers_tries.pickle", "rb") as fichier_tri :
#     mon_depickler_tri = pickle.Unpickler(fichier_tri)
#     tri = mon_depickler_tri.load()
#     for compte_tri_1 in range(98) :
#         element1 = tri[compte_tri_1]
#liste_a_faire = ["fichier_1FJG_A_58_23.pickle", "fichier_1FJG_A_138_3.pickle", "fichier_4PRF_B_25_69.pickle", "fichier_4V9F_0_44_3.pickle", "fichier_4V88_A6_17_55.pickle", "fichier_4V88_A6_48_12.pickle", "fichier_5J5B_BA_48_7.pickle", "fichier_5J5B_BA_138_2.pickle", "fichier_5J7L_DA_50_21.pickle"]
#     for k in range(len(liste_a_faire)) :
#
print(element1)
        
pas_bon = False
for elt in liste :
    if elt in element1 :
        pas_bon = True
        
if pas_bon == False :
                    with open("graphes_extension/"+element1, 'rb') as fichier1 :
                            mon_depickler1 = pickle.Unpickler(fichier1)
                            graphe1 = mon_depickler1.load()
                            chaines_1 = [[1]]
                            for i in range(1,5) :
                                compteur = i
                                if i != 1 : chaines_1.append([i])
                                liaison_B53 = True
                                while liaison_B53 :
                                    liaison_B53 = False
                                    temp = compteur
                                    for voisin in graphe1.successors(compteur) :
                                        for arc in graphe1[compteur][voisin] :
                                            if voisin not in [1,2,3,4] and voisin not in chaines_1[len(chaines_1)-1] and graphe1[compteur][voisin][arc]["label"] == 'B53' :
                                                liaison_B53 = True
                                                temp = voisin
                                                chaines_1[len(chaines_1)-1].append(voisin)
                                                
                                    for voisin in graphe1.predecessors(compteur) :
                                        for arc in graphe1[voisin][compteur] :
                                            if voisin not in [1,2,3,4] and voisin not in chaines_1[len(chaines_1)-1] and graphe1[voisin][compteur][arc]["label"] == 'B53' :
                                                liaison_B53 = True
                                                temp = voisin
                                                chaines_1[len(chaines_1)-1].append(voisin)
                                    compteur = temp
                            
#                             for fic2 in range(fic1+1, len(os.listdir("graphes_extension"))) :
#                                 element2 = os.listdir("graphes_extension")[fic2]
#                             compte_tri = 0 
#                             for compte_tri in range(98) :
#                                 element2 = tri[compte_tri]

                            element2 = "fichier_5FDU_1A_48_25.pickle"
                            tps1 = time.time()
#                                 for j in range(k+1, len(liste_a_faire)) :
#                                     element2 = liste_a_faire[j]
                            print(element2)
                            #element2 = os.listdir("Coline/graphes_extension/")[fic]
                            #element2 = input("Entrer element 2 : ")
                            
                            pas_bon = False
                            for elt in liste :
                                    if elt in element2  :
                                        pas_bon = True
                                            
                                    if pas_bon == False and element2 != element1 and "pickle" in element2 and "couples_possibles_"+ element1[:len(element1)-7] + "_" + element2 not in os.listdir("nouvelle_metrique") and "couples_possibles_"+ element2[:len(element2)-7] + "_" + element1 not in os.listdir("nouvelle_metrique") and "couples_possibles_"+ element1[:len(element1)-7] + "_" + element2 not in os.listdir("nouvelle_metrique") and "couples_possibles_"+ element2[:len(element2)-7] + "_" + element1 not in os.listdir("nouvelle_metrique")  and "couples_possibles_"+ element1[:len(element1)-7] + "_" + element2 not in os.listdir("nouvelle_metrique") and "couples_possibles_"+ element2[:len(element2)-7] + "_" + element1 not in os.listdir("nouvelle_metrique") :     
                                        print(element2)
                                        #with open("fichiers_tot_couples_possibles.txt", 'a') as fichier_tot :
                                            #fichier_tot.write(element1 + "\n")
                                            #fichier_tot.write("Chaines : " + str(chaines_1) + "\n")
                                        with open("graphes_extension/"+element2, 'rb') as fichier2 :
                                            mon_depickler2 = pickle.Unpickler(fichier2)
                                            graphe2 = mon_depickler2.load()   
                                            chaines_2 = [[1]]
                                            for i in range(1,5) :
                                                compteur = i
                                                if i != 1 : chaines_2.append([i])
                                                liaison_B53 = True
                                                while liaison_B53 :
                                                    liaison_B53 = False
                                                    temp = compteur
                                                    for voisin in graphe2.successors(compteur) :
                                                        for arc in graphe2[compteur][voisin] :
                                                            if voisin not in [1,2,3,4] and voisin not in chaines_2[len(chaines_2)-1] and graphe2[compteur][voisin][arc]["label"] == 'B53' :
                                                                liaison_B53 = True
                                                                temp = voisin
                                                                chaines_2[len(chaines_2)-1].append(voisin)
                                                                
                                                    for voisin in graphe2.predecessors(compteur) :
                                                        for arc in graphe2[voisin][compteur] :
                                                            if voisin not in [1,2,3,4] and voisin not in chaines_2[len(chaines_2)-1] and graphe2[voisin][compteur][arc]["label"] == 'B53' :
                                                                liaison_B53 = True
                                                                temp = voisin
                                                                chaines_2[len(chaines_2)-1].append(voisin)
                                                    compteur = temp
                                            #fichier_tot.write(element2 + "\n")
                                            #fichier_tot.write("Chaines : " + str(chaines_2) + "\n")
                                        
                        #                    faire = True
                        #                    for elt_1 in chaines_1 :
                        #                        if len(elt_1) >= 10 :
                        #                            faire = False
                        #                    for elt_2 in chaines_2 :
                        #                        if len(elt_2) >= 10 :
                        #                            faire = False
                
                        #                    if faire :
                                            couples_possibles = [] 
                                            
                                            t = time.time()
                                            try:
                                                result = exectimeout(180, recherche_couples, args=(couples_possibles, chaines_1, chaines_2))
                                                
                                                #print("Résultat:" + str(result))
                                                
                                                #fichier_tot.write("Couples possibles : " + str(result) + "\n") 
                                                with open("nouvelle_metrique/couples_possibles_"+element1[:len(element1)-7]+"_"+element2[:len(element2)-7]+".pickle", "wb") as fichier_sauvegarde :
                                                    mon_pickler = pickle.Pickler(fichier_sauvegarde)
                                                    mon_pickler.dump(result)
                                                tps2 = time.time()
                                            
                                                #fichier_tot.write("Temps : " + str(tps2 - tps1) + "\n")
                                            except multiprocessing.TimeoutError:
                                                result = None
                                                #fichier_tot.write("Timeout expire : Arret au bout de %.3f sec.\n".format(time.time()-tps1))
                                                print("Arrêt au bout de %.3f sec." % (time.time()-t,))
                                                with open("nouvelle_metrique/couples_possibles_"+element1[:len(element1)-7]+"_"+element2[:len(element2)-7]+".pickle", "wb") as fichier_sauvegarde :
                                                    mon_pickler = pickle.Pickler(fichier_sauvegarde)
                                                    mon_pickler.dump(result)
                                

        
        
        
        

