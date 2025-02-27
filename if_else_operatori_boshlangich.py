# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:33:55 2025
MAVZU: IF-ELSE va Tarmoqlanish
@author: f.mamadiev
"""

#Dasturlash tillarida ma'lum bir shartlar bajarilganda kodning biror qismi shishashini  yoki shart bajarilmaganda kodning boshqa qismi ishlashini ko'rishimiz mimkun
#Bunday jarayonlar tarmoqlanish deyiladi

#if operatori yordamida bunday shartlarni yozishni, tekshirishni va tekshirish natijalarini o'rganamiz

#if ingliz tilida agar deb tarjima qilinadi va barcha dasturlash tillarida ishlatiladi

#Keling bir misol ko'raylik
#Avtomabillar ro'yhatini tuzib olaylik
# avtomabillar = ['audi', 'marcedes', 'volvo', 'bmw', 'hyundai']
# #for sikli boshlanayapdi. Avtomabillar ro'yhatidagi har bir o'zgaruvchini avto o'zgaruvchisiga yuklayapdi
# for avto in avtomabillar:
#     #Agar avto bmw ga teng bo'lsa degan shart kiritilayapdi
#     if avto == 'bmw':
#         #bmw ni hamma harflarini katta harflar bilan consolaga chiqaradi
#         print(avto.upper())
#     #Aks holda elementning faqat birinchi harfini katta harflar bilan chiqaradi
#     else:
#         print(avto.title())
# #Yuqoridagi shartimizda agar avtomabillar ro'yhatidagi elementlarni har birini avto o'zgaruvchisiga yuklayapdi
# #Agar element bmw bo'lsa uning hamma harfini katta harflar bilan chiqaradi.
# #Aks holda ya'ni element bmw bo'lmasa uning faqat birinchi harfini katta harflar bilan chiqaradi

#Tarmoqlanish operatorida == belgi tengmi degam ma'non bildiradi
#!= belgi esa teng emasmi dengan manoni bildiradi
#Bu ikki belgi orqali biz shartlarni tekshirishimiz mumkun


#Endi != ya'ni teng emasmi belgisi orqali matinlarni teng emasligini twskshiramiz
#Foydalanuvchidan ismini so'raymiz
# ism = input('Ismingizni kiriting\n>>>')
# #Agar foydalanuvchi kiritgan ism Ali ga teng bo'lmasa degan shart kiritilayapdi
# #Bu yerda ism.lower() foydalanuvchi kiritgan ism katta kichik harfligidan qatiy nazar kichkina harfga o'tkazib olayapdi
# if ism.lower() != 'ali':
#     # Agar yuqorydagi shart bajarilsa ya'ni kiritilgan ism ali bo'lmasa quyidagi habar chiqadi
#     print(f'Uzur {ism.title()}  biz Alini kutayapmiz')
#     #Aks holda
# else:
#     #yani kiritilgan ism Ali bo'lsa quyidagi matin chiqadi
#     print('Salom Ali!')


#SONLARNI SOLISHTIRISH
#Shart operatorlarida ==, != belgilaridan tashqari >, >=, <, <= belgilari ham ishlatiladi
#Foydalanuvchidan 12*6 nechiga tengligini so'rayapmiz
# javob = float(input('12*6 nechiga teng?\n>>>'))
# #Agar javob 72 ga teng emas bo'lsa degan shart kiritayapmiz
# if javob != 72:
#     #Shart bajarilsa ya'ni javob 72 ga teng bo'lmasa quyidagi xabar chiqadi
#     print('Javob xato.')


#Foydalanuvchidan yoshini so'raymiz. Agar uning yoshi 18 yoshdan katta bo'lsa Xush kelibsiz matnini ekranga chiqaramiz
#Aks holda kirish mumkun emas degan matinni chiqaramiz
# yosh = float(input('Yoshingiz nechida?\n>>>'))
# #Agar foydalanuvchi kiritgan yosh 18 dan katta yoki teng bo'lsa 
# if yosh >=18:
#     #Quyidagi matin chiqadi
#     print('Xush kelibsiz!')
#     #Aks holda
# else:
#     #Quyidagi matin chiqadi
#     print('Kirish mimkun emas')



#Foydalanuvchidan login kiritishini so'raymiz.
#Agar login 5 ta belgidan kam bo'lsa login qabul qilinmaydi. Aks holda login qabul qilinadi
# login = len(input('Login kiriting\n>>>'))
# #Agar kiritilgan login 5 ta belgidan kam bo'lsa 
# if login <= 5:
#     #Quyidagi matn chiqadi
#     print('Login 5 ta belgidan ko\'p bo\'lishi kerak.')
#     #Aks holda
# else:
#     # Quyidagi matin chiqadi
#     print('Login qabul qilindi.')
    
    
    
# #Foydalanuvchidan tug'ilgan yilini so'raymiz
# tugilgan_yil = float(input('Tug\'ilgan yilingizni kiriting\n>>>'))
# # #Agar quyidagi shart bajarilsa
# if 2025 - tugilgan_yil > 18:
# #     #Quyidagi matin chiqadi
#      print(f'Yoshingiz {2025 - tugilgan_yil} da ekan')
#      print('Marhamat kirishingiz mumkun!')
# #     #Aks holda
# else:
# #     # Quyidagi matin chiqadi
#      print('Voyaga yetmaganlarga kirish taqiqlanadi.')



#Agar kodimiz qisqa bo'lsa shartimiz va uninf badanini bir qatorda kiritish mmkun
# yosh = int(input('Yoshingiz nechada\n>>>'))
# if yosh > 60: print('Siz COVID-19 riski qatorida ekansiz')

# x, y = 25, 50
# print('x>y') if x>y else print('y<y')



#AMALIYOT
#1-masala
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# #car o'zgaruvchisiga cars ro'yhatidagi har bir elementni yuklayapdi
# for car in cars:
#     #Agar car gm ga teng bo'lsa. car.lower() bu elementni hamma harfini kichik harfga o'girayapdi
#    if car.lower() == 'gm':
#        #carning hamma harfi katta harf bilan chiqadi
#        print(car.upper())
#        #Aks holda
#    else:
#        #Elementning faqat birinchi harfi katta harf bilan chiqadi
#        print(car.title())
    
    
#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# #car o'zgaruvchisiga cars ro'yhatidagi har bir elementni yuklayapdi
# for car in cars:
#     #Agar car gm ga teng bo'lmasa. car.lower() bu elementni hamma harfini kichik harfga o'girayapdi
#     if car.lower() != 'gm':
#         #car ni faqat bosh harfini katta qilib beradi
#         print(car.title())
#         #Aks holda
#     else:
#         #hamma harfini katta qilib beradi
#         print(car.upper())



#2-masala
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
# foydalanuvchi_ismi = input('Loginingizni kiriting\n>>>')
# #Agar foydalanuvchining ismi admin bo'lsa
# if foydalanuvchi_ismi.lower() == 'admin':
#     # Quyidagi matin chiqadi
#     print(f'"Xush kelibsiz, {foydalanuvchi_ismi.title()}. Foydalanuvchilar ro\'yxatini ko''rasizmi?"')
#     #Aks holda quyidagi matin chiqadi
# else:
#     print(f'"Xush kelibsiz, {foydalanuvchi_ismi.title()}!"')


#3 - masala
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# x = int(input('Birinchi sonni kiriting\n>>>'))
# y = int(input('Ikkinchi sonni kiriting\n>>>'))
# if x == y:
#     print(f'{x} va  {y} sonlari teng')
# else:
#     print(f'{x} va  {y} sonlari teng emas')


#4-masala
#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
# son = float(input('Istalgan sonni kiriting:\n>>>'))
# if son > 0:
#     print('Kiritilgan son musbat.')
# else:
#     print('Kiritilgan son manfiy.')



#5-masala
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
son = int(input('Birorta son kiriting\n>>>'))
if son > 0:
    print(f'{son} ning kvadrat ildizi {son**(1/2)} ga teng.')
else:
    print("Musbat son kiriting")