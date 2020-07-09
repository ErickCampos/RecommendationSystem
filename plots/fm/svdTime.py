import matplotlib.pyplot as plt
rmse = [1.10878, 1.10835, 1.10785, 1.10736, 1.10724, 1.10728, 1.10709, 1.10697,
1.10693, 1.10678, 1.10671, 1.10672, 1.10669, 1.10661]

rmse = [1.08042
,1.07577
,1.07568
,1.07725
,1.07796
,1.08112
,1.0816
,1.0836
,1.08533
,1.08801
,1.08752
,1.08847
,1.09135]

k = [5 ,25 ,50 ,75 ,100 ,125 ,150 ,175 ,200 ,225 ,250 ,275 ,300]

time = [1 ,2 ,4 ,5 ,6 ,9 ,10 ,10 ,12 ,14 ,16 ,18 ,20]

fig = plt.figure()
plt.plot(k,time)
plt.ylabel("Tempo (s)",fontsize='18', fontweight='bold')
plt.xlabel("K",fontsize='18', fontweight='bold')
plt.xticks(k)
plt.grid()
plt.show()


