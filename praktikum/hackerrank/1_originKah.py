# DIKTAT HALAMAN 21
# Easy
'''
Bayangkan kamu terlempar ke dunia isekai yang ajaib, 
di mana segala sesuatu bisa direpresentasikan pada bidang kartesius dua dimensi. 
Di dunia ini, kamu selalu tahu di mana posisimu berada dengan tepat, lengkap dengan koordinatnya. 
Suatu hari, kamu penasaran apakah kamu berada di titik awal dari semua petualangan ini, yaitu titik pusat (0,0). 
Dengan semangat petualang sejati, kamu pun menciptakan sebuah fungsi bernama is_origin(x, y),
yang akan dengan mudah memberitahumu apakah kamu sedang berdiri di titik nol dari dunia isekai ini, 
atau apakah kamu masih harus menjelajah lebih jauh lagi!

<<<
fungsi bernama is_origin(x, y), yang akan dengan mudah memberitahumu apakah kamu sedang berdiri di titik nol
>>>

Input Format
    is_origin(x,y)

Constraints
    -100 ≤ x, y ≤ 100

Output Format
    True atau False

Sample Input 0
    is_origin(0,0)

Sample Output 0
    True

Sample Input 1
    is_origin(1,1)

Sample Output 1
    False
'''

#REALISASI
def is_origin(x, y):
    return x == 0 and y == 0

# APLIKASI SAMPLE INPUT
print(is_origin(0,0))
print(is_origin(1,1))
