# Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Menyiapkan himpunan fuzzy
biaya = ctrl.Antecedent(np.arange(0, 1001, 1), 'biaya')
permintaan = ctrl.Antecedent(np.arange(0, 61, 1), 'permintaan')
produksi = ctrl.Consequent(np.arange(0, 101, 1), 'produksi')

# Biaya produksi
biaya['Rendah'] = fuzz.zmf(biaya.universe, 0, 500)
biaya['Standar'] = fuzz.pimf(biaya.universe, 0, 500, 500, 1000)
biaya['Tinggi'] = fuzz.smf(biaya.universe, 500, 1000)

# Permintaan
permintaan['Turun'] = fuzz.trapmf(permintaan.universe, [0, 0, 10, 30])
permintaan['Biasa'] = fuzz.trimf(permintaan.universe, [10, 30, 50])
permintaan['Naik'] = fuzz.trapmf(permintaan.universe, [30, 50, 60, 60])

# Produksi barang
produksi['Berkurang'] = fuzz.trapmf(produksi.universe, [0, 0, 10, 50])
produksi['Normal'] = fuzz.trimf(produksi.universe, [30, 50, 70])
produksi['Bertambah'] = fuzz.trapmf(produksi.universe, [50, 90, 100, 100])

# Aturan fuzzy
aturan1 = ctrl.Rule(biaya['Rendah'] & permintaan['Naik'], produksi['Bertambah'])
aturan2 = ctrl.Rule(biaya['Standar'], produksi['Normal'])
aturan3 = ctrl.Rule(biaya['Tinggi'] & permintaan['Turun'], produksi['Berkurang'])

# Sistem kontrol
engine = ctrl.ControlSystem([aturan1, aturan2, aturan3])
system = ctrl.ControlSystemSimulation(engine)

# Input
system.input['biaya'] = 500
system.input['permintaan'] = 30

# Proses
system.compute()

# Output
print("Jumlah produksi:", system.output['produksi'])

# Visualisasi
produksi.view(sim=system)

import matplotlib.pyplot as plt
plt.show()