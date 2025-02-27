# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:36:57 2025
Mavzu: Sonlar bilan ishlash
@author: f.mamadiev
"""

#Python dasturlash tilida matinlarda bo'lgani kabi sonlar ustida ham turli amallar metodlar kiritishimiz  umkun
#Masalan
# a = 6
# b = 7.2
# c = a*b
# print(c)
#Ko'rib turganimizdek a sonini turi int ya'ni butun son b sonining turi float ya'ni o'nlik son bo'layapdi. butun sonni o'nlik songa ko'paytirganimizda natija o'nlik son chiqayapdi
#Butun va o'nlik sonlar orasida bajarilgan arfimetik amallar natijasi har doim o'nlik so'n chiqadi 
#Masalan
# pi = 3.14
# radius = 5
# diametr = 2*radius
# aylana_uzunligi = pi*diametr
# print("Radiusi " , radius , " ga teng bo'lgan aylananing uzunligi ", aylana_uzunligi, " ga teng")

#Bundan tashqari sonlarning turini ham aniqlashimiz mumkun
# a = 8.5
# b = 7
# print(type(a))
# print(type(b))

#O'qishga oson bo'lishi uchun sonlarni pastki chiziq bilan ajratib yozishimiz mumkun lekin sonni elon qilganimizda sonlar qo'shilib yoziladi
#Masalan
# dunyo_aholisi = 7_456_876_986
# print(dunyo_aholisi)

#Avval aytganimizdek ikkita butun sonni bo'lganimizda natija o'nlik son chiqadi
#Masalan
# a = 100
# b = 2
# c = a/b
# print(c)

#Bo'linma natijasini butun qismini olishimiz uchun // belgidan foydalanishimiz kerak
# c = a//b
# print(c)


#O'ZGARMAS SONLAR
#Dasturlash tilida o'zfaruvchining nomini katta harflarda yozsak uni o'zgarmas son deb qabul qiladi va bu o'zgaruvchini turini o'zgarmas deb qabul qiladi
#Masalan
# PI = 3.1467
# radius = 5
# aylana_yuzi = PI*radius**2
# print(type(PI))


#BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH
# x, y, z = 2, 5.2, 7.23
# a = x, y, z
# print(a)


#O'ZGARUVCHILAR TURINI ALMASHTIRISH
#Odatda matinga sonni yoki songa matinni qo'shib bo'lmaydi. Bunday holatlarda o'zgaruvchilarni turini:
#int() o'zgaruvchini turini butun songa almashtiradi
#float() o'zgaruvchi turini o'nlik songa almashtiradi
#str() o'zgaruvchi turini matinga almashtiradi
#Masalan
# ism = "Faxriddin"
# yosh = 30
#print(ism + " " + yosh + "da")
#Yuqoridagi buyruqni bajarganimizha hatolik chiqadi chunki matinni songa qo'shish mumkun emas. Bu xolatda sonni matin ko'rinishiga o'tkazib olishimiz kerak
# print(ism + " " + str(yosh) + " da")

#Foydalanuvchi tug'ilgan yili orqali uning yoshini aniqlaydigan dastur tuzamiz
#Foydalanuvchidan tug'ilgan yilini so'raymi
# t_yil = input("Nechanchi yilda tug'ilgansin? ")
#Hozirgi yildan foydalanuvchi tug'ilgan yilini ayiramiz. Tug'ilgan yilni foydalanuvchi matin ko'rinishida kiritgani uchun ayirishda tug'ilgan yilni butun songa o'girib olamiz
# yosh = 2025 - int(t_yil)
#Foydalanuvchiga nechi yoshda ekanligini aytamiz
#Matinga sonni qo'shib bo'lmaganligi uchun yoshni matinga o'girib olamiz
# print("Siz " + str(yosh) + " da ekansi")


#AMALIYOT
#1-amaliyot
#Foydalanuvchi kiritgan sonning kvadrari va kubini hisoblaydiga dastur
#Matinni songa o'girish funksiyasini qo'llaymiz
# son = int(input("Ixtiyoriy son kiriting: "))
# sonning_kvadrati = son**2
# sonning_kubi = son**3
# print("Siz kiritgan sonning kvadrati " + str(sonning_kvadrati) + " ga teng")
# print("Siz kiritgan sonning kubi " + str(sonning_kubi) + " ga teng")

#2-amaliyot
#Foydalanuvchidan yoshini so'rab uning tug'ilgan yilini aniqlovchi dastur
#Foydalanuvchi yoshini so'raymiz va u kiritgan sonni tipini o'zgartirib olamiz
# yosh = int(input("Yoshingiz nechchida? "))
#Hozirgi yildan foydalanuvchi yoshini ayiramiz
# t_yil = 2025 - yosh
#Ekranga foydalanuvchi tug'ilgan yilini matinga o'g'irib chiqatramiz
# print("Siz " + str(t_yil) + " da tug'ilgan ekansiz")

#3-amaliyot
#Foydalanuvchidan ikki son kiritishni so'rash va kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqarish
#Foydalanuvchidan son kiritishini so'raymiz va u kiritgan sonni turini integer ya'ni songa o'girib olamiz
birinchi_son = int(input("Birinchi sonni kiriting:\n>>>"))
ikkinchi_son = int(input("Ikkinchi sonni kiriting:\n>>>"))
#Foydalanuvchi kiritgan sonlar ustida bajarilgan amallarni boshqa o'zgaruvchilarga biriktirib olamiz
a = birinchi_son + ikkinchi_son
b = birinchi_son - ikkinchi_son
c = birinchi_son*ikkinchi_son
d = birinchi_son/ikkinchi_son

#Natijalarni ekranga chiqaramiz
print("Siz kiritgan sonning yig'indisi " + str(a) + " ga teng")
print("Siz kiritgan sonning ayirmasi " + str(b) + " ga teng")
print("Siz kiritgan sonning ko'paytmasi " + str(c) + " ga teng")
print("Siz kiritgan sonning bo'linmasi " + str(d) + " ga teng")

