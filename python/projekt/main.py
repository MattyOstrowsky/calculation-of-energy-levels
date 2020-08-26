from function import *


struktura = wczytywanie()

polprzewodniki = [Polprzewodnik("GaAs", 1.422, -0.8, 0.067, 0.327, 0.090),
                  Polprzewodnik("AlAs", 3.003, -1.330, 0.124, 0.510, 0.180)]

for i in struktura:
    if i[1] == 'AlGaAs':
        AlGaAs(i, polprzewodniki)

polprzewodniki[0].wypisz()
polprzewodniki[1].wypisz()
polprzewodniki[2].wypisz()

m_wartosc, m_wektor = poziom_energetyczny(struktura, polprzewodniki)
wartosci_wlasne, wektory_wlasne = dane(m_wartosc, m_wektor, struktura)
zapis(wartosci_wlasne,wektory_wlasne)
