'''
Created on 9 oct. 2018

@author: Coline Gi
'''
import pickle
import networkx as nx


liste = ['5J7L_DA_191_3', '5J7L_DA_191_4', '5FDU_1A_301_1', '5J7L_DA_301_2', '5DM6_X_334_1', '5FDU_1A_334_2', '4V9F_0_335_1', '5J7L_DA_335_2', '3JCS_1_137_4', '4V88_A5_290_1', '4V88_A6_314_2', '5J7L_DA_218_3', '4V9F_0_251_2', '1FJG_A_62_8', '5J7L_DA_137_1', '4V9F_0_118_1', '4V9F_0_62_2', '5J7L_DA_271_2', '4V9F_0_224_1', '5DM6_X_197_1', '3GX5_A_138_6', '1FJG_A_317_2', '5J5B_BA_317_1', '1FJG_A_326_1', '5DM6_X_137_3', '5J5B_BA_314_1', '4V9F_0_134_6', '4V9F_0_328_1', '4V9F_0_197_2', '4V9F_0_62_16', '5J7L_DA_282_2', '4V88_A5_137_2', '5FDU_1A_224_3', '5J7L_DA_326_2']


def ajout_sommet(G, compteur, compteur_tige, position, typ, poids, label, positions_ajoutees, int_tige, valeur_debut, *args, **kwargs):
    long_range = kwargs.get("long_range", False)
    
    voisin_chaine =  kwargs.get("voisin_chaine", -1)
#     if len(pos_liaisons) > 0 :
#         if typ == 1 :
#             if len(pos_liaisons[0]) > 1 : ## il faut decouper le sommet en deux voire plus car il est lie a plusieurs sommets de l autre chaine
#                 for elt in pos_liaisons[0] :
#                     G.add_node(compteur, position=position, type=typ, poids=G.nodes[elt]["poids"], chaine=[valeur_debut], pos_liaisons=pos_liaisons[1])
#                     
#                     if valeur_debut not in G.nodes[elt]["pos_liaisons"] and G.nodes[elt]["type"] == 1 :
#                         G.nodes[elt]["pos_liaisons"].append(valeur_debut)
#                         
#                     G.add_edge(compteur, elt, label="CWW", long_range=False)   
#                     G.add_edge(elt, compteur, label="CWW", long_range=False)
#                     
#                     compteur += 1
#                 compteur = compteur-1
#             else :
#                 G.add_node(compteur, position=position, type=typ, poids=poids, chaine=[valeur_debut], pos_liaisons=pos_liaisons[1]) 
#                 
#                 if valeur_debut not in G.nodes[pos_liaisons[0]]["pos_liaisons"] and G.nodes[pos_liaisons[0]]["type"] == 1 :
#                     G.nodes[elt]["pos_liaisons"].append(valeur_debut)
#                     G.add_edge(compteur, elt, label="CWW", long_range=False)
#                     G.add_edge(elt, compteur, label="CWW", long_range=False)
#         else :
#             G.add_node(compteur, position=position, type=typ, poids=poids, chaine=[valeur_debut], pos_liaisons=[])
#     else : 
#         G.add_node(compteur, position=position, type=typ, poids=poids, chaine=[valeur_debut], pos_liaisons=pos_liaisons)
    
    G.add_node(compteur, position=position, type=typ, poids=poids, chaine=[valeur_debut])
    if typ == 1 : ## il faut peut etre rajouter des aretes si on a deja mis le sommet de la deuxieme chaine
        if compteur == 14 :
            print("ramou")
            print(voisin_chaine)
        noeud_existe = False
        for noeud, data in G.nodes(data=True) :
            if voisin_chaine >= data["position"][0] and voisin_chaine <= data["position"][1] :
                noeud_existe = noeud
        if noeud_existe != False :
            G.add_edge(compteur, noeud_existe, label="CWW", long_range=False)
            G.add_edge(noeud_existe, compteur, label="CWW", long_range=False)
            
        
    if label == "B53" :
        if int_tige == 1 :
            if valeur_debut == 3 or valeur_debut == 4 :
                G.add_edge(compteur_tige, compteur, label=label, long_range=long_range)
            else :
                G.add_edge(compteur, compteur_tige, label=label, long_range=long_range)
        else :
            if valeur_debut == 3 or valeur_debut == 4 :
                G.add_edge(compteur, compteur_tige, label=label, long_range=long_range)
            else :
                G.add_edge(compteur_tige, compteur, label=label, long_range=long_range)
    else :
        G.add_edge(compteur_tige, compteur, label=label, long_range=long_range)
        G.add_edge(compteur, compteur_tige, label=label, long_range=long_range)
    for i in range(position[0], position[1]+1) :
        positions_ajoutees.append(i)
    

# def tige(G, graphes, nom_cle, compteur, compteur_tige, positions_ajoutees) :
#     valeur_debut = compteur_tige
#    
# #     if valeur_debut == 2 or valeur_debut == 1:
# #         new_position = G.node[valeur_debut]["position"][0]-i*int_tige
# #     else :
# #         new_position = G.node[valeur_debut]["position"][0]+i*int_tige 
# 
#     new_position = G.node[valeur_debut]["position"][0]
#     
#     while valeur_debut < 5 and new_position > 0 and new_position < graphes[nom_cle].number_of_nodes() :
#         #print(i)
#         voisins = graphes[nom_cle][new_position]
#         if nom_cle == ('4V88', 'A6') :
#             print(new_position)
#             print("voisins")
#         for voisin in voisins :
# #             if nom_cle == ('4V88', 'A6') :
# #                 print(voisin)
# #                 print(positions_ajoutees)
#             if voisin not in positions_ajoutees :
#                 
#                 G.add_node(compteur, position = (voisin, voisin), type=None, poids=1, chaine=[valeur_debut])
#                 G.add_edge(compteur, valeur_debut, label=graphes[nom_cle].edges[new_position,voisin]["label"])
#                 G.add_edge(valeur_debut, compteur, label=graphes[nom_cle].edges[new_position,voisin]["label"])
#                 compteur = compteur + 1
#                 positions_ajoutees.append(voisin)
#             else :
#                 if nom_cle == ('4V88', 'A6') :
#                     print(voisin)
#                     print(G.edges())
#                 for u, pos in G.nodes(data="position") :
#                     if pos[0] <= voisin and pos[1] >= voisin  :
#                         if (u,valeur_debut) not in G.edges() and (valeur_debut, u) not in G.edges():
#                             G.add_edge(u, valeur_debut, label=graphes[nom_cle].edges[new_position,voisin]["label"])
#                             G.add_edge(valeur_debut, u, label=graphes[nom_cle].edges[new_position,voisin]["label"])
#                         
#                             if valeur_debut not in G.nodes[u]["chaine"] :
#                                 G.nodes[u]["chaine"].append(valeur_debut)
#         
#         valeur_debut += 1               
#         new_position = G.node[valeur_debut]["position"][0]
#         
#     
#     return G

