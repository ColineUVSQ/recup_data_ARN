'''
Created on 12 mars 2019

@author: coline
'''

import os
import pickle

dico_graphes = {}
for fic in os.listdir("result_graphes_comp_test") :
    if "pickle" in fic :
        with open("result_graphes_comp_test/"+fic, 'rb') as fichier :
            mon_depickler = pickle.Unpickler(fichier)
            dico_graphe = mon_depickler.load()
            
            for cle in dico_graphe.keys() :
                if cle in dico_graphes.keys() :
                    print("bizarre")
                dico_graphes.update({cle : dico_graphe[cle]})
            

with open("dico_comp_complet_metrique_toutes_aretes.pickle", 'wb') as fichier_ecriture :
    mon_pickler = pickle.Pickler(fichier_ecriture)
    mon_pickler.dump(dico_graphes)
    
    
    