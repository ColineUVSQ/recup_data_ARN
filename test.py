'''
Created on 11 oct. 2018

@author: Coline Gi
'''
import pickle
import os
import networkx as nx

# with open("graphs_2.92.pickle", 'rb') as fichier_tout :
#         mon_depickler_graphes = pickle.Unpickler(fichier_tout)
#         graphes = mon_depickler_graphes.load()
#         with open("fichier_struct_second_2XD0_V.txt","w") as fichier :
#             fichier.write(str(graphes[('2XD0', 'V')].nodes.data()))
#             fichier.write(str(graphes[('2XD0', 'V')].edges.data()))
#             print("ramousnif")
#             print(graphes[('2XD0', 'V')].nodes.data())
#             print(graphes[('2XD0', 'V')].edges.data())
            
#         with open("graphes_extension/fichier_1FJG_A_48_8.pickle", 'rb') as fichier_extension :
#             mon_depickler_extension = pickle.Unpickler(fichier_extension)
#             extension = mon_depickler_extension.load()
#             print(extension.nodes.data())

# with open("fichier_max.pickle", 'rb') as fichier :
#     mon_depickler = pickle.Unpickler(fichier)
#     tab = mon_depickler.load()
#     print(len(tab))
#     print(tab)


# for fic in os.listdir("graphes_extension/fichiers_couples/") :
#         element1 = fic.split('_')[2] + '_' + fic.split('_')[3] + '_' + fic.split('_')[4] + '_' + fic.split('_')[5] + '_' + fic.split('_')[6]
#         element2 = fic.split('_')[7] + '_' + fic.split('_')[8] + '_' + fic.split('_')[9] + '_' + fic.split('_')[10] + '_' + fic.split('_')[11][:len(fic.split('_')[11])-7]
#         #element1 = "fichier_1FJG_A_48_11"
#         #element2 = "fichier_1FJG_A_48_8"
#         #fic = "couples_possibles_fichier_1FJG_A_48_11_fichier_1FJG_A_48_8.pickle"
#         with open("graphes_extension/"+element1+".pickle", 'rb') as fichier1 :
#                 mon_depickler1 = pickle.Unpickler(fichier1)
#                 graphe1 = mon_depickler1.load()     
#                 with open("graphes_extension/"+element2+".pickle", 'rb') as fichier2 :
#                     mon_depickler2 = pickle.Unpickler(fichier2)
#                     graphe2 = mon_depickler2.load()
#      
#                     with open("graphes_extension/fichiers_couples/" + fic, 'rb') as fichier_pickle :
#                                     memory_error = False
#                                     graphe_motif = nx.MultiGraph()
#                                     for i in range(1,6) :
#                                         graphe_motif.add_node((i,i))
#                                     graphe_motif.add_edge((1,1),(2,2), type="NON_CAN")
#                                     graphe_motif.add_edge((1,1),(3,3), type="COV")
#                                     graphe_motif.add_edge((1,1),(5,5), type="NON_CAN")
#                                     graphe_motif.add_edge((2,2),(4,4), type="COV")
#                                     graphe_motif.add_edge((2,2),(5,5), type="CAN")
#                                     graphe_motif.add_edge((3,3),(4,4), type="NON_CAN")
#                                     
#                                                             
#                                     mon_depickler = pickle.Unpickler(fichier_pickle)
#                                     couples_possibles = mon_depickler.load()
#                                     print(fic)
#                                     #print(couples_possibles)
#                                     
#                                     new_couples_possibles = []
#                                     for i in range(4) :
#                                         new_couples = []
#                                         if 'memory error' in couples_possibles[i] :
#                                             memory_error = True
#                                             break
#                                         for chaine in couples_possibles[i] :
#                                             new_chaine = [(i+1, i+1)]
#                                             for couple in chaine :
#                                                 new_chaine.append(couple)
#                                             new_couples.append(new_chaine)
#                                         new_couples_possibles.append(new_couples)
#                                     print(new_couples_possibles)

# with open("tab_nexiste_pas.pickle", 'rb') as fichier :
#     mon_depickler = pickle.Unpickler(fichier)
#     tab = mon_depickler.load()
#     print(tab)
#     
#     for elt in tab :
#         if '3JCS_1_282_1' in elt[0] or '3JCS_1_282_1' in elt[1] :
#             print(elt)
            
    
# with open("graphes_extension/fichiers_couples_qui_manquent/couples_possibles_fichier_4PRF_B_25_69_fichier_5J7L_DA_272_2.pickle", 'rb') as fichier :
#     mon_depickler = pickle.Unpickler(fichier)
#     couples_possibles = mon_depickler.load()
#     print(couples_possibles[3])       
            

# with open("fichier_comp_grands_graphes_test.pickle", 'rb') as fichier:
#     mon_depickler_comp = pickle.Unpickler(fichier)
#     dico_comp_4v9f = mon_depickler_comp.load()
#     
#     with open("fichier_comp_grands_graphes_V2.pickle", 'rb') as fichier_comp:
#         mon_depickler_tout = pickle.Unpickler(fichier_comp)
#         dico_comp = mon_depickler_tout.load()
#         
#         print(len(dico_comp))
#         print(len(dico_comp_4v9f))
#         print(dico_comp_4v9f.keys())
#         
# #         for elt in dico_comp.keys() :
# #             if elt[0] == ('4V9F', '0', 25, 4) or elt[1] == ('4V9F', '0', 25, 4) :
# #                 print("ramousnif")
#         
#         compteur = 0
#         for elt in dico_comp_4v9f.keys() :
#             if elt[0] == ('4V9F', '0', 25, 4) or elt[1] == ('4V9F', '0', 25, 4) :
#                 dico_comp.update({elt : dico_comp_4v9f[elt]})
#                 compteur += 1
#         print(compteur)
# 
#         print(len(dico_comp))          

# with open("grands_graphes.pickle", 'rb') as fichier:
#         mon_depickler_tout = pickle.Unpickler(fichier)
#         dico_graphe = mon_depickler_tout.load()
# #         for u,v, dict in dico_graphe[('1FJG', 'A', 294, 1)].edges(data=True) :
# #             print((u,v))
# #             print(dict)
#             
#         compteur_arc = 0
#         compteur = 0
#         for (u, v, keys, t) in dico_graphe[('1FJG', 'A', 294, 1)].edges(data="label", keys = True) :
#             if (v,u) in dico_graphe[('1FJG', 'A', 294, 1)].edges() :
#                 print("ramou")
#                 compteur += 1
#         print(compteur)
#                 
#         print(compteur_arc)
#         print(dico_graphe[('1FJG', 'A', 294, 1)].number_of_edges())
    
    
with open("graphs_2.92.pickle", 'rb') as fichier_tout :
        mon_depickler_graphes = pickle.Unpickler(fichier_tout)
        graphes = mon_depickler_graphes.load() 
        
        with open("fichier_struct_second_1GID_B.txt", 'w') as fichier :
            
            for noeud, data in graphes[('1GID', 'B')].nodes(data=True) :
                fichier.write(str(noeud) + " "+ str(data)+ "\n")
            
            for u,v,data in graphes[('1GID', 'B')].edges(data=True) :
                fichier.write(str((u,v)) + " "+ str(data) + "\n")
            
            
                                    