def type_sommet(voisins, new_position, G):
    
    if new_position == G.nodes[1]["position"][0] :
        return 11 
    if new_position == G.nodes[2]["position"][0] :
        return 12 
    if new_position == G.nodes[3]["position"][0] :
        return 13
    if new_position == G.nodes[4]["position"][0] :
        return 14
    if new_position == G.nodes[5]["position"][0] :
        return 15 
    
    type_sommet_actuel = -1
    if len(voisins) == 0 :
        type_sommet_actuel = 0
    if len(voisins) == 1 : ##Pas de voisin en dehors de la sequence
        for voisin in voisins :
            if graphes[nom_cle][new_position][voisin]["label"] == "B53": 
                type_sommet_actuel = 0
            else :
                type_sommet_actuel = 3
    elif len(voisins) == 2 : ## Un autre voisin en dehors de la sequence
        for voisin in voisins :
            label_voisin = graphes[nom_cle][new_position][voisin]["label"]
            if label_voisin != "B53" :
                if label_voisin == 'CWW' and graphes[nom_cle][new_position][voisin]["long_range"] == False : #and ((voisin <= compteur_tige2 and voisin > compteur_tige2-5) or (voisin >= compteur_tige2 and voisin < compteur_tige2+5) or (voisin <= G.node[valeur_debut]["position"][0] and voisin > G.node[valeur_debut]["position"][0]-10) or (voisin >= G.node[valeur_debut]["position"][0] and voisin < G.node[valeur_debut]["position"][0]+10)) :
                ##sommet de type 0
                    type_sommet_actuel = 1       
                    #compteur_tige2 = voisin
                else : ##sommet de type 3
                    type_sommet_actuel = 3
    else : ##Plus d'un autre voisin en dehors de la sequence
        for voisin in voisins : #Recherche d'une liaison can de tige
            label_voisin = graphes[nom_cle][new_position][voisin]["label"]
            if label_voisin != "B53" :
                if label_voisin == 'CWW' and graphes[nom_cle][new_position][voisin]["long_range"] == False : #and ((voisin <= compteur_tige2 and voisin > compteur_tige2-5) or (voisin >= compteur_tige2 and voisin < compteur_tige2+5) or (voisin <= G.node[valeur_debut]["position"][0] and voisin > G.node[valeur_debut]["position"][0]-10) or (voisin >= G.node[valeur_debut]["position"][0] and voisin < G.node[valeur_debut]["position"][0]+10)) :
                    type_sommet_actuel = 2
                    #compteur_tige2 = voisin
        if type_sommet_actuel == -1 :
            type_sommet_actuel = 3
            
    return type_sommet_actuel


def extension_tige(G, graphes, nom_cle, compteur, compteur_tige, positions_ajoutees, int_tige):
    #print(compteur)
    valeur_debut = compteur_tige
    i = 0
    poids_sommet = 1
    type_sommet_prec = None
    type_sommet_actuel = None 
    type_sommet_voisin = None
    type_sommet_voisin_prec = None
   
    if valeur_debut == 2 or valeur_debut == 1:
        new_position = G.node[valeur_debut]["position"][0]-i*int_tige
    else :
        new_position = G.node[valeur_debut]["position"][0]+i*int_tige 

    #new_position = G.node[valeur_debut]["position"][0]                    
#     if nom_cle == ('4V88', 'A6') and occ["num_motif"] == 17 and occ["num_occ"] == 55 :
#                         print(G.edges.data())
    
    position_prec = new_position
    position_prec_groupe = new_position
    
    voisin_chaine = -1
    voisin_chaine_prec = -1
    chaine_sommet_voisin = -1
    chaine_sommet_voisin_prec = -1
    voisin_dans_chaine = False
    
    while i < 10 and new_position > 0 and new_position < graphes[nom_cle].number_of_nodes() :
        
#         if i == 3 :
#             print("ramou")
#             print(chaine)
#             print(compteur)
        #print(i)
        voisins = graphes[nom_cle][new_position]
        
#         if nom_cle == ('4V88', 'A6') and occ["num_motif"] == 17 and occ["num_occ"] == 55 :
#             print(valeur_debut)
#             print(G.edges.data())
        ### On cherche le type de sommet ##
        
                
        ## ##
        #if nom_cle == ('1FJG', 'A') :
        #    print("petit rat")
        #    print(type_sommet_actuel)
        #    print(new_position)
        #    print(poids_sommet)
        
