from function import load, Semiconductor, AlGaAs, energy_level, data, save

structure = load()

semiconductor = [Semiconductor("GaAs", 1.422, -0.8, 0.067, 0.327, 0.090),
                 Semiconductor("AlAs", 3.003, -1.330, 0.124, 0.510, 0.180)]

for i in structure:
    if i[1] == 'AlGaAs':
        AlGaAs(i, semiconductor)

semiconductor[0].display()
semiconductor[1].display()
semiconductor[2].display()

m_values, m_vector = energy_level(structure, semiconductor)
eigenvalues, eigenvectors = data(m_values, m_vector, structure)
save(eigenvalues, eigenvectors)
