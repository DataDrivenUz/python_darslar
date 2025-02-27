# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:07:58 2025

@author: f.mamadiev
"""

# ism = "Faxriddin"
# print(ism)

#Pythonda matnlar kiritayotganimizda turli hil unicodlar ya'ni turli alifbolar belgilardan foydalanishimiz mumkun
#Masalan
# televizor = "📺"
# print("Men bugun yangi", televizor, "sotib oldim")

#Shuning dek matinlarni qo'shishda , dan tashqari + belgisidan ham foydalanish mumkun
#Masalan
# ism = "Faxriddin"
# familiya = "Mamadiyev"
# ism_familiya = ism + familiya
# print(ism_familiya)

#Ko'rib turganimizdek ism va familyra qo'shilib qoldi. Bu holatni bartaraf etish uchun bo'shliq qo'yishimiz kerak
# ism_familiya = ism + " " + familiya
# print(ism_familiya)

#Ikki va undan ko'p matin ko'rinishidagi o'zgaruvchilarni birlashrtirish uchun f-string dan ham foydalansak bo'ladi
#masalan
# ism = "Faxriddin"
# familiya = "Mamadiyev"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

#Bundan tashqari uzun matimlarni ham qo'shish uchun f-string dan foydalansak bo'ladi
# print(f"Salom, mening ismim {ism}. {ism_sharif}")

#MAHSUS BELGILAR
#Matinlar orasiga bo'shliq qo'shish uchun \t belgisidan foydalanamiz, keyingi qatorga tushurish uchun \n belgisidan foydalanamiz
#Masalan
#Oddiy matin
# print("Hello world")

#Bo'shliq qo'shilgan matin
# print("Hello \tworld")

#keyingi qatorga tushurilgan matin
# print("Hello \nworld")

#STRING METODLARI
#Pythonda string ya'ni matinlar ustida amalga oshirish mumkun bo'lgan tayyor amallar to'plami mavjud. Bundam amallar to'plami Metodlar deb ataladi
#Bu metodlardan foydalanish uchun matn.metod_nomi() ko'rinishida kiritishimiz kerak

#upper() metodi matindagi har bir harifni katta harflarda kiritish uchun ishlatiladi
# ism = "Faxriddin"
# sharif = "Rayimkulovich"
# ism_sharif = f"{ism} {sharif}"
# print(ism_sharif.upper())

#lower() metodi matindagi har bir harifni kichik harflarda kiritish uchun ishlatiladi
# print(ism_sharif.lower())

#title() metodi matindagi har bir so'zni bosh harfini katta harf bilan 
# print(ism_sharif.title())

#capitalize metodi matindagi faqat birinchi harfini katta harf bilan elon qiladi
# print(ism_sharif.capitalize())

#lstrip() matin boshidagi bo'shliqni olib tashlaydi
# meva = "   olma   "
# print(meva)
# print("men " + meva.lstrip() +"ni yashi ko'raman")

#rstrip() matin oxiridagi bo'shliqni olib tashlaydi
# print("men " + meva.rstrip() +"ni yashi ko'raman")

#strip() matinning o'ng va chap tomonifagi bo'shliqni olib tashlaydi
# print("men " + meva.strip() +"ni yashi ko'raman")


#INPUT FOYDALANUVCHI BILAN MULOQOT
#Ma'lumotni o'zimiz emas foydalanuvchi kiritishi uchun input() funktsiyasidan foydalanaiz
# ism = input("Isming nima?\n>>>")
# print("Assalomu alaykum! Mening ismim Faxriddin")

#AMALIYOT
#1-amaliyot
# kocha = 'Bog\'bon'
# mahalla = 'Sog\'bon'
# tuman = "Bodamzor"
# viloyat = "Samarqand"
# manzil = kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati"
# print(manzil)

#2-amaliyot
# kocha = input("Qaysi ko'chada turasan\n>>>")
# mahalla = input("Qaysi mahallada turasan\n>>>")
# tuman = input("Qaysi tumanda turasa\n>>>")
# viloyat = input("Qaysi viloyatda turasan\n>>>")
# manzil = kocha + " k'chasi, " + mahalla + " mahallasi, " + tuman + " tumani " + viloyat + " viloyati"
# print("Assalomaleykum! Men " + manzil + " da yashayman")


#3-amaliyot
kocha = 'Bog\'bon'
mahalla = 'Sog\'bon'
tuman = "Bodamzor"
viloyat = "Samarqand"
manzil = kocha + " ko'chasi,\n" + mahalla + " mahallasi, \n" + tuman + " tumani, \n" + viloyat + " viloyati"
yangi_manzil = f"{kocha} ko'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati"
manzil = yangi_manzil
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())