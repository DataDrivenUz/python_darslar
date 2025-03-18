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


# =============================================================================
# try-except-else
# yuqoridagi misolimizda try operatorining badanida yosh = int(yosh) va print(f"Siz {2025-yosh} yilda tug'olgan ekansiz") kodlarini kiritayapmiz
# Aslida bu usul xato. To'g'ri kod try operatorini ichiga yosh = int(yosh) kodini kiritishimiz kerak
# except operatorini ichida esa try ni ichida kiritilgan kodda xatolik chiqanda bajariladigan kod kiritishimiz kerak
# else operatorini ichida esa try operatori ichidagi kodda xatolik chiqmaganda bajariladigan ifoda kiritiladi
# Yani:
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError: #Bu misolimizda qiymat xato kiritilishi oldini olish uchun ValueError dan foydalanayapmiz
#     print("Siz butun son kiritmadingiz.")
# else:
#     print(f"Siz {2025-yosh} da tug'ilgan ekansi.")
# =============================================================================


# =============================================================================
# ZeroDivisionError
# Bazi arfimetik amallarda 0 ga bo'lish xatoligi yuzaga kelishi mumkun
# Aynan shu xatolikni oldini olish uchun ZeroDivisionError dan foydalanamiz
# x,y = 10,5
# try:
#     x/(y-5)
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkun emas")
# 
# Yuqoridagi misolimizda x va y ga qiymatlar berilayapdi arfimetik amalda esa x ya'ni 10 0 ga bo'linayapdi. Bu esa mumkun emas
# Xatolikni oldini olish uchun try-except va ZeroDivisionError dan foydalandik
# Xatolik chiqqan taqdirda ham kodimiz to'xtab qolmasdan keyingi kodga o'tib ketadi
# =============================================================================



# =============================================================================
# IndexError 
# Bu xatolik odatda ro'yxatda mavjud bo'lmagan elementga murojat qilganimizda chiqadi
# Masalan
# talabalar = ['Olim', 'Vali', 'Sobir', 'Behruz', 'Sodiq']
# try:
#     print(talabalar[8])
# except IndexError:
#     print(f"Ro'yhatda {len(talabalar)} ta talaba bor")
# 
# Yuqoridagi misolimizda 5 ta elementdan iborat talabalar ro'yhatini yaratib oldik
# Bu ro'yhatni ichidan 7-indexli talabani consolga chiqarmoqchimiz. Lekin ro'yxatda 5 ta talaba bor
# Xatolik chiqqanda kodimiz to'xtab qolmasligi uchun kidimizni try-except IndexError operatorlari badaniga kiritib qo'ydik
# =============================================================================


# =============================================================================
# KeyError
# Bu turdagi xatolik lug'atda bavjud bo'lmagan kalitga burojat qilganimizda kelib chiqadi
# Masalan
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}
# # user nomli lug'at yaratib olayapmiz
# key = 'tel' #key o'zgaruvchisiga tel qiymatini yuklayapmiz
# try:
#     print(f"Foydalanuvchi: {user[key]}") #user lug'atini ichidan key kalit so'zini qiymatini konsolga chiqarmoqchimiz
# except KeyError: #lug'atda key kaliti mavjud bo'lmaganligi uchun KeyError dan foydalandik
#     print(f"Lug'atda {key} kaliti mavjud emas") #Xatolik chiqqanda consolga chiqadigan matin
# =============================================================================


# Bazi hollarda turli xil hatolarni ushlashga to'g'ri kelishi mumkun
# Bunday hollarda except operatorini bir necha marta ishlatamiz
# masalan
n = input("Butun son kiriting: ")#Foydalanuvchidan butun son kiritishini so'rayapmiz
try:
    n = int(n)
    x = 20/n
except ValueError:#Agar foydalanuvchi butun son kiritmasa
    print("Siz butun son kiritmadingiz!")
except ZeroDivisionError:#Agar foydalanuvchi 0 kiritsa
    print("0 ga bo'lish mumkun emas!")
else:
    print(f"x = {x}")