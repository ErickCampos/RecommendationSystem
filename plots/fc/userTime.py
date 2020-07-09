import matplotlib.pyplot as plt
rmse = [1.10878, 1.10835, 1.10785, 1.10736, 1.10724, 1.10728, 1.10709, 1.10697,
1.10693, 1.10678, 1.10671, 1.10672, 1.10669, 1.10661]


k = [5 ,25 ,50 ,75 ,100 ,125 ,150 ,175 ,200 ,225 ,250 ,275 ,300]

time = [193 ,195 ,207 ,210 ,210 ,212 ,215 ,218 ,232 ,233 ,236 ,240 ,245]

fig = plt.figure()
plt.plot(k,time)
plt.ylabel("Tempo (s)",fontsize='18', fontweight='bold')
plt.xlabel("K",fontsize='18', fontweight='bold')
plt.xticks(k)
plt.grid()
plt.show()


