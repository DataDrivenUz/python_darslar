# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:38:37 2025
Mavzu: List(ro'yhatlar') va ular ustida amallar
@author: f.mamadiev
"""
#Biz avvalgi darslarimizda bitta o'zgaruvchiga bitta qiymat bergandik. O'zgaruvchiga bir nechta qiymatlar ham berish mumkun bo'nay ber nechta elementga ega o'zgarubchilar ro'yhat denm ataladi
#Ro'yhatlar adatda bir nechta elementga ega bo'lganligi uchun unga -lar qo'shimchasi qo'shiladi
#Uyida biz ber nechta ro'yhatlarni yaratib olamiz
#ro'yhat elementlari sonlar, matinlar yoki aralash elementlardan tashkil topishi mumkun

# sonlar = [2, 2, 5.6, 9]#Sonlar ro'yhati
# mevalar = ['olma', 'anor', 'anjir', 'nok']#Meveler ro'yhati
# mashinalar = ['Nexia', 'Laseti', 'Damas', 'Spark']#Mashinalar ro'yxati
# narxlar = [12000, 56000, 68000, 75000]#Narhlar ro'yhati
# aralash = ['meva', 'Faxridin', 1000, 'Kamaz', -153.24]#Aralash ro'yhat

#Yaratilgan ro'yxatlarni consolga chiqarib olamiz
# print(sonlar)
# print(mevalar)
# print(mashinalar)
# print(narxlar)
# print(aralash)

#Dasturlashda sanoq 0 dan boshlanganligi uchun biz sanashni 0 dan hisoblaymiz
#Royhat ichidahi biror elementni uning indeksi bilan chaqirishimiz mumkun
#print(mevalar[0])#Mevalar ro'yhatidagi birinchi elementni chiqaradi

#Bir nechta ro'yhatdagi elementlarni bigralikda chaqirsak ham bo'ladi
#Masalan
# print(mevalar[0], " ning narhi ", narxlar[0])
# print(mevalar[2], " ning  narhi ", narxlar[1])


#Bundan tashqari ro'yhatdagi elementlarna string metonladini ham qo'llashimiz mumkun
# print(mashinalar[0].upper())
# print(mevalar[3].title())

#Ro'yhat elementlari ustida amallar ham bajarishimiz mumkun
# print(narxlar[1]+narxlar[3] + 15000)

#Agar ro'yhatning oxiridagi elementga murojat qilmoqchi bo'lsak -1 dan oxiridan bitta oldingi elementga murojat qilmoqchi bo'lsan -2 dan foydalanamiz va hokazo
# print(mevalar[-1])
# print(aralash[-2])


#RO'YHATGA ELEMENT QO'SHISH OLIB TASHLASH VA BIROR ELEMENTNI O'ZGARTIRISH
#RO'YXATDAGI ELEMENTNI O'ZGARTIRISH
# narxlar = [12000, 56000, 68000, 75000]#Narhlar ro'yhati
# #Ro'yhatdagi elementlarni o'zgartirishimiz echibn shu elementning indeksi bo'yicha murojat qilamiz
# narxlar[0] = 15000#Narxlar ro'yxatidagi birinchi element 15000 ga o'zgartirilayapdi
# narxlar[1] = 60000#Narxlar ro'yxatidagi ikkinchi element 60000 ga o'zgartirilayapdi
# narxlar[3] = narxlar[3] + 20000#Narxlar ro'yxatidagi to'rtinchi element narxiga 20000 qo'shilayapdi
# print(narxlar)


#RO'YHATGA YANGI ELEMENT QO'SHISH
# mashinalar = ['BMW', "MERCEDES", "VOLVO"]#Inomarkalar ro'yhati
# mashinalar.append("MISTUBISHI")#append() metodi ro'yhatning oxiriga element qo'shadi
# print(mashinalar)

#Bosh ro'yxat yaratib olamiz va bo ro'yxatga append metodi yordamida bir nechta element qo'shamiz
# mevalar = []#Bo'sh ro'yxat yaratib oldik
# mevalar.append("Olma")#Mevalar nomli bo'sh ro'yhatimizga Olma elementini qo'shdik
# mevalar.append("Anor")#Ro'yhatga Anor elementini qo'shdik
# mevalar.append("Shaftoli")#Royhatga Shaftoli elementini qo'shdik
# print(mevalar)#Mevelar nomli ro'yhatimizni elon qildik


#Ro'yxatning istalgan qismiga element qo'shish uchun insert() metodidan foydalanamiz. Buning uchun qaysi tartibga element qo'shmoqchiligimizni va qanday element qo'shmoqchiligimizni ko'rsatishimiz kerak
#Masalan
# mashinalar = ['Nexia', 'Laseti', 'Damas', 'Spark']#Bizda mashinalar ro'yxati bor
# #Bu ro'yxatning ikkinchi elementi sifatida Matiz element qo'shamiz
# mashinalar.insert(1, "Matiz")
# #Ro'yxatning 3-elementiga Tracer ni qo'shamiz
# mashinalar.insert(2, "Tracer")
# #Yang elementlar qo'shilgan ro'yxatni elon qilamiz
# print(mashinalar)


#RO'YXATDAGI ELEMENTNI O'CHIRISH
#Ro'yxatdagi biror indeksli elementni o'chirish uchun del metodidan foydalanamiz
#Masalan
# ismlar = ["Faxriddin", "Xurshid", "Shaxlo", "Sarvinoz", "Safura", "Kumush", "Afruza", "Yasmina"]
#ismlar ro'yxatidagi bikkinchi elementni o'chiramiz
# del ismlar[1]
# print(ismlar)

#Agar ro'yxatimizdagi o'chirilishi kerak bo'lgan elementning indeksini bilmasak u elementni o'chirish uchun remove dan fordalanamiz
#ismlar ro'yxatidagi Kumush ismini olib tashlaymiz
# ismlar.remove("Kumush")
# print(ismlar)


#Agar ro'yxatimizdabitta elemetn bir necha matra takrorlangan bo'lsa remove metodi yordamida bu elementni o'chirganimizda faqat birinchi kelgani o'chadi
# ismlar = ["Faxriddin", "Xurshid", "Shaxlo", "Sarvinoz", "Safura", "Kumush", "Afruza", "Xurshid", "Yasmina"]
# #Ismlar ro'yxatida Xurshin ismi 2- va 8- tartibda takrorlangan remove yordamida bu elementni o'chirsak faqat 2- tartibda kelgani o'chadi
# ismlar.remove("Xurshid")
# print(ismlar)


#RO'YXAT ICHIDAN ELEMENTNI SUG'URIB OLISH
#Bozorlik ro'yxati berilgan bo'lsin
# bozorlik = ["Kartoshka", "Piyoz", "Olma", "Shakar", "Non", "Un"]
# #Ro'yhat ichidan shakarni sug'urib olib yangi elementga birlashtiramiz
# olingan = bozorlik.pop(3)
# print("Men ro'yxatdagi " + olingan + " mahsulotini oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# #Agar pop sug'urib olish metodi indeksiga son qo'ymasak oxiridagi elementni sug'urib oladi
# olingan = bozorlik.pop()
# print(olingan)
# print(bozorlik)


#AMALIYOT
#1-AMALIYOT
# dostlar = ["Sunnat", "Zafar", "Elmurod"]
# print("Salom ", dostlar[0], " bugun choyhonaga kelasizmi")
# print(dostlar[1], " bugun choyxonaga vaqtingiz bormi")
# print("Do'stlar ", dostlar[2], " bugun choyxonaga kela olmas ekan. Lenin ", dostlar[0], " kelemen dedi.\nLekin ", dostlar[1], " keldi")

#2-amaliyot
# sonlar = [1200, -5, 253.26, 100, -4500]
# print(sonlar[0]+sonlar[3])
# print(sonlar[1]*sonlar[2])
# print(sonlar[3]/sonlar[0])
# sonlar[0] = 500
# sonlar[2] = 1500
# sonlar[4] = sonlar[3] + 2000
# del sonlar[3] 
# print(sonlar)


#3-AMALIYOT
# t_shaslar = ["Amir Temur", "Imam Al Buhoriy", "Mirzo Ulug'bek", "Al Xorazmiy", "At-Termiziy"]
# z_shaxslar = ["Erkinjon Turdimiv", "Otabek Umarov", "Elon Mask", "Tramp"]
# print("Men tariziy shaxslardan ", t_shaslar.pop(1), " bilan,\nZamonaviy shaxslardan ", z_shaxslar.pop(-2), " bilan suhbatlashishni hohlar edim")


#4-AMALIYOT
# friends = []
# friends.append("Anvar")
# friends.append("Sobir")
# friends.append("Sarvar")
# friends.append("Umidjon")
# friends.append("Zafar")
# friends.append("Sherzod")
# friends.append("Farrux")
# friends.append("Saidjalol")
# print(friends)
# friends.insert(0, "Sodiqjon")
# friends.insert(4, "Sanjarbek")
# print(friends)
# print("Bazibga taklif qilinganlar ro'yxati ", friends, " dan iborat")
# friends.remove("Sobir")
# friends.remove("Zafar")
# print("Bazimga keladiganlar ro'yhati ", friends)


#5-AMALIYOT
# yangi_mehmonlar = []
# yangi_mehmonlar.append(friends.pop(0))
# yangi_mehmonlar.append(friends.pop(2))
# yangi_mehmonlar.append(friends.pop(4))
# yangi_mehmonlar.append(friends.pop(1))
# yangi_mehmonlar.append(friends.pop(3))
# print("Bazimga keladigan yangi mehmonlar: ", yangi_mehmonlar)

