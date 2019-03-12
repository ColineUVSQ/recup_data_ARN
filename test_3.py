'''
Created on 4 déc. 2018

@author: coline
'''

import pickle
import os
import time

for fic in os.listdir("graphes_extension/fichiers_couples_qui_manquent_incomp/") :
        tps1 = time.time()
        if fic not in os.listdir("graphes_extension/fichiers_couples_qui_manquent_epures/")  :
            with open("graphes_extension/fichiers_couples_qui_manquent_incomp/"+fic, 'rb') as fichier_sortie :
                mon_depickler = pickle.Unpickler(fichier_sortie)
                new_couples_possibles = mon_depickler.load()
            
                new_couples_possibles_epuree = [[],[],[],[]]
                
                #print(len(new_couples_possibles))
                if len(new_couples_possibles) == 4 :
                    for m in range(4) :
                        #print(m)
                        print(new_couples_possibles)
                        if 'memory_error' not in new_couples_possibles[m] :
                            a_enlever = []
                            for i in range(0,len(new_couples_possibles[m])) :
                                for j in range(0, len(new_couples_possibles[m])) :
                                        if j != i :
                                            nb_existe_deja = 0
                                            for k in range(0, len(new_couples_possibles[m][i])) :
                                                for l in range(0, len(new_couples_possibles[m][j])) :
                                                    if new_couples_possibles[m][i][k][0] == new_couples_possibles[m][j][l][0] and new_couples_possibles[m][i][k][1] == new_couples_possibles[m][j][l][1]  :
                                                        nb_existe_deja += 1
                                            #print(nb_existe_deja)
                                            if nb_existe_deja == len(new_couples_possibles[m][i]) and i not in a_enlever :
                                                if len(new_couples_possibles[m][i]) == len(new_couples_possibles[m][j]) :
                                                    a_enlever.append(j)
                                                else :
                                                    a_enlever.append(i)
                            #print(a_enlever)
                            for i in range(0, len(new_couples_possibles[m])) :
                                if i not in a_enlever :
                                    new_couples_possibles_epuree[m].append(new_couples_possibles[m][i])
                                else :
                                    a_enlever.remove(i)
                        else :
                            break
                print(fic)
                
                print(new_couples_possibles)
                print(new_couples_possibles_epuree)
                print("\n")
                
                with open("graphes_extension/fichiers_couples_qui_manquent_epures/"+fic, 'wb') as fichier_epure :
                    mon_pickler = pickle.Pickler(fichier_epure)
                    mon_pickler.dump(new_couples_possibles_epuree)
                        