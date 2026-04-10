📘 Sistem Fuzzy Logic dengan Python

Proyek ini berisi implementasi Logika Fuzzy menggunakan library scikit-fuzzy di Python. Terdapat tiga studi kasus yang berbeda, yaitu:

Sistem kontrol kecepatan kipas
Sistem penentuan jumlah produksi
Sistem penilaian restoran
🧠 Konsep Dasar

Logika fuzzy adalah metode yang digunakan untuk menangani ketidakpastian dengan menggunakan nilai keanggotaan (membership function), tidak hanya benar atau salah (0 atau 1), tetapi bisa berada di antara keduanya.

Tahapan dalam sistem fuzzy:

Fuzzifikasi (mengubah input menjadi nilai fuzzy)
Inferensi (menggunakan aturan)
Defuzzifikasi (menghasilkan output pasti)
⚙️ Library yang Digunakan

Pastikan sudah menginstall library berikut:

pip install numpy scikit-fuzzy matplotlib
📂 Struktur File
kipas.py → Sistem kontrol kecepatan kipas
produksi.py → Sistem penentuan jumlah produksi
restoran.py → Sistem penilaian restoran
🌬️ 1. Sistem Kipas (kipas.py)
Input:
Suhu (0–40 °C)
Kelembapan (0–100%)
Output:
Kecepatan kipas (0–100)
Aturan Contoh:
Jika suhu panas atau kelembapan lembab → kipas cepat
Jika suhu dingin dan kelembapan kering → kipas lambat
Tujuan:

Menentukan kecepatan kipas secara otomatis berdasarkan kondisi lingkungan.

🏭 2. Sistem Produksi (produksi.py)
Input:
Biaya produksi (0–1000)
Permintaan (0–60)
Output:
Jumlah produksi (0–100)
Aturan Contoh:
Jika biaya rendah dan permintaan naik → produksi bertambah
Jika biaya tinggi dan permintaan turun → produksi berkurang
Tujuan:

Membantu pengambilan keputusan dalam jumlah produksi.

🍽️ 3. Sistem Penilaian Restoran (restoran.py)
Input:
Kualitas makanan (0–10)
Pelayanan (0–10)
Output:
Nilai restoran (0–10)
Aturan Contoh:
Jika makanan enak atau pelayanan ramah → nilai baik
Jika makanan tidak enak dan pelayanan ketus → nilai buruk
Tujuan:

Menentukan kualitas restoran berdasarkan pengalaman pelanggan.

▶️ Cara Menjalankan

Jalankan salah satu file Python:

python kipas.py
python produksi.py
python restoran.py
📊 Output

Setiap program akan menghasilkan:

Nilai output (print di terminal)
Grafik fuzzy (matplotlib)
📝 Catatan
Nilai input dapat diubah langsung pada bagian:
system.input['variabel'] = nilai
Grafik akan muncul sebagai visualisasi fungsi keanggotaan.
🎯 Kesimpulan

Proyek ini menunjukkan bagaimana logika fuzzy dapat digunakan dalam:

Sistem kontrol (kipas)
Pengambilan keputusan (produksi)
Evaluasi kualitas (restoran)
