import numpy as np
import scipy.linalg as la


class Semiconductor:
    def __init__(self, name,
                 energy_break, 
                 edge_of_valence_band, 
                 effective_mass_of_electron,
                 effective_mass_of_heavy_holes,
                 effective_mass_of_light_holes):
        self.name = name
        self.energy_break = energy_break
        self.edge_of_valence_band = edge_of_valence_band
        self.effective_mass_of_electron = effective_mass_of_electron
        self.effective_mass_of_heavy_holes = effective_mass_of_heavy_holes
        self.effective_mass_of_light_holes = effective_mass_of_light_holes

    def display(self) -> print():
        print("\n" + "name:" + str(self.name) + "\n" +
              "effective mass of heavy holes = " + str(self.energy_break) + "\n" +
              "edge of valence band = " + str(self.edge_of_valence_band) + "\n" +
              "effective mass of electron = " + str(self.effective_mass_of_electron) + "\n" +
              "effective mass of heavy holes = " + str(self.effective_mass_of_heavy_holes) + "\n" +
              "effective mass of light holes = " + str(self.effective_mass_of_light_holes) + "\n")


def load() -> list:
    x = []
    with open('structure.txt') as file:
        next(file)
        for line in file:
            x.append(line.strip().split())
    return x


def Ev(struct, z, semiconductor) -> float:
    if z < float(struct[0][-1]):
        for i in semiconductor:
            if struct[0][1] == str(i.name):
                return i.edge_of_valence_band
    elif z > float(struct[0][-1]) + float(struct[1][-1]):
        for i in semiconductor:
            if struct[2][1] == str(i.name):
                return i.edge_of_valence_band
    elif z > float(struct[0][-1]) or z < float(struct[0][-1]) + float(struct[1][-1]):
        for i in semiconductor:
            if struct[1][1] == str(i.name):
                return i.edge_of_valence_band


def Eg(struct, z, semiconductor) -> float:
    if z < float(struct[0][-1]):
        for i in semiconductor:
            if struct[0][1] == str(i.name):
                return i.energy_break
    elif z > float(struct[0][-1]) + float(struct[1][-1]):
        for i in semiconductor:
            if struct[2][1] == str(i.name):
                return i.energy_break
    elif z > float(struct[0][-1]) or z < float(struct[0][-1]) + float(struct[1][-1]):
        for i in semiconductor:
            if struct[1][1] == str(i.name):
                return i.energy_break


def mass_effective(struct, z, semiconductor) -> float:
    if z < float(struct[0][-1]):
        for i in semiconductor:
            if struct[0][1] == str(i.name):
                return i.effective_mass_of_electron
    elif z > float(struct[0][-1]) + float(struct[1][-1]):
        for i in semiconductor:
            if struct[2][1] == str(i.name):
                return i.effective_mass_of_electron
    elif z > float(struct[0][-1]) or z < float(struct[0][-1]) + float(struct[1][-1]):
        for i in semiconductor:
            if struct[1][1] == str(i.name):
                return i.effective_mass_of_electron


def Ec(struct, z, semiconductor):
    return Ev(struct, z, semiconductor) + Eg(struct, z, semiconductor)


