# DIKTAT HALAMAN 19
# Medium
'''
Di tengah kerasnya petualangan di Antartika, Sandy, seorang petualang tangguh, tiba-tiba merasa bosan dengan dinginnya es dan salju. 
Untuk mengusir kebosanan, Sandy mengajukan tantangan menarik: "Coba buatkan aku sebuah fungsi yang bisa menghitung rata-rata dari angka-angka, 
tapi bukan sembarang rata-rata—aku ingin yang istimewa! 
Hitung rata-rata dari bilangan yang bukan yang terbesar dan bukan yang terkecil!"

Dengan semangat, kamu menciptakan fungsi MO(a, b, c, d), 
sebuah formula ajaib yang secara cerdik memilih dua bilangan di antara empat angka yang diberikan, 
mengabaikan yang paling besar dan yang paling kecil. 
Hasilnya? Sandy pun terkesima melihat angka yang muncul, 
sebuah rata-rata yang sempurna untuk menemani petualangan berikutnya di tengah daratan es yang tak kenal ampun!

<<<
Misal diberikan empat masukan, maka 2 integer terbesar dan terkecil dihilangkan, kemudian sum dari dua integer yang tersisa dibagi 2.
>>>

'''

'''
Input Format
    MO(a,b,c,d)

Constraints
    -100 ≤ a,b,c,d ≤ 100

Output Format
    x

Sample Input 0
    MO(3,5,4,2)

Sample Output 0
    3.5

Sample Input 1
    MO(2,2,2,2)

Sample Output 1
    2.0
'''

#REALISASI
def max2(a, b):
    return ((a + b + abs(a - b)) / 2)

def min2(a, b):
    return ((a + b - abs(a - b)) / 2)

def max4(i, j, k, l):
    return max2(max2(i, j), max2(k, l))

def min4(i, j, k, l):
    return min2(max2(i, j), min2(k, l))

def MO(a, b, c, d):
    return ((a + b + c + d) - min(a, b, c, d) - max(a, b, c, d)) / 2
    
# APLIKASI SAMPLE INPUT
print(MO(3,5,4,2))
print(MO(2,2,2,2))
