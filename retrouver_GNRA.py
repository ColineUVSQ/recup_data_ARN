'''
Created on 12 déc. 2018

@author: coline
'''

import pickle
import os

with open("graphs_2.92.pickle", 'rb') as fichier_tot :
    mon_depickler = pickle.Unpickler(fichier_tot)
    graphe_tot = mon_depickler.load()
    
    for fic in os.listdir("graphes_extension/") :
        if "pickle" in fic :
            
            with open("graphes_extension/"+fic, 'rb') as fichier_graphe :
                mon_depickler_graphe = pickle.Unpickler(fichier_graphe)
                graphe = mon_depickler_graphe.load()
                occ = fic.split("_")[1]
                chaine = fic.split("_")[2]
                num = (occ, chaine)
                
                pos_1 = graphe.nodes[1]["position"][0]
                pos_3 = graphe.nodes[3]["position"][0]
                
                if graphe_tot[num].nodes[pos_1]["nt"] == 'A' and (graphe_tot[num].nodes[pos_3]["nt"] == 'A' or graphe_tot[num].nodes[pos_3]["nt"] == 'G') and graphe_tot[num].nodes[pos_3-2]["nt"] == 'G' and graphe_tot[num].nodes[pos_3-4]["part"] == "Stem" and graphe_tot[num].nodes[pos_1+2]["part"] == "Stem" :  
                    print(fic)
                    liaison_ok = False
                    for voisin in graphe_tot[num][pos_1] :
                        if voisin == pos_3-2 and graphe_tot[num][pos_1][voisin]["label"] == 'THS' :
                            liaison_ok = True
                    if liaison_ok :
                        print('ok')
                    #print(graphe_tot[num].nodes.data())
                     