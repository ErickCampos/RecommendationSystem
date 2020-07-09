import matplotlib.pyplot as plt

rmse = [1.11493
,1.11116
,1.10948
,1.10870
,1.10822
,1.10783
,1.10755
,1.10751
,1.1072
,1.1072
,1.10718
,1.10697
,1.10689
,1.10682]

k = [250
,500
,750
,1000
,1250
,1500
,1750
,2000
,2250
,2500
,2750
,3000
,3250
,3500]

time = [123
,124
,126
,126
,127
,128
,129
,130
,131
,374
,120
,122
,127
,123]

fig = plt.figure()
plt.plot(k,time)
plt.ylabel("Tempo (s)",fontsize='18', fontweight='bold')
plt.xlabel("K",fontsize='18', fontweight='bold')
plt.xticks(k)
plt.grid()
plt.show()


