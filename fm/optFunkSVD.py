import numpy as np
import pandas as pd
import matplotlib.pyplot as plt                                                 


class gradient:
    globalMean = 0
    nUsers = 3974
    nItens = 3564
    bu = np.zeros(nUsers)
    bi = np.zeros(nItens)

    k = 0
    lr = 0
    reg = 0
    miter = 0

    def __init__(self,k,lr,reg,miter):
        self.k = k
        self.lr = lr
        self.reg = reg
        self.miter = miter
        self.p = np.full((self.nUsers,k),0.1)
        self.q = np.full((self.nUsers,k),0.1)

    def optFunkSVD(self):
        mat = np.load('../train.npy')
        dados = pd.read_csv('../data/train.csv')
        self.globalMean = np.nanmean(mat)
        for l in range(0,self.miter):
            error = 0
            for ind in dados.index:
                u = dados['user_id'][ind]-1                                                
                i = dados['movie_id'][ind]-1                                             
                r = dados['rating'][ind]
                pred = self.globalMean + self.bu[u] + self.bi[i] + np.dot(self.p[u,:],self.q[i,:])
                e = r - pred
                error += np.power(e,2)
                #plt.scatter(e,(f+1)*(l+1))
                #plt.pause(0.02)
                self.bu[u] = self.bu[u] + self.lr*e - self.reg*self.bu[u] 
                self.bi[i] = self.bi[i] + self.lr*e - self.reg*self.bi[i]
                for f in range(0,self.k):
                    temp = self.p[u][f]
                    self.p[u][f] = self.p[u][f] + self.lr*(e * self.q[i][f] - self.reg * self.p[u][f])
                    self.q[i][f] = self.q[i][f] + self.lr * (e * temp - self.reg * self.q[i][f])
            rmse = np.sqrt(error/len(dados.index))
            print(rmse)
        #plt.show()

    def predict(self,user,item):
        pred = self.globalMean + self.bu[user] + self.bi[item] + np.dot(self.p[user,:],self.q[item,:])
        print(pred)

if __name__=='__main__':
    ob = gradient(4,0.05,0.02,500)
    ob.optFunkSVD()
    test = pd.read_csv('../data/test.csv')
    for ind in test.index:
        user = test['user_id'][ind]-1
        item = test['movie_id'][ind]-1
        ob.predict(user,item)        