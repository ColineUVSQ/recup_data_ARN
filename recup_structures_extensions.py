'''
Created on 29 janv. 2019

@author: coline
'''
import pickle
import networkx as nx

liste = ['5J7L_DA_191_3', '5J7L_DA_191_4', '5FDU_1A_301_1', '5J7L_DA_301_2', '5DM6_X_334_1', '5FDU_1A_334_2', '4V9F_0_335_1', '5J7L_DA_335_2', '3JCS_1_137_4', '4V88_A5_290_1', '4V88_A6_314_2', '5J7L_DA_218_3', '4V9F_0_251_2', '1FJG_A_62_8', '5J7L_DA_137_1', '4V9F_0_118_1', '4V9F_0_62_2', '5J7L_DA_271_2', '4V9F_0_224_1', '5DM6_X_197_1', '3GX5_A_138_6', '1FJG_A_317_2', '5J5B_BA_317_1', '1FJG_A_326_1', '5DM6_X_137_3', '5J5B_BA_314_1', '4V9F_0_134_6', '4V9F_0_328_1', '4V9F_0_197_2', '4V9F_0_62_16', '5J7L_DA_282_2', '4V88_A5_137_2', '5FDU_1A_224_3', '5J7L_DA_326_2']

def recup_structure() :
    with open("fichiers_pickle/a-minor_test2.pickle", 'rb') as fichier_pickle :
            mon_depickler = pickle.Unpickler(fichier_pickle)
            tab_aminor = mon_depickler.load()
        
            with open("graphs_2.92.pickle", 'rb') as fichier_tout :
                mon_depickler_graphes = pickle.Unpickler(fichier_tout)
                graphes = mon_depickler_graphes.load()
            
                dico_graphes = {}
                for occ in tab_aminor :
                    est_la = False
                    for elt in liste :
                        if occ["num_PDB"]+"_"+ occ["num_ch"]+"_"+ str(occ["num_motif"])+"_"+ str(occ["num_occ"]) == elt :
                            est_la = True
                            
                    if est_la == False :
                        num = (occ["num_PDB"], occ["num_ch"])
                        
                        tab_id = []
                        graphe_a_minor = nx.MultiDiGraph()
                        
                        for j in range(5) :
                            pos = occ["a_minor"][j]
                        
                            if pos not in graphe_a_minor.nodes() :
                                #tab_id.append(pos)
                                graphe_a_minor.add_node(pos, **graphes[num].nodes[pos])
                                for voisin in graphes[num][pos] :
                                    
                                    deja_vu = False
                                    for voisin_deja_vu in graphe_a_minor.successors(pos) :
                                        for edge in graphe_a_minor[pos][voisin_deja_vu] :
                                            if voisin == voisin_deja_vu and (voisin in graphes[num].successors(pos) and graphe_a_minor[pos][voisin_deja_vu][edge]["label"] == graphes[num].edges[pos, voisin]["label"]) or (voisin in graphes[num].predecessors(pos) and graphe_a_minor[pos][voisin_deja_vu][edge]["label"] == graphes[num].edges[voisin, pos]["label"]) :
                                                deja_vu = True
                                    for voisin_deja_vu in graphe_a_minor.predecessors(pos) :
                                        for edge in graphe_a_minor[voisin_deja_vu][pos] :
                                            if voisin == voisin_deja_vu and (voisin in graphes[num].successors(pos) and graphe_a_minor[voisin_deja_vu][pos][edge]["label"] == graphes[num].edges[pos, voisin]["label"]) or (voisin in graphes[num].predecessors(pos) and graphe_a_minor[voisin_deja_vu][pos][edge]["label"] == graphes[num].edges[voisin, pos]["label"]) :
                                                deja_vu = True
                                                
                                    if deja_vu == False :
                                        if voisin not in graphe_a_minor.nodes() :
                                            graphe_a_minor.add_node(voisin, **graphes[num].nodes[voisin])
                                            
                                        if voisin in graphes[num].successors(pos) :
                                            graphe_a_minor.add_edge(pos, voisin, **graphes[num].edges[pos, voisin])
                                            if graphes[num].edges[pos, voisin]["label"] != 'B53' :
                                                graphe_a_minor.add_edge(voisin, pos, **graphes[num].edges[voisin, pos])
                                        else :
                                            graphe_a_minor.add_edge(voisin, pos, **graphes[num].edges[voisin, pos])
                                            if graphes[num].edges[voisin, pos]["label"] != 'B53' :
                                                graphe_a_minor.add_edge(pos, voisin **graphes[num].edges[pos, voisin])
                            
                            
                            if j < 4 :
                                for i in range(1,10) :
                                    if pos - i > 0 and pos + i < graphes[num].number_of_nodes() :
                                        if pos - i not in graphe_a_minor.nodes() :
                                            #tab_id.append(pos - i)
                                            graphe_a_minor.add_node(pos-i, **graphes[num].nodes[pos-i])
                                        if pos + i not in graphe_a_minor.nodes() :
                                            #tab_id.append(pos + i)
                                            graphe_a_minor.add_node(pos+i, **graphes[num].nodes[pos+i])
