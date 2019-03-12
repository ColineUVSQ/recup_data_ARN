'''
Created on 19 nov. 2018

@author: coline
'''
import os
import pickle

with open("graphs_2.92.pickle", 'rb') as fichier :
    mon_depickler_graphes = pickle.Unpickler(fichier)
    graphes = mon_depickler_graphes.load()
    compteur = 0
    with open("fichier_pas_liaison_cov_2.txt", 'w') as fichier_sortie :
        for element in os.listdir('graphes_extension/'):
            if "pickle" in element : 
                with open("graphes_extension/"+element, 'rb') as fichier_entree :
                    mon_depickler = pickle.Unpickler(fichier_entree)
                    G_ext = mon_depickler.load()
                    
                    occ = (element.split("_")[1], element.split("_")[2])
                    
                    for noeud_ext in G_ext.nodes() :
                        liaison_cov = False
                        elt = G_ext.nodes[noeud_ext]["position"][0]
                        while elt <= G_ext.nodes[noeud_ext]["position"][1] :
                            #for voisin in graphes[occ][elt] :
                            #if graphes[occ][elt][elt+1]["label"] == 'B53' :
                            #    liaison_cov = True
                            if elt+1 < graphes[occ].number_of_nodes() :
                                if graphes[occ][elt][elt+1]["label"] != 'B53' and G_ext.nodes[noeud_ext]["type"] not in [None,11,12,13,14] :
                                    print(element)
                                    print(elt)
                                    fichier_sortie.write(str(occ) + " num RIN : " + str(int(element.split('_')[3]) - 1)+ " num occ : " + str(int(element.split('_')[4][:len(element.split('_')[4]) - 7])-1) + " num nucleotide " + str(elt) + " " + str(graphes[occ][elt][elt+1]["label"]) + "\n")
                                    compteur = compteur+1
                            elt = elt + 1
        
    print(compteur)
            