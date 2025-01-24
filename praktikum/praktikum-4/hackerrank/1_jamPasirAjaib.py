'''
Di Desa Kuno di sebuah isekai, ada sebuah legenda tentang "Jam Pasir Ajaib" yang dapat menghitung waktu dengan sangat presisi. 
Jam Pasir ini memiliki kemampuan khusus: dapat menunjukkan waktu yang telah berlalu sejak titik awal waktu dalam bentuk jam, menit, dan detik secara akurat. 
Legenda menyebutkan bahwa hanya orang-orang yang bisa mengoperasikan Jam Pasir Ajaib dengan tepat yang bisa membuka pintu menuju Kuil Matahari, 
tempat peninggalan rahasia desa tersembunyi.

Suatu hari, seorang peneliti muda bernama Gege menemukan Jam Pasir tersebut, dan kini dia harus menentukan waktu yang tepat dengan format , di mana:

j menunjukkan jumlah jam dalam rentang 0 hingga 24 m menunjukkan jumlah menit dalam rentang 0 hingga 59.
s menunjukkan jumlah detik dalam rentang 0 hingga 59. 

Iza membutuhkan bantuan kamu untuk membuat program yang memvalidasi dan mencetak waktu dari format tersebut. 
Setiap input tuple harus mewakili waktu yang valid.

Buat sebuah program yang menerima sebuah tuple berisi tiga bilangan integer 𝑗, 𝑚, dan 𝑠, di mana:

𝑗 adalah bilangan integer yang mewakili jam, yang bernilai antara 0 hingga 24. 
𝑚 adalah bilangan integer yang mewakili menit, yang bernilai antara 0 hingga 59. 
𝑠 adalah bilangan integer yang mewakili detik, yang bernilai antara 0 hingga 59. 

Program harus menentukan apakah tuple tersebut merupakan waktu yang valid, dan jika valid, cetak waktu tersebut dalam format: "Jam: j, Menit: m, Detik: s".

Jika input tidak valid, program harus mencetak: "Waktu tidak valid".

Input Format
    jam(j,m,s)

Constraints
    (0 ≤ 𝑗 ≤ 24) (0 ≤ m ≤ 59) (0 ≤ 𝑠 ≤ 59)

Output Format
    "Jam: j, Menit: m, Detik: s"

Sample Input 0
    jam(12,30,45)

Sample Output 0
    Jam: 12, Menit: 30, Detik: 45

Explanation 0
    Waktu yang diberikan valid, yaitu 12 jam, 30 menit, dan 45 detik.

Sample Input 1
    jam(12,45,60)

Sample Output 1
    Waktu tidak valid

Explanation 1
    Detik tidak valid karena lebih dari 59. Waktu yang diberikan tidak valid
'''

def jam(j, m, s):
    if (0 <= j <= 24) and (0 <= m <= 59) and (0 <= s <= 59):
        return f"Jam: {j}, Menit: {m}, Detik: {s}"
    else:
        return "Waktu tidak valid"
    
print(eval(input()))