#                                         
#                                         if occ["num_PDB"] == '5DM6' and occ["num_ch"] == 'X' and occ["num_motif"] == 328 and occ["num_occ"] == 2 :
#                                             print(pos-i)
#                                             print(graphes[num][pos-i])
#                                             print(pos+i)
#                                             print(graphes[num][pos+i])
                                        
                                        for voisin in graphes[num][pos-i] :
                                            
                                            
                                            deja_vu = False
                                            for voisin_deja_vu in graphe_a_minor.successors(pos-i) :
                                                for edge in graphe_a_minor[pos-i][voisin_deja_vu] :
                                                    if voisin == voisin_deja_vu and (voisin in graphes[num].successors(pos-i) and graphe_a_minor[pos-i][voisin_deja_vu][edge]["label"] == graphes[num].edges[pos-i, voisin]["label"]) or (voisin in graphes[num].predecessors(pos-i) and graphe_a_minor[pos-i][voisin_deja_vu][edge]["label"] == graphes[num].edges[voisin, pos-i]["label"]) :
                                                        deja_vu = True
                                            for voisin_deja_vu in graphe_a_minor.predecessors(pos-i) :
                                                for edge in graphe_a_minor[voisin_deja_vu][pos-i] :
                                                    if voisin == voisin_deja_vu and (voisin in graphes[num].successors(pos-i) and graphe_a_minor[voisin_deja_vu][pos-i][edge]["label"] == graphes[num].edges[pos-i, voisin]["label"]) or (voisin in graphes[num].predecessors(pos-i) and graphe_a_minor[voisin_deja_vu][pos-i][edge]["label"] == graphes[num].edges[voisin, pos-i]["label"]) :
                                                        deja_vu = True
                                                        
                                            if deja_vu == False :
                                                if voisin not in graphe_a_minor.nodes() :
                                                    graphe_a_minor.add_node(voisin, **graphes[num].nodes[voisin])
                                                
                                                if voisin in graphes[num].successors(pos-i) :
                                                    graphe_a_minor.add_edge(pos-i, voisin, **graphes[num].edges[pos-i, voisin])
                                                    if graphes[num].edges[pos-i, voisin]["label"] != 'B53' :
                                                        graphe_a_minor.add_edge(voisin, pos-i, **graphes[num].edges[voisin, pos-i])
                                                else :
                                                    graphe_a_minor.add_edge(voisin, pos-i, **graphes[num].edges[voisin, pos-i])
                                                    if graphes[num].edges[voisin, pos-i]["label"] != 'B53' :
                                                        graphe_a_minor.add_edge(pos-i, voisin **graphes[num].edges[pos-i, voisin])
