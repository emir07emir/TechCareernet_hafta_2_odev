#%% 1.soru - Sayi Analizi

sayi=int(input("sayi giriniz: "))
if(sayi < 0):
    if(sayi % 2 == 0):
        print("Negatif çift bir sayı girdiniz")
    if(sayi % 2 == 1):
        print("Negatif tek bir sayı girdiniz")

if(sayi > 0):
    if(sayi % 2 == 0):
        print("Pozitif çift bir sayı girdiniz")
    if(sayi % 2 == 1):
        print("Pozitif tek bir sayı girdiniz")


if(sayi == 0):
    print("girdiğiniz sayı 0 (sıfırdır)")

#%% 2.soru - Harf Frenkansi(String)
from collections import Counter

dictionary = {}
kelime = input("bir kelime giriniz: ")

#harf_sayilari=Counter(kelime)
#print(harf_sayilari)
for harf in kelime:
    if harf in dictionary:
        dictionary[harf] += 1
    else:
        dictionary[harf] = 1
print(dictionary)

#%% 3.soru - Sifre Kontrolu



sifre=input("Şifre oluşturunuz: ")



if(len(sifre) < 8):
    print("Şifreniz en az 8 karakterli olmalıdır")

elif(sifre.islower()):
    print("Şifreniz en az 1 büyük harf içermelidir")
    
elif not any(kontrol.isdigit() for kontrol in sifre):
    print("Şifreniz en az 1 rakam içermelidir")    

else:
    print("Tebrikler Şifre oluşturuldu")

#%% 4.soru - Liste İslemleri


liste=[12, 4, 9, 25, 30, 7, 18]
ort_buyuk_sayilar=[]

#ortalama bulma
toplam=0
for a in liste:
    toplam = toplam + a
    

ortalama = toplam/len(liste)
print(ortalama) 

# ortalamadan buyuk sayilari yeni listeye ekleme

for dongu in liste:
    if(dongu > 15):
        ort_buyuk_sayilar.append(dongu)

# listeyi ekrana yazdirma
print(ort_buyuk_sayilar)







#%% 5.soru Nested Loop(desen)
a = 0
for a in range(1,6):
    print("*"*a)
    







#%% 6.soru – While Döngüsü 

sayilar = []
while(True):
    sayi = int(input("Sayı giriniz(eğer sıfır cevabını verirseniz program sonlanır): "))
    
    if(sayi==0):
        print("program sonlandırılıyor...")
        break
    else:
        sayilar.append(sayi)
        
        
# toplam        
toplam_sayilar = sum(sayilar)

# ortalama

ortalama_sayilar = toplam_sayilar/len(sayilar)
         
print("girilen sayıların toplamı: ",toplam_sayilar)
print("Girilen sayıların ortalaması: ",ortalama_sayilar)        




#%% 7.soru - Palindrom Kontrolü

word = input("Herhangi bir kelime giriniz: ")

reverse_word = word[::-1]

if(word==reverse_word):
    print(word,"kelimesi Palindromdur")
else:
    print(word,"kelimesi Palindrom değildir")






#%% 8.soru - List Comprehension

mylist=[]

for i in range(1,101):
    if(i % 3 == 0 and i % 5 == 0):
        i=i**2
        mylist.append(i)
        
        
print(mylist)        
        








#%% 9.soru - String İslemleri

cumle = input("Bir adet cümle giriniz: ")

ayirilmis_cumle = cumle.split()

guncellenmis_cumle = " ".join(i.capitalize() for i in ayirilmis_cumle) # " " ile kelimeler arasi bosluk koyduk ve join ile string ifade olarak birlestirme yaptik

print(guncellenmis_cumle)




#%% Mini Proje Film Yorumu Analizi


film_yorum_liste = ["Film çok güzeldi", "Kötüydü", "Ortalama bir filmdi", "Gerçekten çok iyi!", "İyi ama daha iyi olabilirdi"]

#film_yorum = input("Leon the Professional filmi hakkındaki yorumunuzu giriniz: ")

#film_yorum_liste.append(film_yorum)


toplam_yorum_sayisi = len(film_yorum_liste)
iyi_gecen_yorum_sayisi = sum("iyi" in yorum.lower() for yorum in film_yorum_liste)
en_uzun_yorum = max(film_yorum_liste, key = len) 
en_kısa_yorum = min(film_yorum_liste, key = len)
ortalama_uzunluk = sum(len(yorum) for yorum in film_yorum_liste) / len(film_yorum_liste)



print("Toplam yorum sayısı: ",toplam_yorum_sayisi)
print('"iyi" geçen yorum sayısı: ',iyi_gecen_yorum_sayisi)
print("En uzun yorum: ",en_uzun_yorum)
print("En kısa yorum: ",en_kısa_yorum)
print("Ortalama uzunluk: kategori",ortalama_uzunluk)    







      