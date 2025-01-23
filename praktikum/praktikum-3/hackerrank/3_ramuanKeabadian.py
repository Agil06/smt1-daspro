# Medium
'''
Dahulu kala di sebuah kota bernama Uruk, Gilgamesh sang raja Sumeria memiliki ketertarikan terhadap konsep keabadian. 
Sepeninggal sahabatnya Enkidu, obsesi ini menguat sehingga dipanggilah alchemist terhebat di Uruk untuk membuat sebuah ramuan keabadian.

Sang Alchemist menyanggupi hal tersebut dan meminta waktu 1 bulan untuk membuatnya. Sang raja manusia pun menunggu dengan sabar.

Pada dini hari ke 29, tepat sehari sebelum tenggat waktu, langit kota Uruk tiba-tiba bersinar terang. 
Dari atas cakrawala muncul cahaya terang yang jatuh seakan membelah langit. 
Cahaya itu tiba di suatu rumah dan menimbulkan ledakan dahsyat, menghancur leburkan rumah tersebut seisinya. 
Itu adalah rumah sang alchemist.

Ternyata para dewa tidak menyukai kegiatan sang alchemist ini. Bagi mereka manusia tidak berhak mendapatkan keabadian. 
Oleh karena itu dewa Ereshkigel mengarahkan anak panahnya ke rumah sang alchemist.
# -----------------------------------------------------------------------------------------------------------------------------------

Tetapi sang alchemist telah menuliskan suatu formula dengan bahan a, b, c, dan d yang selamat dari serangan misterius tersebut. 
Formula yang di temukan sebagai berikut:

-bahan a 30% dari total formula
-bahan b 30% dari total formula
-bahan c 15% dari total formula
-bahan d 25% dari total formula

juga terdapat catatan tambahan berupa:

" Wahai, jangan kau sama ratakan takaran tiap bahan. Niscaya beda lima saja itu petaka"
" Wahai, jangan kau campur sama rata. Karena jika sama, Utu sang dewa surya akan merasa hina"

Engkau adalah alchemist ke dua yang diberikan mandat membuat sebuah "larutan keabadian" dari formula di atas. 
Dari yang kau pahami, jika tiap bahan memiliki takaran sama, maka sesuatu buruk ("ledakan mungkin?") akan terjadi.

Oleh karena itu agar aman jika selisih antar bahan itu kurang atau sama dengan lima, akan mengembalikan pesan "hampir terjadi ledakan". 
Serta jika takaran ke-empat sama persis, akan mengembalikan "terjadi ledakan".

Engkau juga ingin mengetahui jika takaran bahan yang diberikan itu kurang. 
Apa bila terdapat dua atau lebih bahan yang kurang, bahan pertama saja yang dikembalikan nilainya 
(e.g bahan a dan b itu kurang, cukup mengembalikan "larutan a terlalu sedikit")

Input Format
    buatRamuan(a, b, c, d)

Constraints
    "0 <= a <= 100"

    "0 <= b <= 100"

    "0 <= c <= 100"

    "0 <= d <= 100"

Output Format
    me-return (bukan print) salah satu dari string berikut

    "larutan a terlalu sedikit"
    "larutan b terlalu sedikit"
    tergantung inputan parameter a, b, c, d

Sample Input 0
    buatRamuan(30, 30, 15, 25)

Sample Output 0
    ramuan berhasil di dapatkan

Sample Input 1
    buatRamuan(29, 30, 15, 25)

Sample Output 1
    larutan a terlalu sedikit

Sample Input 2
    buatRamuan(30, 30, 30, 26)

Sample Output 2
    hampir terjadi ledakan

Sample Input 3
    buatRamuan(28, 29, 15, 25)

Sample Output 3
    larutan a terlalu sedikit
'''



def buatRamuan(a, b, c, d):

    persenA = persen(a, a + b + c + d)
    persenB = persen(b, a + b + c + d)
    persenC = persen(c, a + b + c + d)
    persenD = persen(d, a + b + c + d)


    if persenA == 30 and persenB == 30 and persenC == 15 and persenD == 25:
        return "ramuan berhasil di dapatkan"
    elif persenA == persenB == persenC == persenD:
        return "terjadi ledakan"
    elif abs(persenA - persenB <= 5) and abs(persenA - persenC <= 5) and abs(persenA - persenD <= 5) and abs(persenB - persenC <= 5) and abs(persenB - persenD <= 5) and abs(persenC - persenD <= 5):
        return "hampir terjadi ledakan"
    else:
        if persenA < 30:
            return "larutan a terlalu sedikit"
        if persenB < 30:
            return "larutan b terlalu sedikit"
        if persenC < 15:
            return "larutan c terlalu sedikit"
        if persenD < 25:
            return "larutan d terlalu sedikit"

def persen(x, y):
    return (x / y) * 100

print(eval(input()))
    
print(buatRamuan(30, 30, 15, 25))
print(buatRamuan(29, 30, 15, 25))
print(buatRamuan(30, 30, 30, 26))
print(buatRamuan(28, 29, 15, 25))

#TESTCASE 6
buatRamuan(42, 42, 21, 35) #EXPECTED OUTPUT = ramuan berhasil di dapatkan
#TESTCASE 14
buatRamuan(6,6,3,5) #EXPECTED OUTPUT = ramuan berhasil di dapatkan

#TESCASE 15
buatRamuan(6,4,3,7)  #EXPECTED OUTPUT = hampir terjadi ledakan TESTCASE MASIH GAGAL.
