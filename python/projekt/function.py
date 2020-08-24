import numpy as np
import scipy.linalg as la


class Polprzewodnik:
    def __init__(self, nazwa, przerwa_energ, kraw_pasm_walenc, masa_efekt_elektron, masa_efekt_ciezkiej_dziury, masa_efekt_lekkiej_dziury):
        self.nazwa = nazwa
        self.przerwa_energ = przerwa_energ
        self.kraw_pasm_walenc = kraw_pasm_walenc
        self.masa_efekt_elektron = masa_efekt_elektron
        self.masa_efekt_ciezkiej_dziury = masa_efekt_ciezkiej_dziury
        self.masa_efekt_lekkiej_dziury = masa_efekt_lekkiej_dziury

    def wypisz(self):
        print("\n"+"nazwa:" + str(self.nazwa) + "\n" +
              "przerwa energetyczna = " + str(self.przerwa_energ)+"\n" +
              "krawedz pasma walencyjnego = " + str(self.kraw_pasm_walenc)+"\n" +
              "masa efektywna elektronu = " + str(self.masa_efekt_elektron)+"\n" +
              "masa efektywna ciezkiej dziury = " + str(self.masa_efekt_ciezkiej_dziury)+"\n" +
              "masa efekywna lekkiej dziury = " + str(self.masa_efekt_lekkiej_dziury)+"\n")


def wczytywanie():
    x = []
    with open('struktura.txt') as plik:
        next(plik)
        for linia in plik:
           x.append(linia.strip().split())
    return x


def Ev(strukt, z, polprzewodniki):
    if z < float(strukt[0][-1]):
        for i in polprzewodniki:
            if strukt[0][1] == str(i.nazwa):
                return i.kraw_pasm_walenc
    elif z > float(strukt[0][-1])+float(strukt[1][-1]):
        for i in polprzewodniki:
            if strukt[2][1] == str(i.nazwa):
                return i.kraw_pasm_walenc
    elif z > float(strukt[0][-1]) or z < float(strukt[0][-1])+float(strukt[1][-1]):
        for i in polprzewodniki:
            if strukt[1][1] == str(i.nazwa):
                return i.kraw_pasm_walenc


def Eg(strukt, z, polprzewodniki):
    if z < float(strukt[0][-1]):
        for i in polprzewodniki:
            if strukt[0][1] == str(i.nazwa):
                return i.przerwa_energ
    elif z > float(strukt[0][-1])+float(strukt[1][-1]):
        for i in polprzewodniki:
            if strukt[2][1] == str(i.nazwa):
                return i.przerwa_energ
    elif z > float(strukt[0][-1]) or z < float(strukt[0][-1])+float(strukt[1][-1]):
        for i in polprzewodniki:
            if strukt[1][1] == str(i.nazwa):
                return i.przerwa_energ


def masa_efekt(strukt, z, polprzewodniki):
    if z < float(strukt[0][-1]):
        for i in polprzewodniki:
            if strukt[0][1] == str(i.nazwa):
                return i.masa_efekt_elektron
    elif z > float(strukt[0][-1])+float(strukt[1][-1]):
        for i in polprzewodniki:
            if strukt[2][1] == str(i.nazwa):
                return i.masa_efekt_elektron
    elif z > float(strukt[0][-1]) or z < float(strukt[0][-1])+float(strukt[1][-1]):
        for i in polprzewodniki:
            if strukt[1][1] == str(i.nazwa):
                return i.masa_efekt_elektron


def Ec(strukt, z, polprzewodnik):
    return Ev(strukt, z, polprzewodnik) + Eg(strukt, z, polprzewodnik)


def poziom_energetyczny(struktura,polprzewodnik):
    # siatka
    dz = 0.1  # odleglość między punktami siatki (jednostka: nm)
    zTot = 30.  # całkowita grubość struktury (jednostka: nm)
    N = int(zTot / dz + 1)  # liczba węzłów siatki
    z = [i * dz for i in range(0, N)]  # położenia punktów siatki (jednostka: nm)

    # stałe fizyczne
    hb_eVs = 6.58211928156e-16  # stała Diraca (jednostka: eV*s)
    hb_Js = 1.0545717253e-34  # stała Diraca (jednostka: J*s)
    m0 = 9.10938291e-31  # masa swobodnego elektronu (jednostka: kg)

    # często stosowane wielkości
    hh2m = 0.5 * hb_eVs * hb_Js * 1e9 * 1e9 / m0  # hbar^2/(2*m0) (jednostka: eV*nm*nm, 10^9 jest po to by zamienić m na nm)
    dzdz1 = 1. / (dz * dz)  # 1/(dz*dz) (jednostka: 1/nm^2)

    # Budowanie macierzy
    # Macierz tworzymy w ten sposób, że po kolei rozpatrujemy węzły siatki
    # i zapisujemy równania wynikające z postaci równania Schrodingera niezależnego od czasu.

    MACel = np.zeros((N, N))  # macierz dla elektronów (większość elementów będzie równa 0)

    for i in range(1, N + 1):
        Z = z[i - 1]  # położenie rozpatrywanego węzła (jednostka: nm)

        mel_LE = masa_efekt(struktura, Z - 0.5 * dz, polprzewodnik)  # masa efektywna elektronu w materiale na lewo od rozpatrywanego węzła
        mel_RI = masa_efekt(struktura, Z + 0.5 * dz,polprzewodnik)  # masa efektywna elektronu w materiale na prawo od rozpatrywanego węzła
        Ec_LE = Ec(struktura, Z - 0.5 * dz, polprzewodnik)  # krawędź pasma przewodnictwa w materiale na lewo od rozpatrywanego węzła
        Ec_RI = Ec(struktura, Z + 0.5 * dz, polprzewodnik)  # krawędź pasma przewodnictwa w materiale na prawo od rozpatrywanego węzła
        # uwaga: dla skrajnych węzłów sięgamy "nieco" poza strukturę

        # dodatkowe oznaczenia
        a_LE = - hh2m / mel_LE
        a_RI = - hh2m / mel_RI
        b_CE = 0.5 * (Ec_LE + Ec_RI)  # krawędź pasma przewodnictwa w miejscu, gdzie znajduje się rozpatrywany węzeł

        # Poniższe równania były prawdopodobnie omawiane na zajęciach z metody różnic skończonych.

        if (i > 1):
            MACel[i - 1][i - 2] = (a_LE * dzdz1)

        if 1:
            MACel[i - 1][i - 1] = (- a_LE * dzdz1 - a_RI * dzdz1 + b_CE)

        if (i < N):
            MACel[i - 1][i] = (a_RI * dzdz1)

    # wyznaczanie wartości i wektorów własnych
    eigvals, eigvecs = la.eig(MACel)

    return eigvals.real, eigvecs


def dane(wartosc, wektor, strukt):
    wart_wlasne = []
    wekt_wlasne = []
    for x,i in enumerate(wartosc):
        if float(strukt[0][-1]) < i < float(strukt[0][-1])+float(strukt[1][-1]):
            wart_wlasne.append(i)
            wekt_wlasne.append(wektor[x])
    return wart_wlasne, wekt_wlasne


def zapis(wart, wekt):
    with open('wynik.txt', "w+") as plik:
        for i, x in enumerate(wart):
            plik.write("wartosc wlasna : " + str(x) + "\n"+ "wektor wlasny : " + str(wekt[i]) + "\n\n")









