from math import *
# Medium
'''
Xaviera, seorang petualang yang suka menjelajah peta dan mengukur jarak antara tempat-tempat yang ia temukan, memberimu sebuah tantangan menarik. 
Dia memberikan dua titik koordinat pada bidang kartesius, (x1, y1) dan (x2, y2), 
dan memintamu untuk menghitung jarak antara kedua titik tersebut. 
Jarak ini akan membantunya menentukan seberapa jauh ia harus melangkah menuju petualangan berikutnya.

Dengan semangat, kamu menciptakan fungsi least_square(x1, y1, x2, y2), 
yang menggunakan formula ajaib dari geometri, yaitu rumus jarak Euclidean. 
Fungsi ini akan menghitung jarak terpendek antara kedua titik tersebut di bidang kartesius, 
memberi Xaviera informasi yang ia butuhkan untuk melanjutkan perjalanannya. 
Dengan setiap langkah yang ia ambil, Xaviera akan tahu pasti seberapa jauh ia telah berjalan, berkat perhitungan jarak yang kamu lakukan!


<<<
...Dia memberikan dua titik koordinat pada bidang kartesius, (x1, y1) dan (x2, y2)...
...memintamu untuk menghitung jarak antara kedua titik tersebut...
...fungsi least_square(x1, y1, x2, y2), yang menggunakan formula ajaib dari geometri, yaitu rumus jarak Euclidean...
>>>

Input Format
    least_square(x1,y1,x2,y2)

Constraint
    -100 ≤ x1, y1, x2, y2 ≤ 100

Output Format
    x

Sample Input 0
    least_square(0,0,3,4)

Sample Output 0
    5.0 

Sample Input 1
    least_square(1, 2, 4, 6)

Sample Output 1
    5.0 
'''

#RUMUS MATEMATIS DARI JARAK DUA TITIK MENGGUNAKAN RUMUS EUCLIDEAN
# sqrt((x2-x1)^2 + (y2-y1)^2)

#REALISASI
#FUNGSI ANTARA
def fx2(x):
    return x * x

def dif2(x, y):
    return fx2(x - y)

#FUNGSI UTAMA
def least_square(x1, y1, x2, y2):
    return sqrt(dif2(y2, y1) + dif2(x2, x1))