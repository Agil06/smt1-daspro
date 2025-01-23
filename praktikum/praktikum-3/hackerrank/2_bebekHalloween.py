# Medium
'''
Ketika Halloween, Pak Dengklek menyiapkan sejumlah N permen untuk dibagikan kepada bebek-bebeknya di kandang. 
Banyaknya bebek Pak Dengklek ialah B ekor. Bebek akan marah jika banyaknya permen lebih sedikit daripada banyaknya bebek 
karena pasti ada bebek yang tidak mendapatkan permen satu pun. 
Sebaliknya, bebek akan gembira ketika Pak Dengklek memberikan permennya sama rata. 
Selain itu, Pak Dengklek akan bingung saat permennya justru mempunyai sisa. Entah harus diberi ke siapa sisa permen tersebut.

Pak Dengklek meminta bantuanmu untuk menentukan apakah bebek-bebeknya "marah" atau "gembira". 
Tidak lupa pula, berikan informasi apakah Pak Dengklek akan "bingung" atau "tidak bingung".

Input Format
    BebekHalloween(N, B)

    Sebuah fungsi BebekHalloween dengan masukan N dan B yang mana N adalah sejumlah permen yang dimiliki Pak Dengklek dan B adalah banyaknya bebek.

Constraints
    0 <= N <= 1000
    1 <= B <= 1000

Output Format
    Keluarkan "bebek marah", "bebek gembira dan Pak Dengklek tidak bingung", atau "bebek gembira tetapi Pak Dengklek bingung" sesuai dengan kondisi yang memenuhi.

Sample Input 0
    BebekHalloween(0, 3)

Sample Output 0
    bebek marah

Explanation 0
    Banyaknya bebek lebih banyak daripada permen sehingga pasti ada bebek yang tidak mendapatkan permen sehingga bebek marah.

Sample Input 1
    BebekHalloween(24, 7)

Sample Output 1
    bebek gembira tetapi Pak Dengklek bingung

Explanation 1
    Banyaknya permen lebih banyak dari banyaknya bebek, tetapi permen akan bersisa.

Sample Input 2
    BebekHalloween(70, 7)

Sample Output 2
    bebek gembira dan Pak Dengklek tidak bingung

Explanation 2
    Banyaknya permen dapat dibagikan hingga habis dan tiap bebek mendapatkan jumlah permen yang sama rata.
'''
def BebekHalloween(N, B):
    if N < B:
        return "bebek marah"
    elif N % B == 0:
        return "bebek gembira dan Pak Dengklek tidak bingung"
    else:
        return "bebek gembira tetapi Pak Dengklek bingung"

print(BebekHalloween(0, 3))
print(BebekHalloween(24, 7))
print(BebekHalloween(70, 7))