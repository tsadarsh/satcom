import matplotlib.pyplot as plt
from pprint import pprint

G = 6.674 * (10 ** (-20)) # km^3 kg^-1 s^-2
Mp = 5.972 * (10 ** 24) # kg
Kp = G * Mp

r_n = 20_000 # km
theta_n = 0 # rad

vr_n = 0 # km/s
vt_n = 5 # km/s

del_t = 10 # secs

del_r_n = vr_n * del_t
del_theta_n = vt_n * del_t / r_n

r, theta = [r_n], [theta_n]

Tp = 0
theta_cache = 1.57

for i in range(1, 50000):
    Tp += del_t

    r_n1 = r_n + del_r_n
    theta_n1 = (theta_n + del_theta_n)
    del_r_n1 = del_r_n + (((r_n + (0.5 * del_r_n)) * (del_theta_n ** 2)) - (Kp * (del_t ** 2) / (r_n ** 2)))
    del_theta_n1 = (del_theta_n - ((2 * del_r_n * del_theta_n) / (r_n + 0.5 * del_r_n)))
    
    # if theta_cache > (theta_n1 % 3.14):
    #     print("Time period:", Tp, "seconds")
    #     Tp = 0
    # else:
    #     theta_cache = theta_n1 % 3.14
    
    #print(r_n1, theta_n1, del_r_n1, del_theta_n1)
    
    r.append(r_n1)
    theta.append(theta_n1)

    r_n = r_n1
    theta_n = theta_n1
    del_r_n = del_r_n1
    del_theta_n = del_theta_n1

#fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
#ax.plot(theta, r)
bro = [i % 6.28 for i in theta]
count = 0
for i in range(1, len(bro)):
    if bro[i-1] > bro[i]:
        print(count * del_t / (60 * 24))
        count = 0
    else:
        count += 1

# with open("dump.txt", "w") as f:
#     for i in bro:
#         f.write(str(i))
#         f.write("\n")
# # pprint(str(bro))
plt.plot(bro)
plt.show()