#                                                     
#                                             if ((pos-i, voisin) in graphes[num].edges() and graphes[num].edges[pos-i,voisin]["label"] != 'B53') or ((voisin, pos-i) in graphes[num].edges() and graphes[num].edges[voisin, pos-i]["label"] != 'B53') :
#                                                 if voisin not in tab_id :
#                                                     tab_id.append(voisin)
                                        
                                        if occ["num_PDB"] == '5DM6' and occ["num_ch"] == 'X' and occ["num_motif"] == 328 and occ["num_occ"] == 2 :
                                            print("pos + i : " + str(pos+i))
                                        for voisin in graphes[num][pos+i] :
                                            if i < 9 or (voisin in graphes[num].successors(pos+i) and graphes[num].edges[pos+i, voisin]["label"] != 'B53') or (voisin in graphes[num].predecessors(pos+i) and graphes[num].edges[voisin, pos+i]["label"] != 'B53') : 
                                                if occ["num_PDB"] == '5DM6' and occ["num_ch"] == 'X' and occ["num_motif"] == 328 and occ["num_occ"] == 2 :
                                                    print(voisin)
                                                deja_vu = False
                                                for voisin_deja_vu in graphe_a_minor.successors(pos+i) :
                                                    for edge in graphe_a_minor[pos+i][voisin_deja_vu] :
                                                        if voisin == voisin_deja_vu and (voisin in graphes[num].successors(pos+i) and graphe_a_minor[pos+i][voisin_deja_vu][edge]["label"] == graphes[num].edges[pos+i, voisin]["label"]) or (voisin in graphes[num].predecessors(pos+i) and graphe_a_minor[pos+i][voisin_deja_vu][edge]["label"] == graphes[num].edges[voisin, pos+i]["label"]) :
                                                            deja_vu = True
                                                            
                                                for voisin_deja_vu in graphe_a_minor.predecessors(pos+i) :
                                                    for edge in graphe_a_minor[voisin_deja_vu][pos+i] :
                                                        if voisin == voisin_deja_vu and (voisin in graphes[num].successors(pos+i) and graphe_a_minor[voisin_deja_vu][pos+i][edge]["label"] == graphes[num].edges[pos+i, voisin]["label"]) or (voisin in graphes[num].predecessors(pos+i) and graphe_a_minor[voisin_deja_vu][pos+i][edge]["label"] == graphes[num].edges[voisin, pos+i]["label"]) :
                                                            deja_vu = True
                                                            if occ["num_PDB"] == '5DM6' and occ["num_ch"] == 'X' and occ["num_motif"] == 328 and occ["num_occ"] == 2 :
                                                                print("petit rat")
                                                
                                                if occ["num_PDB"] == '5DM6' and occ["num_ch"] == 'X' and occ["num_motif"] == 328 and occ["num_occ"] == 2 :
                                                    print(deja_vu)            
                                                if deja_vu == False :
                                                    if voisin not in graphe_a_minor.nodes() :
                                                        graphe_a_minor.add_node(voisin, **graphes[num].nodes[voisin])
                                                        
                                                    if voisin in graphes[num].successors(pos+i) :
                                                        graphe_a_minor.add_edge(pos+i, voisin, **graphes[num].edges[pos+i, voisin])
                                                        if graphes[num].edges[pos+i, voisin]["label"] != 'B53' :
                                                            graphe_a_minor.add_edge(voisin, pos+i, **graphes[num].edges[voisin, pos+i])
                                                    else :
                                                        graphe_a_minor.add_edge(voisin, pos+i, **graphes[num].edges[voisin, pos+i])
                                                        if graphes[num].edges[voisin, pos+i]["label"] != 'B53' :
                                                            graphe_a_minor.add_edge(pos+i, voisin **graphes[num].edges[pos+i, voisin])
                                                
