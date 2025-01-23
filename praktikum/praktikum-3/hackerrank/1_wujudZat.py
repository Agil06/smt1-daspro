# Easy
'''
Buatlah program fungsional yang 
menerima masukan suatu besaran yang menyatakan temperatur air dalam derajat Celcius dan pda tekanan 1 atm. 
Fungsi tersebut akan mengembalikan nilai keadaan dari zat air tersebut, apakah es, cair, atau uap.

Input Format
    Sebuah bilangan T yang menyatakan 
    temperatur air dalam satuan derajat Celcius dan 
    menjadi parameter formal fungsi wujudZat(T).

Constraints
    -1000 <= T <= 1000

Output Format
    Sebuah string yang kemungkinan outputnya adalah sebagai berikut.

    es
    cair
    uap

Sample Input 0
    wujudZat(0.0)

Sample Output 0
    es

Sample Input 1
    wujudZat(10.0)

Sample Output 1
    cair

Sample Input 2
    wujudZat(273.4)

Sample Output 2
    uap
'''

def wujudZat(T):
    if T <= 0:
        return "es"
    elif 0 < T < 100:
        return "cair"
    else:
        return "uap"
    
print(wujudZat(0.0))
print(wujudZat(10.0))
print(wujudZat(273.4))