#         if compteur == 38 :
#             print("petit rat")
#             print(chaine)
        
        type_sommet_actuel = type_sommet(voisins, new_position, G)
        

        
        if type_sommet_actuel == 1 :
            for voisin in voisins :
                label_voisin = graphes[nom_cle][new_position][voisin]["label"]
                if label_voisin != "B53" :
                    if label_voisin == 'CWW' and graphes[nom_cle][new_position][voisin]["long_range"] == False : #and ((voisin <= compteur_tige2 and voisin > compteur_tige2-5) or (voisin >= compteur_tige2 and voisin < compteur_tige2+5) or (voisin <= G.node[valeur_debut]["position"][0] and voisin > G.node[valeur_debut]["position"][0]-10) or (voisin >= G.node[valeur_debut]["position"][0] and voisin < G.node[valeur_debut]["position"][0]+10)) :
                        voisin_dans_chaine = False
                        for k in range(4) :
                            if voisin in positions_chaines[k] : ## pour savoir si le voisin appartient a une des chaines ou pas 
                                
                                type_sommet_voisin_prec = type_sommet_voisin
                                type_sommet_voisin = type_sommet(graphes[nom_cle][voisin],voisin, G)
                                chaine_sommet_voisin_prec = chaine_sommet_voisin
                                chaine_sommet_voisin = k
                                voisin_chaine_prec = voisin_chaine
                                voisin_chaine = voisin
                                
                                if compteur == 6 :
                                    print("ramou")
                                    print(voisin_chaine)
                                    print(chaine_sommet_voisin)
                                    print(chaine_sommet_voisin_prec)
                                
                                voisin_dans_chaine = True
                        if voisin_dans_chaine == False :
                            voisin_chaine_prec = voisin_chaine
                            voisin_chaine = -1
                            chaine_sommet_voisin_prec = chaine_sommet_voisin
                            chaine_sommet_voisin = -1
                            type_sommet_voisin_prec = type_sommet_voisin
                            type_sommet_voisin = None
                        
#         else :
#             voisin_chaine_prec = -1   
#                                 if compteur == 43 :
#                                     print("petit rat")
#                                     print(voisin_chaine)  
                #                                 noeud_a_trouver = -1
                #                                 for noeud, data in G.nodes(data=True) :
                #                                     if voisin >= data["position"][0] and voisin <= data["position"][1] :
                #                                         noeud_a_trouver = noeud
                #                                         type_a_trouver = data["type"]
                #                                 if noeud_a_trouver != -1 :
                #                                     if len(chaine) > 0 :
                #                                         chaine[0].append(noeud_a_trouver)
                #                                         chaine[2].append(type_a_trouver)
                #                                         for elt in G.nodes[noeud_a_trouver]["chaine"] :
                #                                             if elt not in chaine[1] :
                #                                                 chaine[1].append(elt)
                #                                     else : 
                #                                         chaine = ([noeud_a_trouver], list(G.nodes[noeud_a_trouver]["chaine"]), [type_a_trouver])
                #                                 else :
                #                                     print("probleme42")
                #                         else :
                #                             chaine = []
             
        if new_position not in positions_ajoutees :
            if compteur == 19 :
                print("ramousnif")
                print(poids_sommet)
                print(type_sommet_prec)
            if type_sommet_actuel == 0 or type_sommet_actuel == 1 :  
                
                if type_sommet_actuel == type_sommet_prec  and (type_sommet_actuel == 0 or (type_sommet_actuel == 1 and ((type_sommet_voisin_prec == type_sommet_voisin and (type_sommet_voisin == 1 or type_sommet_voisin == 0)) and (chaine_sommet_voisin == chaine_sommet_voisin_prec) or type_sommet_voisin_prec == None ) )): 
                    poids_sommet += 1
#                 elif type_sommet_actuel == 1 and type_sommet_voisin_prec != type_sommet_voisin and type_sommet_voisin != None  : ## il faut ajouter le sommet precedent
#                     
#                     
                else :
                    if (type_sommet_prec == 1 or type_sommet_prec == 0) :  ## on va ajouter le sommet precedent car il est de type 0 ou 1   
                        
                        
                        deja_vu = False
                        for k in range(min(position_prec_groupe, position_prec), max(position_prec, position_prec_groupe)+1) :
                            if k in positions_ajoutees :
                                deja_vu = True
                                
                        #if position_prec not in positions_ajoutees :
                        if deja_vu == False :
#                             if compteur == 38 :
#                                 print("ramousnif")
#                                 print(chaine)
                                
                            if position_prec - position_prec_groupe <= 0 :
                                if type_sommet_actuel != 1 :
                                    ajout_sommet(G, compteur, compteur_tige, (position_prec,position_prec_groupe), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine)
                                else : 
                                    ajout_sommet(G, compteur, compteur_tige, (position_prec,position_prec_groupe), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine_prec)
                
                            else : 
                                if type_sommet_actuel != 1 :
                                    ajout_sommet(G, compteur, compteur_tige, (position_prec_groupe,position_prec), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine)
                                else :
                                    ajout_sommet(G, compteur, compteur_tige, (position_prec_groupe,position_prec), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine_prec)
                            compteur_tige = compteur
                            compteur = compteur+1
                        else : ## le sommet d'avant existe deja mais il est peut etre en groupe maintenant
                            
                            if poids_sommet != 1 :
                                #print("petit rat")
                                num_sommet_prec = -1
                                #print("ramou")
                                for noeud in G.nodes() :
                                    for k in range(min(position_prec_groupe, position_prec), max(position_prec, position_prec_groupe)+1) :
                                        if  k <= G.nodes[noeud]["position"][1] and k >= G.nodes[noeud]["position"][0] :
                                            num_sommet_prec = noeud ## retrouver le numero du sommet
                                            if valeur_debut not in G.nodes[noeud]["chaine"] :
                                                G.nodes[noeud]["chaine"].append(valeur_debut)
                                if G.nodes[num_sommet_prec]["type"] == None :
                                    G.nodes[num_sommet_prec]["type"] = type_sommet_prec
                                    del(G.nodes[noeud]["chaine"][:])
                                    G.nodes[noeud]["chaine"].append(valeur_debut)
                                if num_sommet_prec == -1 :
                                    print("probleme6") 
                                    
                                if position_prec - position_prec_groupe <= 0 :
                                    G.nodes[num_sommet_prec]["position"] = (min(position_prec, G.nodes[num_sommet_prec]["position"][0]), max(position_prec_groupe, G.nodes[num_sommet_prec]["position"][1]))
                                else :
                                    G.nodes[num_sommet_prec]["position"] = (min(position_prec_groupe, G.nodes[num_sommet_prec]["position"][0]), max(position_prec, G.nodes[num_sommet_prec]["position"][1]))
                                G.nodes[num_sommet_prec]["poids"] = G.nodes[num_sommet_prec]["position"][1] - G.nodes[num_sommet_prec]["position"][0] + 1
                                
