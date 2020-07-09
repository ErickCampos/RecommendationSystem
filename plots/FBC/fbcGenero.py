import matplotlib.pyplot as plt

rmse = [1.11813
,1.11474
,1.11108
,1.11018
,1.10934
,1.10994
,1.1095
,1.1092
,1.10901
,1.10882
,1.10878
,1.10877
,1.10852]

k = [5 ,25 ,50 ,75 ,100 ,125 ,150 ,175 ,200 ,225 ,250 ,275 ,300]

time = [115 ,116 ,117 ,119 ,118 ,120 ,120 ,120 ,121 ,122 ,122 ,124 ,124 ,127]

fig = plt.figure()
plt.plot(k,rmse)
plt.ylabel("RMSE",fontsize='18', fontweight='bold')
plt.xlabel("K",fontsize='18', fontweight='bold')
plt.xticks(k)
plt.grid()
plt.show()


