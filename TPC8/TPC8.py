#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def convBool(val):
    return val=='true'


# In[ ]:


# Descreve em texto o teu 
# 
# BdEMD = [EMD]
# EMD = [idnovo,data, nome, idade, género, morada, modalidade, clube,email,federado,resultado]
#
# Leitura/carregamento da informação do ficheiro

def lerDataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd = []
    f.readline()
    
    for linha in f:
        emd=[]
        novalinha=linha.strip("\n")
        campos=novalinha.split(",")
        emd.append("emd"+str(campos[1])) 
        emd.append(campos[2])
        emd.append(campos[4]+""+ campos[3])  
        emd=emd + campos[5:]
        emd[-1]=convBool(emd[-1])
        emd[-2]=convBool(emd[-2])
        bd.append(emd)
        
    return bd


# In[ ]:


def listarDataset(bd):
    espaco="        "
    inter=[]
    inter.append("id"+espaco+"Nome"+espaco+"Data"+espaco+"Resultado"+espaco)
    #print("---------------------------------------------------------")
    for exame in bd:
        if exame[-1]:
            res="Apto"
        else:
            res="Não"
        inter.append(exame[0]+" | "+exame[2]+" | "+exame[1]+" | "+res)
    return inter

# In[ ]:


def consultarDataset(bd, id):
    stop=True
    res=" "
    while stop==True:
        for e in bd:
            if e[0]==id:
                res=(id+" | "+ str(e[1])+" | "+str(e[2])+" | "+str(e[3])+ " | "+str( e[4])+" | "+str(e[5])+" | "+str(e[6])+" | "+str(e[7])+" | "+ str(e[8])+" | "+str( e[9])+" | "+str(e[10]))
                stop=False
    return res    


def modalidades(bd):
    modalidades=[]
    for exame in bd:
        if exame[6] not in modalidades:
            modalidades.append(exame[6]) 
    
    return sorted(modalidades)


def distribPorAno(bd):
    an={}
    for e in bd:
        data=e[1][0:4]
        if data in an:
            an[data]=an[data]+1
        else:
            an[data]=1
    anl=list(an.items())  
    anl.sort(key= lambda x:x[0])
    res=dict(anl)
    return res

def distrib(bd, ind):
    dis={}
    for e in bd:
        if e[ind] in dis:
            dis[e[ind]]=dis[e[ind]]+1
        else:
            dis[e[ind]]=1     
    disl=list(dis.items())
    disl.sort(key= lambda x:x[0])
    res=dict(disl)
    return res

def plotDistribPorAno(bd):
    import matplotlib.pyplot as plt
    basedados=distribPorAno(bd)
    left = [] 
    height = []
    tick_label=[]
    i=1
    for ano in basedados:
        left.append(i)
        i=i+2
        height.append(basedados[ano])
        tick_label.append(ano)
   
    plt.bar(left, height, tick_label = tick_label,
        width = 1, color = ['teal'])
    plt.show()
def plotDist(bd,ind,oque):
    import matplotlib.pyplot as plt
    basedados=distrib(bd,ind)
    left = [] 
    height = []
    tick_label=[]
    i=1
    if oque in ["Modalidades", "Clubes"]:
        for chave in basedados:
            left.append(i)
            i=i+3
            height.append(basedados[chave])
            tick_label.append(chave)
        plt.xticks(rotation=75)
        plt.bar(left, height, tick_label = tick_label, width = 2, color = ['teal'])
        
    else:
        for chave in basedados:
            left.append(i)
            i=i+1
            height.append(basedados[chave])
            tick_label.append(chave)
        plt.xticks(rotation=0) 
        plt.bar(left, height, tick_label = tick_label, width = 0.5, color = ['teal'])
       
        
    plt.xlabel(oque)
    plt.ylabel("Número")            
    
    plt.show()