#                                 if type_sommet_prec == 1 :
#                                     
#                                     if len(chaine) > 0 :
#                                         for elt in chaine[1] :
#                                             if elt not in G.nodes[num_sommet_prec]["pos_liaisons"] :
#                                                 G.nodes[num_sommet_prec]["pos_liaisons"].append(elt)
#                                         for elt in chaine[0] :
#                                             if valeur_debut not in G.nodes[elt]["pos_liaisons"] and G.nodes[elt]["type"] == 1  :
#                                                 G.nodes[elt]["pos_liaisons"].append(valeur_debut)
#                                                 G.add_edge(num_sommet_prec, elt, label="CWW", long_range=False)
#                                                 G.add_edge(elt, num_sommet_prec, label="CWW", long_range=False)
#                                     else : 
#                                         G.nodes[num_sommet_prec]["pos_liaisons"].append(chaine)
                                
                                compteur_tige = num_sommet_prec 
                    position_prec_groupe = new_position    
                    type_sommet_prec = type_sommet_actuel
                    poids_sommet = 1  
                    
                    
                    
                     
                        
            else :
                if poids_sommet != 1 or (type_sommet_prec == 0 or type_sommet_prec == 1 and poids_sommet == 1): ## on va ajouter le sommet precedent car il est de type 0 ou 1
                    
                    deja_vu = False
                    for k in range(min(position_prec_groupe, position_prec), max(position_prec, position_prec_groupe)+1) :
                        if k in positions_ajoutees :
                            deja_vu = True
                          
                    #if position_prec not in positions_ajoutees : ## le sommet d'avant sur la sequence de type 0 ou 1 n'etait pas deja vu
                    if deja_vu == False :
                        if position_prec - position_prec_groupe <= 0 :
                            if type_sommet_actuel != 1 :
                                ajout_sommet(G, compteur, compteur_tige, (position_prec,position_prec_groupe), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine)
                            else : 
                                ajout_sommet(G, compteur, compteur_tige, (position_prec,position_prec_groupe), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine_prec)
            
                        else : 
                            if type_sommet_actuel != 1 :
                                ajout_sommet(G, compteur, compteur_tige, (position_prec_groupe,position_prec), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine)
                            else :
                                ajout_sommet(G, compteur, compteur_tige, (position_prec_groupe,position_prec), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine_prec)
                        compteur_tige = compteur
                        compteur = compteur+1
                    
#                     else :
#                         num_voisin_seq = -1
#                         #print(position_prec)
#                         for noeud in G.nodes() :
#                             if position_prec <= G.nodes[noeud]["position"][1] and position_prec >= G.nodes[noeud]["position"][0] :
#                                 num_voisin_seq = noeud
#                         if num_voisin_seq == -1 :
#                             print("probleme")
#                         #G.add_edge(num_voisin_seq, compteur_tige, label="B53")
                poids_sommet = 1
                ajout_sommet(G, compteur, compteur_tige, (new_position, new_position), type_sommet_actuel, 1, "B53", positions_ajoutees, int_tige, valeur_debut)
                
                
                compteur_tige = compteur
                compteur = compteur+1
                
                ## ajout de chacun des voisins du sommet actuel car il est de type 2 ou 3
                for voisin in voisins : 
                    label_voisin = graphes[nom_cle][new_position][voisin]["label"]
                    if label_voisin != "B53" :
                        if voisin not in positions_ajoutees :
                            ajout_sommet(G, compteur, compteur_tige, (voisin,voisin), None, 1, label_voisin, positions_ajoutees, int_tige, valeur_debut, long_range = graphes[nom_cle][new_position][voisin]["long_range"] )
                            compteur = compteur+1
                        else :
                            num_sommet = -1
                            #print("ramou")
                            for noeud in G.nodes() :
                                if  voisin <= G.nodes[noeud]["position"][1] and voisin >= G.nodes[noeud]["position"][0] :
                                    num_sommet = noeud ## retrouver le numero du sommet 
                            if num_sommet == -1 :
                                print("probleme2")
                            deja_fait = False
                            for v in G[num_sommet] :
                                for edge in G[num_sommet][v] :
                                    if v == compteur_tige and G[num_sommet][v][edge]["label"] != "B53" : 
                                        deja_fait = True 
                            if deja_fait == False :
                                G.add_edge(num_sommet, compteur_tige, label=label_voisin, long_range = graphes[nom_cle][new_position][voisin]["long_range"])
                                G.add_edge(compteur_tige, num_sommet, label=label_voisin, long_range = graphes[nom_cle][new_position][voisin]["long_range"])
                type_sommet_prec = type_sommet_actuel 

        else : ## le sommet actuel existe deja
            num_sommet = -1
            #print(G.nodes.data())
            #print(positions_ajoutees)
            #print(new_position)
            for noeud in G.nodes() :
                if new_position <= G.nodes[noeud]["position"][1] and new_position >= G.nodes[noeud]["position"][0]  :
                    num_sommet = noeud ## retrouver le numero du sommet 
                    if valeur_debut not in G.nodes[noeud]["chaine"] :
                        G.nodes[noeud]["chaine"].append(valeur_debut)
                    if G.nodes[noeud]["type"] == None :
                        G.nodes[noeud]["type"] = type_sommet_actuel
                        del(G.nodes[noeud]["chaine"][:])
                        G.nodes[noeud]["chaine"].append(valeur_debut)
                    #else :
                    #    print("probleme")
