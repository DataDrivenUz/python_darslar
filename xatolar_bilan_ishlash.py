# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 13:50:45 2025

MAVZU:XATOLAR BILAN ISHLASH

@author: f.mamadiev
"""

# Dasturlash davomida turli xatolarga yo'l qo'yilishi mumkun. Syntaksis xatolardan tashqari bir nechta xatoliklar turlari mavjud
# Bu turdagi xatoliklarni faqatgina dasturni ishlatish davoida aniqlashimiz mumkun
# Bu ko'rinishdagi xatoliklar yuz berganda dastur to'xtab qolishi mumkun. Dastur to'ztab qolmasligi uchun istisno obyekt yaratib olinadi
# Istisno boyektni tutib olish uchun try-except operatori ishlatiladi
# try-except operatorining ishlashi quyidagicha 
# try operatorining badanida bajaritlishi kerak bo'lgan kod yoziladi
# except operatorining badanida xatolik chiqqanda bajarilishi kerak bo'lgan kod yoziladi


# =============================================================================
# Tushunarli bo'lishu uchun quyidagi misolni ko'raylik
# yosh = input("Yoshingizni kiriting: ")#Foydalanuvchidan yoshini kiritishini so'rayapmiz
# yosh = int(yosh)#Foydalanuvchi kiritgan ma'lumotni butin songa o'g'rib olayapmiz
# print(f"Siz {2025-yosh} yilfa tug'olgan ekansiz")#Foydalanuvchi qachon tug'ilganligi elon qilinayapdi
# 
# Bu kodimiz foydalanuvchi faqat butun son kiritgandagina ishlaydi. Agar foydalanuvchi butun son o'rniga o'nli son yoki boshqa ma'lumot kiritsach
# Bu xolatda dastur Value Error ya'ni qiymat hatoligini beradi
# Bu holat oldini olish uchun try except operatorlaridan quyidagi tartibda foydalanishimiz kerak
# yosh = input("Yoshingizni kiriting: ")#Foydalanuvchidan yoshini kiritishini so'rayapmiz
# try:
#     yosh = int(yosh)#Foydalanuvchi kiritgan ma'lumotni butin songa o'g'rib olayapmiz
#     print(f"Siz {2025-yosh} yilda tug'olgan ekansiz")#Foydalanuvchi qachon tug'ilganligi elon qilinayapdi
# except: #Foydalanuvchi o'nlik son yoki boshqa ma'lumot kiritganda 
#     print("Siz butun son kiritmagansiz")#Ekranga chiqadigan habar
# print("Dastur tugadi.")
# 
# Yuqoridagi kodimizda foydalanuvchidan yoshini kiritish so'raladi. Agar foydalanuvchi butun son kiritsa foydalanuvchi tug'ilgan yili elon qilinadi
# Agar foydalanuvchi butun son kiritmasa siz butun son kiritmadingiz degan xabar chiqadi va dastur tugadi degan xabar chiqadi
# =============================================================================


# try-except-else
# yuqoridagi misolimizda try operatorining badanida yosh = int(yosh) va print(f"Siz {2025-yosh} yilda tug'olgan ekansiz") kodlarini kiritayapmiz
# Aslida bu usul xato. To'g'ri kod try operatorini ichiga yosh = int(yosh) kodini kiritishimiz kerak
# except operatorini ichida esa try ni ichida kiritilgan kodda xatolik chiqanda bajariladigan kod kiritishimiz kerak
# else operatorini ichida esa try operatori ichidagi kodda xatolik chiqmaganda bajariladigan ifoda kiritiladi
# Yani:
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
except:
    print("Siz butun son kiritmadingiz.")
else:
    print(f"Siz {2025-yosh} da tug'ilgan ekansi.")
