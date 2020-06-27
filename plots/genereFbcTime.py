import matplotlib.pyplot as plt

k = [250 ,500 ,750 ,1000 ,1250 ,1500 ,1750 ,2000 ,2250 ,2500 ,2750 ,3000 ,3250
,3500]

time = [115 ,116 ,117 ,119 ,118 ,120 ,120 ,120 ,121 ,122 ,122 ,124 ,124 ,127]

fig = plt.figure()
plt.plot(k,time)
plt.ylabel("Tempo (s)")
plt.xlabel("K")
plt.xticks(k)
plt.show()
