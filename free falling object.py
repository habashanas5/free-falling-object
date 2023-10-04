import matplotlib.pyplot as plt
g = - 9.81
v = 20
p = 11
dt = 0.01
duration = 5
t = 0
iteration = int(duration / dt)
t1 = []
p1 = []
v1 = []
for i in range(iteration):
    v += g*dt
    p += v*dt
    t = i * dt
    t1.append(t)
    p1.append(p)
    v1.append(v)

plt.plot(t1, v1 , label = "Velocity line")
plt.plot(t1, p1 , label = "Position line")
plt.legend()
plt.show()