#                     if G.nodes[noeud]["type"] == 0 :
#                         print(new_position)
#                         print(position_prec_groupe)
#                         print(num_sommet)
#                         print(poids_sommet)
#                         
#                         
#                         print(G.nodes.data())
#                         print("ramousnif")
            if num_sommet == -1 :
                print("probleme5")
                #print(G.nodes.data())
                #print(new_position)
            
                                                      
            #print(num_sommet)
            #print(compteur_tige)
            #print(compteur)

            if type_sommet_actuel == 0 or type_sommet_actuel == 1 :
                if type_sommet_actuel == type_sommet_prec  and (type_sommet_actuel == 0 or (type_sommet_actuel == 1 and ((type_sommet_voisin_prec == type_sommet_voisin and (type_sommet_voisin == 1 or type_sommet_voisin == 0)) and (chaine_sommet_voisin == chaine_sommet_voisin_prec) or type_sommet_voisin_prec == None ) )): 
                    poids_sommet += 1
                else :
                    
                    deja_vu = False
                    for k in range(min(position_prec_groupe, position_prec), max(position_prec, position_prec_groupe)+1) :
                        if k in positions_ajoutees :
                            deja_vu = True
                    #if position_prec not in positions_ajoutees :
                    if deja_vu == False :
                        if position_prec - position_prec_groupe <= 0 :
                            if type_sommet_actuel != 1 :
                                ajout_sommet(G, compteur, compteur_tige, (position_prec,position_prec_groupe), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine)
                            else : 
                                ajout_sommet(G, compteur, compteur_tige, (position_prec,position_prec_groupe), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine_prec)
            
                        else : 
                            if type_sommet_actuel != 1 :
                                ajout_sommet(G, compteur, compteur_tige, (position_prec_groupe,position_prec), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine)
                            else :
                                ajout_sommet(G, compteur, compteur_tige, (position_prec_groupe,position_prec), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine_prec)
                        compteur_tige = compteur
                        compteur = compteur+1
                    else : ## le sommet d'avant existe deja mais il est peut etre en groupe maintenant
#                         print("petit rat")
#                         print(new_position)
                        if poids_sommet != 1 :
                            num_sommet_prec = -1
                                #print("ramou")
                            for noeud in G.nodes() :
                                for k in range(min(position_prec_groupe, position_prec), max(position_prec, position_prec_groupe)+1) :
                                    if  k <= G.nodes[noeud]["position"][1] and k >= G.nodes[noeud]["position"][0] :
                                        num_sommet_prec = noeud ## retrouver le numero du sommet 
                                        if valeur_debut not in G.nodes[noeud]["chaine"] :
                                            G.nodes[noeud]["chaine"].append(valeur_debut)
                            if G.nodes[num_sommet_prec]["type"] == None :
                                G.nodes[num_sommet_prec]["type"] = type_sommet_prec
                                del(G.nodes[noeud]["chaine"][:])
                                G.nodes[noeud]["chaine"].append(valeur_debut)
                            if num_sommet_prec == -1 :
                                print("probleme7") 
                                    
                            if position_prec - position_prec_groupe <= 0 :
                                G.nodes[num_sommet_prec]["position"] = (min(position_prec, G.nodes[num_sommet_prec]["position"][0]), max(position_prec_groupe, G.nodes[num_sommet_prec]["position"][1]))
                            else :
                                G.nodes[num_sommet_prec]["position"] = (min(position_prec_groupe, G.nodes[num_sommet_prec]["position"][0]), max(position_prec, G.nodes[num_sommet_prec]["position"][1]))
                            G.nodes[num_sommet_prec]["poids"] = G.nodes[num_sommet_prec]["position"][1] - G.nodes[num_sommet_prec]["position"][0] + 1
                            
#                             if type_sommet_prec == 1 :
#                                 if len(chaine) > 0 :
#                                     for elt in chaine[1] :
#                                         if elt not in G.nodes[num_sommet_prec]["pos_liaisons"] :
#                                             G.nodes[num_sommet_prec]["pos_liaisons"].append(elt)
#                                     for elt in chaine[0] :
#                                         if valeur_debut not in G.nodes[elt]["pos_liaisons"] and G.nodes[elt]["type"] == 1  :
#                                             G.nodes[elt]["pos_liaisons"].append(valeur_debut)
#                                             G.add_edge(num_sommet_prec, elt, label="CWW", long_range=False)
#                                             G.add_edge(elt, num_sommet_prec, label="CWW", long_range=False)
#                                 else : 
#                                     G.nodes[num_sommet_prec]["pos_liaisons"].append(chaine)
                            
                    if int_tige == 1 :
                        if valeur_debut == 3 or valeur_debut == 4 :
                            G.add_edge(compteur_tige, num_sommet, label="B53", long_range=False)
                        else :
                            G.add_edge(num_sommet, compteur_tige, label="B53", long_range=False)
                    else :
                        if valeur_debut == 3 or valeur_debut == 4 :
                            G.add_edge(num_sommet, compteur_tige, label="B53", long_range=False)
                        else :
                            G.add_edge(compteur_tige, num_sommet, label="B53", long_range=False)
                    compteur_tige = num_sommet
                        
#                     if position_prec - position_prec_groupe <= 0 :
#                         G.nodes[num_sommet]["position"] = (position_prec, position_prec_groupe)
#                     else :
#                         G.nodes[num_sommet]["position"] = (position_prec_groupe, position_prec)
                        
                    position_prec_groupe = new_position                       
                    type_sommet_prec = type_sommet_actuel
                    poids_sommet = 1

                    
            else :

                if poids_sommet != 1 or (type_sommet_prec == 0 or type_sommet_prec == 1 and poids_sommet == 1):
                    deja_vu = False
                    for k in range(min(position_prec_groupe, position_prec), max(position_prec, position_prec_groupe)+1) :
                        if k in positions_ajoutees :
                            deja_vu = True
                    
                    #if position_prec not in positions_ajoutees : ## le sommet d'avant sur la sequence de type 0 ou 1 n'etait pas deja vu
                    if deja_vu == False :
