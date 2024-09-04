import matplotlib.pyplot as plt
from yaml import safe_load


def calculate_oribit(sat):
    G = sat['G']
    Mp = sat['Mp']

    Kp = G * Mp

    r_n = sat['r_n']
    theta_n = sat['theta_n']

    vr_n = sat['v_r']
    vt_n = sat['v_theta']
    del_t = sat['del_t']

    del_r_n = vr_n * del_t
    del_theta_n = vt_n * del_t / r_n

    r, theta = [r_n], [theta_n]
    min_r, max_r = 10**10, 0
    th_min, th_max = 0, 0

    stop_iter = sat['stop_iter']

    for i in range(1, stop_iter):
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
    period_scaler = sat['period_scaler']
    for i in range(1, len(bro)):
        if bro[i-1] > bro[i]:
            print(count * del_t / period_scaler)
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


with open('data.yaml', 'r') as file:
    params = safe_load(file)

for sat in params:
    calculate_oribit(params[sat])