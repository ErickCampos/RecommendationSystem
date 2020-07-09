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

time = [122
,123
,123
,126
,129
,131
,133
,136
,139
,140
,142
,143
,145]

fig = plt.figure()
plt.plot(k,time)
plt.ylabel("Tempo (s)",fontsize='18', fontweight='bold')
plt.xlabel("K",fontsize='18', fontweight='bold')
plt.xticks(k)
plt.grid()
plt.show()