#                         if compteur == 11 :
#                             print("ramou")
#                             print(voisin_chaine_prec)
                        if position_prec - position_prec_groupe <= 0 :
                            if type_sommet_actuel != 1 :
                                ajout_sommet(G, compteur, compteur_tige, (position_prec,position_prec_groupe), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine)
                            else : 
                                ajout_sommet(G, compteur, compteur_tige, (position_prec,position_prec_groupe), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine_prec)
            
                        else : 
                            if type_sommet_actuel != 1 :
                                ajout_sommet(G, compteur, compteur_tige, (position_prec_groupe,position_prec), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine)
                            else :
                                ajout_sommet(G, compteur, compteur_tige, (position_prec_groupe,position_prec), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine_prec)
     
                        compteur_tige = compteur
                        compteur = compteur+1
                    else :
                        num_voisin_seq = -1
                       #print(position_prec)
                        for noeud in G.nodes() :
                            for k in range(min(position_prec_groupe, position_prec), max(position_prec, position_prec_groupe)+1) :
                                if  k <= G.nodes[noeud]["position"][1] and k >= G.nodes[noeud]["position"][0] :
                                    num_voisin_seq = noeud
                                    if valeur_debut not in G.nodes[noeud]["chaine"] :
                                        G.nodes[noeud]["chaine"].append(valeur_debut)
                        if num_voisin_seq == -1 :
                            print("probleme3")
                            #print(new_position)
                            #print(position_prec)
                            #print(G.nodes.data())
                        #G.add_edge(num_voisin_seq, compteur_tige, label="B53")
                        
                        if position_prec - position_prec_groupe <= 0 :
                            G.nodes[num_voisin_seq]["position"] = (min(position_prec, G.nodes[num_voisin_seq]["position"][0]), max(position_prec_groupe, G.nodes[num_voisin_seq]["position"][1]))
                        else :
                            G.nodes[num_voisin_seq]["position"] = (min(position_prec_groupe, G.nodes[num_voisin_seq]["position"][0]), max(position_prec, G.nodes[num_voisin_seq]["position"][1]))
                        G.nodes[num_voisin_seq]["poids"] = G.nodes[num_voisin_seq]["position"][1] - G.nodes[num_voisin_seq]["position"][0] +1
#                 
#                         if type_sommet_prec == 1 :
#                             if len(chaine) > 0 :
#                                 for elt in chaine[1] :
#                                     if elt not in G.nodes[num_voisin_seq]["pos_liaisons"] :
#                                         G.nodes[num_voisin_seq]["pos_liaisons"].append(elt)
#                                 for elt in chaine[0] :
#                                     if valeur_debut not in G.nodes[elt]["pos_liaisons"] and G.nodes[elt]["type"] == 1 :
#                                         G.nodes[elt]["pos_liaisons"].append(valeur_debut)
#                                         G.add_edge(num_voisin_seq, elt, label="CWW", long_range=False)
#                                         G.add_edge(elt, num_voisin_seq, label="CWW", long_range=False)
#                             else : 
#                                 G.nodes[num_voisin_seq]["pos_liaisons"].append(chaine)
                    
                #if nom_cle == ('1FJG', 'A') :
                #    print(new_position)
                #    print(num_sommet)
                #    print(compteur_tige)
                
                if i > 0 :
                    if int_tige == 1 :
                        if valeur_debut == 3 or valeur_debut == 4 :
                            G.add_edge(compteur_tige, num_sommet, label="B53", long_range=False)
                        else :
                            G.add_edge(num_sommet, compteur_tige, label="B53", long_range=False)
                    else :
                        if valeur_debut == 3 or valeur_debut == 4 :
                            G.add_edge(num_sommet, compteur_tige, label="B53", long_range=False)
                        else :
                            G.add_edge(compteur_tige, num_sommet, label="B53", long_range=False)
                    G.nodes[num_sommet]["poids"] = 1
                    compteur_tige = num_sommet
                
                #if nom_cle == ('1FJG', 'A') :
                #    print(new_position)
                #    print(compteur_tige)
                #    print(G.nodes.data())
                
                ## ajout de chacun des voisins du sommet actuel car il est de type 2 ou 3
                for voisin in voisins :
                    label_voisin = graphes[nom_cle][new_position][voisin]["label"]
                    if label_voisin != "B53" :
                        if voisin not in positions_ajoutees :
                            ajout_sommet(G, compteur, compteur_tige, (voisin,voisin), None, 1, label_voisin, positions_ajoutees, int_tige, valeur_debut, long_range=graphes[nom_cle][new_position][voisin]["long_range"])
                            compteur = compteur+1
                        else :
                            num_sommet = -1
                            #print(nom_cle)
                            #print(compteur_tige)
                            #print(G.nodes.data())
                            for noeud in G.nodes() :
#                                 print(G.nodes[noeud])
                                if voisin <= G.nodes[noeud]["position"][1] and voisin >= G.nodes[noeud]["position"][0] :
                                    num_sommet = noeud ## retrouver le numero du sommet  
                            if num_sommet == -1 :
                                print("probleme4")
                            deja_fait = False
                            for v in G[num_sommet] :
                                for edge in G[num_sommet][v] :
                                    if v == compteur_tige and G[num_sommet][v][edge]["label"] != "B53" : 
                                        deja_fait = True 
                            if deja_fait == False :
                                G.add_edge(num_sommet, compteur_tige, label=label_voisin, long_range=graphes[nom_cle][new_position][voisin]["long_range"])
                                G.add_edge(compteur_tige, num_sommet, label=label_voisin, long_range=graphes[nom_cle][new_position][voisin]["long_range"])
                type_sommet_prec = type_sommet_actuel
                poids_sommet = 1 
        
        
        if voisin_dans_chaine == False :
            chaine_sommet_voisin = -1
            chaine_sommet_voisin_prec = -1
            type_sommet_voisin_prec = None
            type_sommet_voisin = None   
            voisin_chaine_prec = -1
            voisin_chaine = -1       
        i = i+1
        
        
        
        position_prec = new_position
        if valeur_debut == 2 or valeur_debut == 1 :
            new_position = G.node[valeur_debut]["position"][0]-i*int_tige
        else : #normalement 4 ou 3
            new_position = G.node[valeur_debut]["position"][0]+i*int_tige
            
