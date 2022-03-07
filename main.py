import numpy as np
import matplotlib.pyplot as plt
print('Hello World')
print("Xav suce!")

def calculate(E):
    h, c, e = 6.6260715 * 10 ** (-34), 2.99792458 * 10 ** 8, 1.60217662 * 10 ** (-19)
    return round(abs(h * c * 10 ** 9 / (E * e)), 2)


def plot_rays(arrow_d, group_d, max_x):
    val_y = [-13.6, -3.39, -1.51, -0.85, -0.54, -0.38, 0]
    val_y_ax = ['-13.6 eV (n=1)', '-3.39 eV (n=2)', '-1.51 eV (n=3)', '-0.85 eV (n=4)', '-0.54 eV (n=5)',
                '-0.38 eV (n=6)', '0 eV (n=∞)']
    for j, i in enumerate(val_y):
        plt.plot(np.linspace(0, max_x, max_x + 1), [i] * (max_x + 1), 'r-')
        if j == 5:
            plt.text(-25, i + 0.125, val_y_ax[j], fontsize='8')

            continue
        plt.text(-25, i, val_y_ax[j], fontsize='8')

    tracker = group_d
    liste_symb, liste_serie = ['α', 'β', 'γ'], ['Lyman', 'Balmer', 'Paschen', 'Brackett']
    for i in range(4):

        count = 0
        for j in range(i, len(val_y) - 1):
            var_E = val_y[i] - val_y[j + 1]
            note_A = "{lwave} nm ({energy} eV)".format(lwave=calculate(var_E), energy=round(var_E, 2))
            plt.arrow(tracker, val_y[j + 1], 0, var_E)
            plt.text(tracker - arrow_d / 3, (val_y[0] - val_y[len(val_y) - 1 - i]) / 2, note_A, rotation='vertical',
                     size='small')
            if count < 3:
                plt.text(tracker - 0.5, val_y[i] - 0.5, liste_symb[count])
                count += 1
            tracker += arrow_d
        plt.text(tracker - group_d + (i - 1) * 0.5, 0.5, liste_serie[i], size='large')
        tracker += group_d

    plt.axis('off')
    plt.ylabel("Énergie (eV)")
    plt.text(max_x / 2.5, -15, "Raies de l'atome d'hydrogène", size='large')
    plt.yticks([i - 1 for i in val_y], val_y_ax)

    plt.show()


plot_rays(3, 10, 100)

