# Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# ======================
# VARIABEL
# ======================
suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan')
kipas = ctrl.Consequent(np.arange(0, 101, 1), 'kipas')

# ======================
# HIMPUNAN FUZZY
# ======================

# Suhu
suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['normal'] = fuzz.trimf(suhu.universe, [15, 25, 35])
suhu['panas'] = fuzz.trimf(suhu.universe, [30, 40, 40])

# Kelembapan
kelembapan['kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 50])
kelembapan['sedang'] = fuzz.trimf(kelembapan.universe, [25, 50, 75])
kelembapan['lembab'] = fuzz.trimf(kelembapan.universe, [50, 100, 100])

# Kecepatan kipas
kipas['lambat'] = fuzz.trimf(kipas.universe, [0, 0, 50])
kipas['sedang'] = fuzz.trimf(kipas.universe, [25, 50, 75])
kipas['cepat'] = fuzz.trimf(kipas.universe, [50, 100, 100])

# ======================
# ATURAN FUZZY
# ======================
rule1 = ctrl.Rule(suhu['dingin'] & kelembapan['kering'], kipas['lambat'])
rule2 = ctrl.Rule(suhu['normal'] & kelembapan['sedang'], kipas['sedang'])
rule3 = ctrl.Rule(suhu['panas'] | kelembapan['lembab'], kipas['cepat'])
rule4 = ctrl.Rule(suhu['panas'] & kelembapan['kering'], kipas['cepat'])
rule5 = ctrl.Rule(suhu['dingin'] & kelembapan['lembab'], kipas['sedang'])

# ======================
# SISTEM
# ======================
kipas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
kipas_simulasi = ctrl.ControlSystemSimulation(kipas_ctrl)

# ======================
# INPUT (bisa kamu ubah)
# ======================
kipas_simulasi.input['suhu'] = 30
kipas_simulasi.input['kelembapan'] = 70

# ======================
# PROSES
# ======================
kipas_simulasi.compute()

# ======================
# OUTPUT
# ======================
print("Kecepatan kipas:", kipas_simulasi.output['kipas'])

# ======================
# VISUALISASI
# ======================
suhu.view()
kelembapan.view()
kipas.view(sim=kipas_simulasi)

# Biar tidak langsung tertutup
plt.show()
input("Tekan ENTER untuk keluar...")