#     print(chaine)
    if poids_sommet != 1 or (type_sommet_actuel == 0 or type_sommet_actuel == 1 and poids_sommet == 1):
        deja_vu = False
        for k in range(min(position_prec_groupe, position_prec), max(position_prec, position_prec_groupe)+1) :
            if k in positions_ajoutees :
                deja_vu = True
        #if position_prec not in positions_ajoutees : 
        if deja_vu == False :
            if position_prec - position_prec_groupe <= 0 :
                ajout_sommet(G, compteur, compteur_tige, (position_prec,position_prec_groupe), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine)

            else : 
                ajout_sommet(G, compteur, compteur_tige, (position_prec_groupe,position_prec), type_sommet_prec, poids_sommet, "B53", positions_ajoutees, int_tige, valeur_debut, voisin_chaine = voisin_chaine)
            compteur_tige = compteur
            compteur = compteur + 1
        else : 
            num_sommet = -1
            for noeud in G.nodes() :
                for k in range(min(position_prec_groupe, position_prec), max(position_prec, position_prec_groupe)+1) :
                    if  k <= G.nodes[noeud]["position"][1] and k >= G.nodes[noeud]["position"][0] :
                        num_sommet = noeud
                        if valeur_debut not in G.nodes[noeud]["chaine"] :
                            G.nodes[noeud]["chaine"].append(valeur_debut)
            if int_tige == 1 :
                if valeur_debut == 3 or valeur_debut == 4 :
                    G.add_edge(compteur_tige, num_sommet, label="B53", long_range=False)
                else :
                    G.add_edge(num_sommet, compteur_tige, label="B53", long_range=False)
            else :
                if valeur_debut == 3 or valeur_debut == 4 :
                    G.add_edge(num_sommet, compteur_tige, label="B53", long_range=False)
                else :
                    G.add_edge(compteur_tige, num_sommet, label="B53", long_range=False)
                
            if position_prec - position_prec_groupe <= 0 :
#                 print(num_sommet)
                G.nodes[num_sommet]["position"] = (min(position_prec, G.nodes[num_sommet]["position"][0]), max(position_prec_groupe, G.nodes[num_sommet]["position"][1]))
            else :
                G.nodes[num_sommet]["position"] = (min(position_prec_groupe, G.nodes[num_sommet]["position"][0]), max(position_prec, G.nodes[num_sommet]["position"][1]))
            G.nodes[num_sommet]["poids"] = G.nodes[num_sommet]["position"][1] - G.nodes[num_sommet]["position"][0] +1   
            
#             if type_sommet_actuel == 1 :
# #                 print(chaine)
# #                 print(num_sommet)
#                 if len(chaine) > 0 :
#                     for elt in chaine[1] :
#                         if elt not in G.nodes[num_sommet]["pos_liaisons"] :
#                             G.nodes[num_sommet]["pos_liaisons"].append(elt)
#                     for elt in chaine[0] :
#                         if valeur_debut not in G.nodes[elt]["pos_liaisons"] and G.nodes[elt]["type"] == 1 :
#                             G.nodes[elt]["pos_liaisons"].append(valeur_debut)
#                             G.add_edge(num_sommet, elt, label="CWW", long_range=False)
#                             G.add_edge(elt, num_sommet, label="CWW", long_range=False)
#                 else : 
#                     G.nodes[num_sommet]["pos_liaisons"].append(chaine)               
#     
             
    return G


with open("fichiers_pickle/a-minor_test2.pickle", 'rb') as fichier_pickle :
    mon_depickler = pickle.Unpickler(fichier_pickle)
    tab_aminor = mon_depickler.load()
    
    with open("graphs_2.92.pickle", 'rb') as fichier_tout :
        mon_depickler_graphes = pickle.Unpickler(fichier_tout)
        graphes = mon_depickler_graphes.load()
        
        with open("fichier_test_graphes_version3_avec_boucles_test_digraph_new.txt", "w") as fichier :
            
            compteur_nb = 0
            compteur_nb_2 = 0
            for occ in tab_aminor :
                
                
                le_bon = False
                pas_bon = False
                for elt in liste :
                    if occ["num_PDB"]+"_"+ occ["num_ch"]+"_"+ str(occ["num_motif"])+"_"+ str(occ["num_occ"]) == elt :
                        pas_bon = True
#                 if occ["num_PDB"] == '5J7L' and occ["num_ch"] == 'DA' and occ["num_motif"] == 191 and occ["num_occ"] == 4 :
#                         print("ramounsnif 3")
#                         print(pas_bon)       
#                 if occ["num_PDB"] == '3JCS' and occ["num_ch"] == '1' and occ["num_motif"] == 48 and occ["num_occ"] == 18 :
#                     le_bon = True

                if pas_bon == False :
                    
                    positions_chaines = [[],[],[],[]]
                     
                    G = nx.MultiDiGraph()
                    i = 1
                    positions_ajoutees = []
                    for elt in occ["a_minor"] :
                        G.add_node(i, position = (elt,elt), type = i+10, poids=1, chaine=[i], pos_liaisons = [])
                        positions_ajoutees.append(elt)
                        
                        i = i+1
                    G.add_edge(1,2, label="CSS", long_range = True)
                    G.add_edge(2,1, label="CSS", long_range = True)
                    if(G.node[1]["position"][0] < G.node[3]["position"][0]) :
                        G.add_edge(1,3, label="B53", long_range = False)
                    else :
                        G.add_edge(3,1, label="B53", long_range = False)
                    G.add_edge(1,5, label="TSS", long_range = True)
                    G.add_edge(5,1, label="TSS", long_range = True)
                    if(G.node[2]["position"][0] < G.node[4]["position"][0]) :
                        G.add_edge(2,4, label="B53", long_range = False)
                    else :
                        G.add_edge(4,2, label="B53", long_range = False)
                    G.add_edge(2,5, label="CWW", long_range = False)
                    G.add_edge(5,2, label="CWW", long_range = False)
                    G.add_edge(3,4, label="CSS", long_range = True)
                    G.add_edge(4,3, label="CSS", long_range = True)
                    compteur = 6
                    compteur_tige = 2
                     
