'''
Di Desa Kuno Isekai, pengembangan teknologi tidak hanya membantu di bidang pertanian, 
tapi juga dalam pengawasan lalu lintas udara. 
Bandara lokal Argosari baru saja memperkenalkan sistem pemantauan yang mampu menganalisis berbagai 
jenis pesawat terbang berdasarkan ketinggian, kecepatan, dan status bahan bakar. 
Sistem ini sangat penting untuk mencegah kecelakaan dan menjaga efisiensi operasional di bandara.

Tugas kamu adalah membuat sistem deteksi otomatis yang dapat 
memantau kondisi setiap pesawat dan memberikan status berdasarkan tiga parameter utama:

Ketinggian pesawat dalam satuan meter (m). x
Kecepatan pesawat dalam kilometer per jam (km/h). y
Status bahan bakar dalam persen (%). z

Sistem ini harus menganalisis data dan mengeluarkan status operasional pesawat berdasarkan kondisi berikut:

"Kecepatan Berbahaya": Jika kecepatan melebihi 900 km/h atau di bawah 200 km/h.
"Terlalu Tinggi": Jika ketinggian pesawat melebihi 12.000 meter.
"Bahan Bakar Rendah": Jika status bahan bakar kurang dari 20%. 
"Aman untuk Mendarat": Jika ketinggian kurang dari 5.000 meter, kecepatan antara 200 hingga 900 km/h, dan bahan bakar lebih dari 50%. "Berjalan Normal": Jika tidak ada kondisi di atas yang terpenuhi.

Input Format

monitor_pesawat(x,y,z)

Constraints

-

Output Format

"Kecepatan Berbahaya" 
"Terlalu Tinggi" 
"Bahan Bakar Rendah" 
"Aman untuk Mendarat" 
"Berjalan Normal"

Sample Input 0

monitor_pesawat(4000,850,55)
Sample Output 0

Aman untuk Mendarat
Explanation 0

Pesawat memiliki ketinggian kurang dari 5.000 meter, kecepatan dalam rentang yang aman, dan bahan bakar lebih dari 50%, sehingga pesawat "Aman untuk Mendarat".

Sample Input 1

monitor_pesawat(5000,950,70)
Sample Output 1

Kecepatan Berbahaya
Explanation 1

Kecepatan melebihi 900 km/h sehingga pesawat dalam kondisi "Kecepatan Berbahaya".
'''

'''
"Kecepatan Berbahaya": Jika kecepatan melebihi 900 km/h atau di bawah 200 km/h.
"Terlalu Tinggi": Jika ketinggian pesawat melebihi 12.000 meter.
"Bahan Bakar Rendah": Jika status bahan bakar kurang dari 20%. 
"Aman untuk Mendarat": Jika ketinggian kurang dari 5.000 meter, kecepatan antara 200 hingga 900 km/h, dan bahan bakar lebih dari 50%. 
"Berjalan Normal": Jika tidak ada kondisi di atas yang terpenuhi.

Ketinggian pesawat dalam satuan meter (m). x
Kecepatan pesawat dalam kilometer per jam (km/h). y
Status bahan bakar dalam persen (%). z
'''
def monitor_pesawat(x,y,z):
    if 900 < y < 200:
        return "Kecepatan Berbahaya"
    elif x > 12000:
        return "Terlalu Tinggi"
    elif z < 20:
        return "Bahan Bakar Rendah"
    elif x < 5000 and (200 <= y <= 900) and z > 50:
        return "Aman untuk Mendarat"
    else:
        return "Berjalan Normal"

"Kecepatan Berbahaya" 
"Terlalu Tinggi" 
"Bahan Bakar Rendah" 
"Aman untuk Mendarat" 
"Berjalan Normal"