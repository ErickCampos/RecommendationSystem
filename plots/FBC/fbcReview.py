import matplotlib.pyplot as plt

rmse = [1.88856
,1.88725
,1.88809
,1.8885
,1.88872
,1.88918
,1.8893
,1.88949
,1.88953
,1.88967
,1.88979
,1.8898
,1.88995]

k = [5 ,25 ,50 ,75 ,100 ,125 ,150 ,175 ,200 ,225 ,250 ,275 ,300]

time = [113
,113
,113
,113
,114
,114
,115
,116
,117
,117
,118
,119
,120
,121
,122
,123
,124
,125
,127]

fig = plt.figure()
plt.plot(k,rmse)
plt.ylabel("RMSE",fontsize='18', fontweight='bold')
plt.xlabel("K",fontsize='18', fontweight='bold')
plt.xticks(k)
plt.grid()
plt.show()


