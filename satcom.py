import matplotlib.pyplot as plt
from pprint import pprint

# G = 6.674 * (10 ** (-20)) # km^3 kg^-1 s^-2
G = 6.674 * (10 ** (-29)) # Mkm^3 kg^-1 s^-2
#Mp = 5.972 * (10 ** 24) # kg
Mp = 1.9891 * (10 ** 30) # kg (sun)

Kp = G * Mp

r_n = 5_270_000 # Mkm
theta_n = 0 # rad

vr_n = 0 # km/s
vt_n = 0.00091 # km/s

del_t = 100 # secs

del_r_n = vr_n * del_t
del_theta_n = vt_n * del_t / r_n

r, theta = [r_n], [theta_n]
min_r, max_r = 10**10, 0
th_min, th_max = 0, 0

for i in range(1, 100000000):
    r_n1 = r_n + del_r_n
    theta_n1 = (theta_n + del_theta_n)
    del_r_n1 = del_r_n + (((r_n + (0.5 * del_r_n)) * (del_theta_n ** 2)) - (Kp * (del_t ** 2) / (r_n ** 2)))
    del_theta_n1 = (del_theta_n - ((2 * del_r_n * del_theta_n) / (r_n + 0.5 * del_r_n)))

    r.append(r_n1)
    theta.append(theta_n1)
    if min_r > r_n1:
        min_r = r_n1
        th_min = theta_n1
    elif max_r < r_n1:
        max_r = r_n1
        th_max = theta_n1
    
    r_n = r_n1
    theta_n = theta_n1
    del_r_n = del_r_n1
    del_theta_n = del_theta_n1

major_axis = min_r + max_r
foci_to_foci = major_axis - (2 * min_r)
ecc = foci_to_foci / major_axis
print("Ecc: ", ecc)


fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.plot([th_min, th_max], [min_r, max_r])
bro = [i % 6.28 for i in theta]
count = 0
for i in range(1, len(bro)):
    if bro[i-1] > bro[i]:
        print(count * del_t / (60 * 24)) #hours
        count = 0
    else:
        count += 1

# with open("dump.txt", "w") as f:
#     for i in bro:
#         f.write(str(i))
#         f.write("\n")
# # pprint(str(bro))
# plt.plot(bro)
plt.show()