def energy_level(structure, semiconductor) -> tuple:
    # siatka
    dz = 0.1  # odleglość między punktami siatki (jednostka: nm)
    zTot = 30.  # całkowita grubość structury (jednostka: nm)
    N = int(zTot / dz + 1)  # liczba węzłów siatki
    z = [i * dz for i in range(0, N)]  # położenia punktów siatki (jednostka: nm)

    # stałe fizyczne
    hb_eVs = 6.58211928156e-16  # stała Diraca (jednostka: eV*s)
    hb_Js = 1.0545717253e-34  # stała Diraca (jednostka: J*s)
    m0 = 9.10938291e-31  # masa swobodnego elektronu (jednostka: kg)

    # często stosowane wielkości
    hh2m = 0.5 * hb_eVs * hb_Js * 1e9 * 1e9 / m0  # (jednostka: eV*nm*nm, 10^9 jest po to by zamienić m na nm)
    dzdz1 = 1. / (dz * dz)  # 1/(dz*dz) (jednostka: 1/nm^2)

    # Budowanie macierzy
    # Macierz tworzymy w ten sposób, że po kolei rozpatrujemy węzły siatki
    # i saveujemy równania wynikające z postaci równania Schrodingera niezależnego od czasu.

    MACel = np.zeros((N, N))  # macierz dla elektronów (większość elementów będzie równa 0)

    for i in range(1, N + 1):
        Z = z[i - 1]  # położenie rozpatrywanego węzła (jednostka: nm)

        mel_LE = mass_effective(structure, Z - 0.5 * dz,
                                semiconductor)  # masa efektywna elektronu w materiale na lewo od rozpatrywanego węzła
        mel_RI = mass_effective(structure, Z + 0.5 * dz,
                                semiconductor)  # masa efektywna elektronu w materiale na prawo od rozpatrywanego węzła
        Ec_LE = Ec(structure, Z - 0.5 * dz,
                   semiconductor)  # krawędź pasma przewodnictwa w materiale na lewo od rozpatrywanego węzła
        Ec_RI = Ec(structure, Z + 0.5 * dz,
                   semiconductor)  # krawędź pasma przewodnictwa w materiale na prawo od rozpatrywanego węzła
        # uwaga: dla skrajnych węzłów sięgamy "nieco" poza structurę

        # dodatkowe oznaczenia
        a_LE = - hh2m / mel_LE
        a_RI = - hh2m / mel_RI
        b_CE = 0.5 * (Ec_LE + Ec_RI)  # krawędź pasma przewodnictwa w miejscu, gdzie znajduje się rozpatrywany węzeł

        # Poniższe równania były prawdopodobnie omawiane na zajęciach z metody różnic skończonych.

        if i > 1:
            MACel[i - 1][i - 2] = (a_LE * dzdz1)

        if 1:
            MACel[i - 1][i - 1] = (- a_LE * dzdz1 - a_RI * dzdz1 + b_CE)

        if i < N:
            MACel[i - 1][i] = (a_RI * dzdz1)

    # wyznaczanie wartości i vectorów własnych
    eigenvalues, eigenvectors = la.eig(MACel)

    return eigenvalues.real, eigenvectors


def data(value, vector, struct) -> tuple:
    eigenvalues = []
    eigenvectors = []
    for x, i in enumerate(value):
        if float(struct[0][-1]) < i < float(struct[0][-1]) + float(struct[1][-1]):
            eigenvalues.append(i)
            eigenvectors.append(vector[x])
    return eigenvalues, eigenvectors


def save(wart, vector):
    with open('wynik.txt', "w+") as file:
        for i, x in enumerate(wart):
            file.write("eigenvalues : " + str(x) + "\n" + "eigenvectors : " + str(vector[i]) + "\n\n")


def AlGaAs(data_params, pp):
    E_g = float(data_params[3]) * pp[1].energy_break + (1 - float(data_params[3])) * pp[0].energy_break - float(
        data_params[3]) * (
                 1 - float(data_params[3])) * (-0.127 + 1.310 * float(data_params[3]))
    E_v = float(data_params[3]) * pp[1].edge_of_valence_band + (1 - float(data_params[3])) * pp[0].edge_of_valence_band
    me = float(data_params[3]) * pp[1].effective_mass_of_electron + (1 - float(data_params[3])) * pp[
        0].effective_mass_of_electron
    mhh = float(data_params[3]) * pp[1].effective_mass_of_heavy_holes + (1 - float(data_params[3])) * pp[
        0].effective_mass_of_heavy_holes
    mlh = float(data_params[3]) * pp[1].effective_mass_of_light_holes + (1 - float(data_params[3])) * pp[
        0].effective_mass_of_light_holes
    pp.append(Semiconductor("AlGaAs", E_g, E_v, me, mhh, mlh))
