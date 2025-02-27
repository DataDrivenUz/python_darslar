# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 08:40:27 2025

MAVZU: Ro'yhatlar bilan ishlash. O'zgarmas ro'yhatlar(Tuples)'

@author: f.mamadiev
"""

#RO'YHATLARNI TARTIBLASH
#Listlar bilan ishlaganimizda ularni tartiblashimiz mumkun. Alfabet tartibida, teskari alfabet tartibida o'sish kamayish va boshqa tartiblarda tartiblash mumkun
#Masalan
# mashinalar = ['bmw', 'mercedes', 'audi', 'mistubishi', 'nissan', 'volvo', 'toyota', 'rolsroys']
# #Bu ro'yhatni alfabet tartibida tartiblaymiz
# mashinalar.sort()
# print(mashinalar)
# #Teskari alfabet tartibida tartiblaymiz
# mashinalar.sort(reverse=True)
# print(mashinalar)

#Tartiblashda katta harflar bilan berilgan element har doim birinchi keladi so'ngra qolgan elementlar alfabet tarzida tartiblanadi
# mashinalar = ['bmw', 'Mercedes', 'audi', 'mistubishi', 'nissan', 'volvo', 'toyota', 'rolsroys']
# mashinalar.sort()
# print(mashinalar)#Birinchi Mercedes elementi birinchi keladi va qolgan elementlar undan keyin tartiblanadi


#Bazidaasl yo'yhatni o'zgartirmagan holda ro'yhatni tartiblash kerak bo'ladi bu holatda sorted() funksiyasinad foydalanamiz
# Masalan
# mehmonlar = ['Ahmat', 'Shermat', 'Akmal', 'Jobir', 'Valijon', 'Gulmurod', 'Zokirjon']
# print('Asl ro\'yhat: ', mehmonlar)
# #Asl ro'yhatni o'zgartirmagan holda tartiblayapmiz
# print('sorted() bilan tartiblangan ro\'yhat: ', sorted(mehmonlar))
# #Asl ro'yhatni o'zgartirmagan holda teskari tartibda tartiblayapmiz
# print('sorted() orqali teskari tarriblangan ro\'hat: ', sorted(mehmonlar, reverse=True))


#RO'YHATLARNI AYLANTIRISH
#Bazida berilgan ro'yhatlarni aylantirishga to'g'ri kelishi mumkun. Bunday holatlarda reverse() funksiyasidan foydalanamiz
#Masalan
# mehmonlar = ['Ahmat', 'Shermat', 'Akmal', 'Jobir', 'Valijon', 'Gulmurod', 'Zokirjon']
#Asl ro'yhatni elon qilish
# print(mehmonlar)
#Aylantirilgan ro'yhatni elon qilish
# mehmonlar.reverse()
# print(mehmonlar)
 

#RO'YHAT UZUNLIGI(ELEMENTLAR SONI)
#Ro'yhat uzunligini aniqlash uchun len(ro'yhat) funksiyasidan foydalanamiz
# mevala = ["olma", "anjir", "shaftoli", "uzum", "kartoshka"]
#Ro'yhat uzunligini elon qilamiz
# print("Mevalar nomli ro'yhatning ", len(mevala), " ta elementi bor")


#range() funksiyasi. Bu funksiya orqali biror bir oralig'dagi ketma-ketlik tuzib olishimiz mumkun va bu ketmaketlikni list() funksiyasi orqali ro'yhat yaratib olamiz
#Masalan
# sonlar = list(range(0, 30))#0 dan 29 gacha bo'lgan sonlar ketma ketligini hosil qiladi va bu ketma ketlikdan 
# print(sonlar)


#Range funktsiyasi yordamida elementlari biror qadamga farq qiladigan ro'yhatlarni ham yaratish mumkun
#Masalan
#0 dan 19 gacha bo'lgan 2 qadamli sonlar ro'yhatini tuzib beradi
# sonlar = list(range(0, 20, 2))
#ro'yhatni elon qiladi
# print(sonlar)


#0 dan 30 gacha bo'lgan juft va toq sonlar ro'yhatini tuzib olaylik
#0 dan 30 gacha juft sonlar ro'yhati
# juft_sonlar = list(range(0, 30, 2))
#1 dan 30 gacha toq sonlar ro'yhati
# toq_sonlar = list(range(1, 30, 2))
# print("0 dan 29 gacha juft sonlar ro'yhati: ", juft_sonlar)
# print("0 dan 29 gacha toq sonlar ro'yhati: ",  toq_sonlar)


#SONLI FUNKTSIYALAR USTIDA AMALLAR
#Narxlar ro'yhati berilgan bo'lsin
# narxlar = [26000, 236400, 45900, 468000, 78900, 459700]
#Eng arzon rarhni ekranga chiqaradi
# print("Eng qimmat narh: ", min(narxlar))
#Eng qimmat rarhni ekranga chiqaradi
# print("Eng qimmat narh: ", max(narxlar))
#narhlar yig'indisini chiqaradi
# print("Jami narh: ", sum(narxlar))

#Ro'yhatlarni kesish
#Bazi hollarda biror ro'yhatning ma'lum bir qismini kesib olish talab qilinishi mumkun
#Bunday hollarda Quyidagi usuldan foydalanamiz
# mehmonlar = ['Ahmat', 'Shermat', 'Akmal', 'Jobir', 'Valijon', 'Gulmurod', 'Zokirjon']
#Bu ro'yhatdan 1-3 gacha elementlarni kesib olamiz
# kelgan_mehmonlar = mehmonlar[0:3]
#Mehmonlar ro'yhatini elon qiladi
# print(mehmonlar)
#0 dan 3 gacha kesib olingan ro'yhatni elon qiladi
# print(kelgan_mehmonlar)
#ro'yhatning boshidan 4 elementnacha kesib olib elon qiladi
# print(mehmonlar[:4])
#Mehmonlar ro'yhatidagi ikkinchi indeksdan ro'yhatning oxirigacha kesib olib elon qiladi
# print(mehmonlar[1:])
#Mehmonlar ro'yhatini to'liq kesib olib elon qiladi
# print(mehmonlar[:])


#O'ZGARMAS RO'YHATLAR
#bIZ O'ZGARMAS RO'YHATLARNI QUYIDAGI KO'RINISHDA YASAB OLISHIMIZ MUMKUN
# sonlar = (1, 2, 4, 20, 32)
# #Bu ro'yhatga o'zgarmas ro'yhat bo'lganligi uchun hechqanaqa o'zgarish kirita olmaymiz. Agar o'zgarish kiritib elon qiladigan bo'lsan hatolik beradi
# # print(sonlar.pop[2])
# #sonlar elementidan 3-elementno olmoqchi edik konsolga hatolik chiqdi

# #tuples ya'ni o'zgarmas ro'yhatlarni o'zgartirishimiz uchun list funksiyasi yordamida orriy ro'yhatga o'girib olishimiz kerak
# #tuples o'zgarmas ro'yhatni oddiy ro'yhatga o'girib oldik
# sonlar = list(sonlar)
# #Oddiy ro'yhatga o'girilgan ro'yhatni elon qildik
# print(sonlar)
# #Bu ro'yhat ustida amallar bajaramiz
# sonlar[0] = 500
# print(sonlar)
# sonlar_1 = sonlar.pop(2)
# print(sonlar_1)
# sonlar.append(70)
# print(sonlar)
# sonlar.insert(4, 356)
# print(sonlar)
# del sonlar[3]
# print(sonlar)
# sonlar.remove(20)
# print(sonlar)


#AMALIYOT
#1-masala
# davlatlar = ["Italiya", "Rossiya", "Amerika", "Xitoy", "Koreyya", "Yangi Zellandiya", "Vetnam", "Tayvan"]
# #Davlatlar ro'yhati ekranga chiqadi
# print(davlatlar)
# #Davlat ro'yhatining uzunligi
# print("Davlatlar ro'yhatida ", len(davlatlar), " ta davlat bor")
# #
# print("sorted() qaytargan ro'yhat: ", sorted(davlatlar))
# print("Asl ro'yhat: ", davlatlar)
# #Davlatlar ro'yhatini teskarisiga chiqaradi
# davlatlar.reverse()
# print(davlatlar)
# #Davlatlar ro'yhatini alfabet tartibda chiqaradi
# print(sorted(davlatlar))
# #Davlatlar ro'yhatini teskari alfabet tartibda chiqaradi
# print(sorted(davlatlar, reverse=True))


#2-masala
#120 dan 1200 gacha juft sonlar ro'yhati
# sonlar = list(range(120, 1200, 2))
# print(sonlar)
# #Sonlarning yig'indisi
# print("Sonlarning yig'indisi: ", sum(sonlar), " ga teng")
# #Eng kichkina son
# print("Eng kichik son: ", min(sonlar), " ga teng")
# #Eng katta son
# print("Eng katta son: ", max(sonlar), " ga teng")
# #eng katta va eng kichik son orasidagi farq
# print("Eng katta va eng kichik son orasidagi farq: ", max(sonlar)-min(sonlar), " ga teng")
# #ro'yhatdagi elementlar soni
# print("Sonlar ro'yhatida: ", len(sonlar), " ta element bor")
# #Ro'yhatning boshidagi 20 ta element
# print("Ro'yhatning boshidagi 20 ta element: ", sonlar[:20])
# #Royhatning o'rtasidagi 20 ta element
# print("Ro'yhatning o'rtasidagi 20 ta element: ", sonlar[261:281])
# #Ro'yhatning oxirisidagi 20 ta element
# print("Ro'yhatning oxirisidagi 20 ta element: ", sonlar[-20:])


#3 masala
#Taomlar ro'yhati
# taomlar = ['Osh', 'sho\'rva', 'mastava', 'lag\'mon', 'shashlik']
# # #Yangi nonusgta nomli ro'yhat. Taomlar ro'yhatidan nusha olinayapdi
# nonushta = taomlar[:]
# # #Nonushta ro'yhatidan faqat nonshtaga yeyiladiganlari qoldirilayapdi
# # #Osh olib tashlanayapdi
# del nonushta[0]
# # #Lag'mon olib tashlanayapdi
# del nonushta[3]
# # #Shashlik olib tashlanayapdi
# del nonushta[-1]
# # #Elementlari o'chirilgan nonushta ro'yhati elon qilinayapdi
# # print(nonushta)
# # #Nonushta ro'yhatiga qaymoq qo'shilayapdi
# nonushta.append('qaymoq')
# # #Nonushta ro'yhatining ikkinchi indeksiga issiq non qo'shilayapdi
# nonushta.insert(1, 'issiq non')
# # print(nonushta)
# # print(taomlar)

# #4-masala
# #Yuqoridagi nonushta ro'yhati o'zgarmas ro'yhatga aylantirilayapdi
# nonushta = tuple(nonushta)
# print(nonushta)
# #O'zgarmas ro'yhatni o'zgartirib bo'lmaydi. Uni o'zgartirish uchun oddiy ro'yhatga o'tib olish kerak


#YANGI MASALALAR
# Boshlang'ich darajadagi masalalar:
# Elementlarni chiqarish: Berilgan ro'yhatning birinchi va oxirgi elementlarini ekranga chiqaring.
# sonlar = list(range(0, 18, 3))
# print(sonlar)
# print(sonlar[0])
# print(sonlar[-1])
# # Ro'yhat uzunligi: Ro'yhatdagi elementlar sonini aniqlang.
# print(len(sonlar))
# # Element qo'shish: Ro'yhatga yangi element qo'shing (masalan, append() funksiyasidan foydalaning).
# sonlar.append(25)
# print(sonlar)
# # Elementni o'chirish: Ro'yhatdan foydalanuvchi tanlagan bir elementni o'chirib tashlang.
# del sonlar[-5]
# print(sonlar)

# O'rta darajadagi masalalar:
# Minimum va maksimumni topish: Ro'yhatdagi eng kichik va eng katta qiymatlarni aniqlang.
# narxlar = [25400, 459000, 45000, 46200, 75900, 4594000]
# print("Narxlar ro'yhatidagi enf arzon narh", min(narxlar))
# print("Narxlar ro'yhatidagi eng qimmat narh", max(narxlar))
# # Ro'yhatni teskari aylantirish: Ro'yhatni teskari tartibda chiqaring (reverse() yoki slicing yordamida).
# narxlar.reverse()
# print("Narxlar ro'yhatiga teskari ro'yhat", narxlar)
# # O'rtacha qiymatni topish: Ro'yhat elementlari o'rtacha qiymatini hisoblang.
# print("Narxlar ro'yhatidagi o'rtacha narx:", sum(narxlar)/len(narxlar))
# # Elementlarni tartiblash: Ro'yhat elementlarini o'sish tartibida tartiblang (sort() funksiyasidan foydalaning).
# narxlar.sort()
# print(narxlar)


# Qiyinroq masalalar:
# Ikki ro'yhatni birlashtirish: Ikki ro'yhatni birlashtirib yangi ro'yhat yarating.
# juft_sonlar = list(range(0,20,2))
# toq_sonlar = list(range(1,20,2))
# print(juft_sonlar)
# print(toq_sonlar)
# sonlar = juft_sonlar + toq_sonlar
# print(sonlar)