#                     print(G.nodes.data())
                    #print(G.edges.data())
                    #fichier.write(str(graphes[('1U9S', 'A')].nodes.data())+"\n")
                    #fichier.write(str(graphes[('1U9S', 'A')].edges.data()))
                    nom_cle = (occ["num_PDB"], occ["num_ch"])
                    #print(str(nom_cle) + str(occ["num_motif"]) + str(occ["num_occ"])) 
                     
#                     if nom_cle == ('4V88', 'A6') and occ["num_motif"] == 17 and occ["num_occ"] == 55 :
#                         print(nom_cle)
#                         print(occ["num_motif"])
#                         print(occ["num_occ"])
                     
                    ##Garder toutes les positions de la sequence 
                    if G.node[2]["position"][0] - G.node[4]["position"][0] < 0 : ## ordre de haut en bas
                        for i in range(10) :
                            if occ["a_minor"][1]-i > 0 :
                                positions_chaines[1].append(occ["a_minor"][1]-i)
                        for i in range(10) :
                            if occ["a_minor"][3]+i < graphes[nom_cle].number_of_nodes() :
                                positions_chaines[3].append(occ["a_minor"][3]+i)
                    else : ## ordre de bas en haut
                        for i in range(10) :
                            if occ["a_minor"][1]+i < graphes[nom_cle].number_of_nodes() :
                                positions_chaines[1].append(occ["a_minor"][1]+i)
                        for i in range(10) :
                            if occ["a_minor"][3]-i > 0 :
                                positions_chaines[3].append(occ["a_minor"][3]-i)
                                
                                
                    if G.node[1]["position"][0] - G.node[3]["position"][0] < 0 : ## ordre de haut en bas
                        for i in range(10) :
                            if occ["a_minor"][0]-i > 0 :
                                positions_chaines[0].append(occ["a_minor"][0]-i)
                        for i in range(10) :
                            if occ["a_minor"][2]+i < graphes[nom_cle].number_of_nodes() :
                                positions_chaines[2].append(occ["a_minor"][2]+i)
                    else : ## ordre de bas en haut
                        for i in range(10) :
                            if occ["a_minor"][0]+i < graphes[nom_cle].number_of_nodes() :
                                positions_chaines[0].append(occ["a_minor"][0]+i)
                        for i in range(10) :
                            if occ["a_minor"][2]-i > 0 :
                                positions_chaines[2].append(occ["a_minor"][2]-i)
                     
                      
                    ##Connaitre l'ordre des positions sur la sequence
                    int_tige = 0
                    if G.node[2]["position"][0] - G.node[4]["position"][0] < 0 : ## ordre de haut en bas
                        int_tige = 1
                    else : ## ordre de bas en haut
                        int_tige = -1
                    #compteur_tige2 = G.node[5]["position"][0] + int_tige
                     
                    ##Initialisation de la boucle 1
                    #===================================================================
                    G = extension_tige(G, graphes, nom_cle, compteur, compteur_tige, positions_ajoutees, int_tige)
                    #print(G.nodes.data())
                    #print(positions_ajoutees)
                    #if nom_cle == ('1FJG', 'A') :
                    #    print(G.nodes.data())
                    #    print(G.edges.data())
                     
                    compteur = G.number_of_nodes()+1
                         
                    #compteur_tige2 = G.node[5]["position"][0] - int_tige
                    compteur_tige = 4
                     
#                     print(nom_cle)
#                     print(occ["num_motif"])
#                     print(occ["num_occ"])
                     
                    G = extension_tige(G, graphes, nom_cle, compteur, compteur_tige, positions_ajoutees, int_tige)  
 
                    compteur_tige = 1 
                    compteur = G.number_of_nodes()+1
                    if G.node[1]["position"][0] - G.node[3]["position"][0] < 0 : ## ordre de haut en bas
                        int_tige = 1
                    else : ## ordre de bas en haut
                        int_tige = -1
                      
                     
                      
                    G = extension_tige(G, graphes, nom_cle, compteur, compteur_tige, positions_ajoutees, int_tige) 
                     
 
                    compteur_tige = 3
                    compteur = G.number_of_nodes()+1
                     
                    G = extension_tige(G, graphes, nom_cle, compteur, compteur_tige, positions_ajoutees, int_tige) 
                     
                     
                     
#                     compteur = G.number_of_nodes()+1
#                     compteur_tige = 1
                    #G = tige(G, graphes, nom_cle, compteur, compteur_tige, positions_ajoutees) 
                    #print(G.nodes.data())
                      

                    fichier.write(str(nom_cle) + " " + str(occ["num_motif"]) + " " + str(occ["num_occ"]) + "\n")
                    for noeud, data in G.nodes(data=True) :
                        fichier.write(str(noeud) + " " + str(data) +"\n")
                        
                    for u,v,data in G.edges(data=True) :
                        fichier.write(str((u,v)) + " " + str(data)+"\n")
                    
# 
                    with open("graphes_extension/fichier_{}.pickle".format(str(occ["num_PDB"]) + "_" + str(occ["num_ch"]) + "_" + str(occ["num_motif"]) + "_" + str(occ["num_occ"])), "wb") as fichier_sortie :
                        mon_pickler = pickle.Pickler(fichier_sortie)
                        mon_pickler.dump(G)
                        
                        
                    
            
            #pos=nx.spring_layout(G)
        
            #===================================================================