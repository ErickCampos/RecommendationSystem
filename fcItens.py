import numpy as np
import pandas as pd
import math

def pred(user,item,k):
    mat = np.load('train.npy')
    iItem = []
    jItem = []
    sim = []
    for i in range(0,3564):#itens
        if math.isnan(mat[user][i]):#verifica se item foi avaliado pelo usuário testado
            continue
        if i == item:#verifica se o item é igual ao item testado?
            continue
        iBias = np.nanmean(mat[:,item]) #vies do item testado
        jBias = np.nanmean(mat[:,i]) #vies de cada item
        if math.isnan(iBias):
            iBias = 0
        if math.isnan(jBias):
             jBias = 0
        for j in range(0,3974):#usuarios
            sum1 = 0
            sum2 = 0
            sumI = 0
            sumJ = 0
            result = 0
            if math.isnan(mat[j][item]) or j == user: #verifica se não tem nota ou usuário atual é igual o usuário de teste
                continue
            if math.isnan(mat[j][item]) or math.isnan(mat[j][i]):# se os itens foram simultaneamente votados
                continue
            else:
                iItem.append(mat[j][item])#conjunto das notas do item testado
                jItem.append(mat[j][i])#conjunto das notas do item fo laço
        if len(iItem) == 0:                                                         
            iItem.clear()
            jItem.clear()
            continue
        for x in range(0,len(iItem)):
            sum1 += (iItem[x] - iBias) * (jItem[x] - jBias) #somatorio do numerador da similaridade
            sumI += np.power((iItem[x]-iBias),2)
            sumJ += np.power((jItem[x]-jBias),2)
            sum1 = round(sum1,4)
            sumI = round(sumI,4) 
            sumJ = round(sumJ,4) 
        result = sum1/(np.sqrt(sumI) * np.sqrt(sumJ)) #similaridade
        result = round(result,4)
        if math.isnan(result):
            iItem.clear()
            jItem.clear()
            continue
        sim.append((result,i))#conjunto de simularidades e seus respectivos item (sim, item)
        iItem.clear()
        jItem.clear()
    sim = sorted(sim, key=lambda tup: tup[0],reverse=True)#ordena de forma decrescente a similaridade 
    sum1 = 0
    sum2 = 0
    pred = 0
    #print(len(sim))
    if k > len(sim):
        k = len(sim)
    for y in range(0,k):
        it = sim[y][1]
        sum1 += sim[y][0] * mat[user][it]
        sum2 += sim[y][0]
        sum1 = round(sum1,4)
        sum2 = round(sum2,4)
        #print(sum1, end=' ') 
        #print(sum2)
    if sum2 == 0:
        pass
    pred = sum1/sum2#predição
    pred = round(pred,4)
    print(pred)

if __name__=='__main__':
    test = pd.read_csv('data/test.csv')
    for ind in test.index:
        user = test['user_id'][ind]-1
        item = test['movie_id'][ind]-1
        pred(user,item,10)