#                                         if occ["num_PDB"] == '5DM6' and occ["num_ch"] == 'X' and occ["num_motif"] == 328 and occ["num_occ"] == 2 :
#                                             print("petit rat")
                                        if (pos-i, pos-i+1) in graphe_a_minor.edges() : 
                                            vu = False
                                            for edge in graphe_a_minor[pos-i][pos-i+1] :
                                                if graphe_a_minor[pos-i][pos-i+1][edge]["label"] == 'B53'  :
                                                    vu = True
                                            if vu == False :
                                                graphe_a_minor.add_edge(pos-i, pos-i+1, label= 'B53', long_range=False)
                                                
                                        if (pos+i-1, pos+i) in graphe_a_minor.edges() :
                                            vu = False
                                            for edge in graphe_a_minor[pos+i-1][pos+i] :
                                                if graphe_a_minor[pos+i-1][pos+i][edge]["label"] == 'B53' :
                                                    vu = True
                                            if vu == False :
                                                graphe_a_minor.add_edge(pos+i-1, pos+i, label= 'B53', long_range=False)
#                                                 if occ["num_PDB"] == '5DM6' and occ["num_ch"] == 'X' and occ["num_motif"] == 328 and occ["num_occ"] == 2 :
#                                                     print("gros rat")
#                                                     print(pos+i-1)
                                            
#                                             if ((pos+i, voisin) in graphes[num].edges() and graphes[num].edges[pos+i,voisin]["label"] != 'B53') or ((voisin, pos+i) in graphes[num].edges() and graphes[num].edges[voisin, pos+i]["label"] != 'B53') :
#                                                 if voisin not in tab_id :
#                                                     tab_id.append(voisin)
#                         if occ["num_PDB"] == '5DM6' and occ["num_ch"] == 'X' and occ["num_motif"] == 328 and occ["num_occ"] == 2 :
#                             print(occ["a_minor"])
#                             print(tab_id)
#                             print(len(tab_id))
                            
                        #print(tab_id)
                        
                        #graphe_a_minor = graphes[num].subgraph(tab_id)
                        #print(graphe_a_minor.nodes.data())
                        
                        if not graphe_a_minor.has_edge(occ["a_minor"][0], occ["a_minor"][1]) :
                            graphe_a_minor.add_edge(occ["a_minor"][0], occ["a_minor"][1], label="CSS", long_range=True)
                            graphe_a_minor.add_edge(occ["a_minor"][1], occ["a_minor"][0], label="CSS", long_range=True)
                        if not graphe_a_minor.has_edge(occ["a_minor"][2], occ["a_minor"][3]) :
                            graphe_a_minor.add_edge(occ["a_minor"][2], occ["a_minor"][3], label="CSS", long_range=True)
                            graphe_a_minor.add_edge(occ["a_minor"][3], occ["a_minor"][2], label="CSS", long_range=True)
                        if not graphe_a_minor.has_edge(occ["a_minor"][0], occ["a_minor"][4]) :
                            graphe_a_minor.add_edge(occ["a_minor"][0], occ["a_minor"][4], label="TSS", long_range=True)
                            graphe_a_minor.add_edge(occ["a_minor"][4], occ["a_minor"][0], label="TSS", long_range=True)
                            
                        dico_graphes.update({(occ["num_PDB"], occ["num_ch"], occ["num_motif"], occ["num_occ"]) : graphe_a_minor.copy()})
                        
                #print(dico_graphes)     
                #print(graphes)   
                with open("grands_graphes.pickle", 'wb') as fichier_ecriture :
                    mon_pickler = pickle.Pickler(fichier_ecriture)
                    mon_pickler.dump(dico_graphes)
            
if __name__ == '__main__':
    recup_structure()
    with open("grands_graphes.pickle", 'rb') as fichier :
        mon_depickler = pickle.Unpickler(fichier)
        dico_graphes = mon_depickler.load()
        
        print(len(dico_graphes))            
        print(dico_graphes[('5FDU', '1A', 25, 78)].nodes.data())
        print(dico_graphes[('5FDU', '1A', 25, 78)].edges.data())
        
        print(dico_graphes[('5FDU', '1A', 25, 78)][490])
             
        
    
                    
                        