from math import *
'''
Lara sedang memperhatikan seekor semut yang berada di titik sudut sebuah balok berukuran x×y×z 
yang baru saja dibuat dengan bahan kertas. 
Semut tersebut sepertinya akan bergerak mendekati sebuah kotoran gula yang 
kebetulan berada di ujung titik sudut berlawanan dari si semut 
(Dapat kamu diasumsikan bahwa semut berada di (0,0,0) dan gula berada di (x,y,z) dalam bidang kartesius).
Lara penasaran akan jalan mana yang semut pilih agar semut tersebut sampai ke gula melalui jalan tercepat. 
Kamu perlu membantu Lara dalam menemukan jarak jalan tercepat tersebut!

Input Format
    jalanSemut(x,y,z)

Constraints
    1 ≤ x,y,z ≤ 10000

Output Format
    Bilangan real yang menyatakan jarak terpendek si semut. (Gunakan round([float], 3)
    untuk membulatkan hasil ke 3 angka desimal)

Sample Input 0
    jalanSemut(3,4,5)

Sample Output 0
    8.602

Sample Input 1
    jalanSemut(1,2,7)

Sample Output 1
    7.616
'''

def fx2(x):
    return x * x

def dif2(x, y):
    return fx2(x + y)

def min2(a, b):
    return ((a + b - abs(a - b)) / 2)

def jalanSemut(x, y, z):
    return round((min2
                     (min2(sqrt(fx2(x + y) + fx2(z)), 
                           sqrt(fx2(x + z) + fx2(y))), 
                        
                     sqrt(fx2(y + z) + fx2(x))))
                 , 3)

'''
Menggunakan variabel
    a = sqrt(fx2(x + y) + fx2(z))
    b = sqrt(fx2(x + z) + fx2(y))
    c = sqrt(fx2(y + z) + fx2(x))
    
    return round((min2(min2(a, b), c)), 3)
'''

#APLIKASI
print(jalanSemut(20, 12, 3))
