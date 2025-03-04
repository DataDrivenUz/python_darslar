# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 08:22:31 2025

MAVZU:KO'P UCHRAYDIGAN HATOLAR'

@author: f.mamadiev
"""

# =============================================================================
# Dasturlash davomida dasturchilar bazi hatolarga yo'l qo'yishi mumkun. Bu tabiy
# Quyida biz bir nechta xato yozilgan kodlarni to'g'irlaymiz
# 
# 1-Misol
# son = float(input("Juft son kiriting: ")
# if son%2==0:
#     print("Bu son juft emas.')
# else:
#     print("Rahmat!"))
# 
# Yuqoridagi kodimizning 3-qatorida uchta xatolik mavjud. Elon qilinadigan matin 2-qatordagi kodga mos kelmaydo
# Chunku 2-qatorda juftson sharti kiritilayapdi. Matinda ese Bu son juft son emas habari berilgan
# Ikkinchi xatokil esa matinni boshida qo'shtirnoq oirisida esa birtirnoq ishlatilgan
# Birinchi qatorda ham hatolik bor yani float uchun qavs yopilmagan
# Aslida kod bu ko'rinishda bo'lishi kerak
# son = float(input("Juft son kiriting: "))
# if son%2==0:
#     print("Rahmat")
# else:
#     print("Bu son juft emas.")
# =============================================================================


# =============================================================================
# 2-Misol
# yosh = (input("Yoshingiz nechida?"))
# 
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")
# 
# Bu koddagi birinchi hatolik 1-qatorda yani input ham qahvs ichiga olinayapdi va input matin qabul qilganligi uchun uni butun songa o'girib olishimiz kerak
# 5-qatorda esa shartoperatoriga ikki nuqta : qo'yilmagan
# oxirgi qatordagi habar matni faqatgina oxirgi shart uchun bo'lib qolgan
# # To'g'ri kod quyidagicha
# 
# yosh = int(input("Yoshingiz nechida? "))
# 
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")
# =============================================================================


# =============================================================================
# 3-Misol
# x = float(input("Birinchi sonni kiriting: ")
# y = float(input("Ikkinchi sonni kiriting: ")
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}")
# else
#     print(f"{x}>{y}")
# Bu kodimizning birinch va ikkinchi qatorlarida qavslar to'liq yopilmagan. Ikkita qavs ochilgan lekin bittasi yopilgan
# 6-qatorda esa ham birtirnoq ham qo'shtirnoq ishlatilgan
# 7-qatorda esa shartga ikki nuqta : qo'yilmagan
# To'g'ri kod quyidagicha
# 
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")
# =============================================================================


# =============================================================================
# 3-misol
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun'
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# if savat:
#     for mahsulot in savat
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            
# 
# Bu kodning birinchi qatorida ro'yhat qavsi yopilmagan
# Uchinchi qatorda savat nomli ro'yhatga element qo'shayapmiz lekin savat nomli ro'yhatning ozi yo'q
# Beshinchi qatorda esa for operatori uchun ikki nuqta ishlatilmagan
# To'g'ri kod quyidagicha
# 
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# 
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")      
# =============================================================================


# =============================================================================
# 4-misol
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# 
# 
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo'shing: '))
# 
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahslot)
#     else:
#         mavjud_emas.append(mahsulot)
# 
# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# Bu kodda 130 qatorda f-stringda qo'sh tirnoq ishlatishimiz kerak edi. Agar birtirnoq ishlatadigan bo'lsak matinni qo\'shing ko'rinishida yozishimiz kerak
# 136 qatorda esa mahslot deb yozilgan matin o'rniga mahsulot bo'lishi kerak edi
# 142 qatordagi for operatori esa shart operatorining badani sifatida yozilishi kerak edi
# 
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# 
# 
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# 
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# 
# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#       print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# =============================================================================


# =============================================================================
# 5-misol
# users = ['alisher1983','aziza','yasina' 'umar']
# 
# login = input("Yangi login tanlang:' )
# 
# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")
#     
# Bu kodda ro'yhat elementlarini ajratishda yasina elementidan keyin vergul qo'yilmagan
# 178-qatorda esa ham qo'shtirnoq ham birtirnoq ishlatilgan. Kodda yoki qo'shtirnoq yoki birtirnoq ishlatish kerak
# users = ['alisher1983','aziza','yasina' 'umar']
# 
# login = input("Yangi login tanlang:" )
# 
# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")
# 
# =============================================================================
