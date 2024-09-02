import matplotlib.pyplot as plt

G = 6.674 * (10 ** (-20)) # km^3 kg^-1 s^-2
Mp = 5.972 * (10 ** 24) # kg
Kp = G * Mp

r_n = 20_000 # km
theta_n = 0 # deg

vr_n = 0 # km/s
vt_n = 5 # km/s

del_t = 10 # secs

del_r_n = vr_n * del_t
del_theta_n = vt_n * del_t / r_n

r, theta = [r_n], [theta_n]

Tp = 0

for i in range(1, 50000):
    Tp += del_t

    r_n1 = r_n + del_r_n
    theta_n1 = (theta_n + del_theta_n)
    del_r_n1 = del_r_n + (((r_n + (0.5 * del_r_n)) * (del_theta_n ** 2)) - (Kp * (del_t ** 2) / (r_n ** 2)))
    del_theta_n1 = (del_theta_n - ((2 * del_r_n * del_theta_n) / (r_n + 0.5 * del_r_n)))
    
    if theta_n1 >= 360:
        print("Time period:", Tp, "seconds")
    #print(r_n1, theta_n1, del_r_n1, del_theta_n1)
    
    r.append(r_n1)
    theta.append(theta_n1)

    r_n = r_n1
    theta_n = theta_n1
    del_r_n = del_r_n1
    del_theta_n = del_theta_n1

#print(theta, r)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
plt.show()
