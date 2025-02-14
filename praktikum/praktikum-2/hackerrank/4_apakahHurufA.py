# DIKTAT HALAMAN 20
# Medium
'''
Maxwell, dengan keunikannya yang aneh namun menawan, memiliki kegemaran yang sangat spesifik terhadap huruf 'a'. 
Tak ada karakter lain yang mampu menarik perhatiannya seperti 'a' — tidak 'y', apalagi simbol aneh seperti '@'. 
Karena itu, dia menantangmu untuk membuat sebuah fungsi yang bisa membedakan antara 'a' dan semua karakter lainnya.

Tanpa ragu, kamu menciptakan fungsi is_an_a(c), yang bertugas memastikan apakah karakter yang diberikan adalah sang primadona, yaitu 'a'. 
Jika karakter tersebut adalah 'a', maka Maxwell akan bersorak gembira; namun, jika bukan, Maxwell akan tahu bahwa itu bukanlah favoritnya!

Input Format
    is_an_a(c)

Constraints
    |c| = 1

Output Format
    True / False

Sample Input 0
    is_an_a('a')

Sample Output 0
    True

Sample Input 1
    is_an_a('@')

Sample Output 1
    False
'''

#REALISASI
def is_an_a(c):
    return c == 'a'

# APLIKASI SAMPLE INPUT
print(is_an_a('a'))
print(is_an_a('@'))