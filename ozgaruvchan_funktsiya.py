# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:23:24 2025

MAVZU:MOSLASHUVCHAN FUNKTSIYA

@author: 123
"""

# =============================================================================
# # Biz avvalgi darslarimizda funktsiya kiritganimizda argumentlar soni aniq bo'lar edi
# # Bazi hollarda argumentlar noaniq bo'lgan funktsiyalar kiritishga to'g'ri kelishi mumkun
# # Bunday hollarda *args(*arguments) usulidan foydalanamiz
# =============================================================================


# =============================================================================
# # *args usuli
# # summa() nomli funktsiya yaratamiz va bu funktsiyamiz argumentga istalgancha son kiritganimizda ularning yig'indisini hisoblaydi
# # def summa(*sonlar):#Argumentlar soni noaniq bo'lgan funktsiya kiritayapmiz
# #     """Kiritilgan sonlarning yig'indisini hisoblovchi funktsiya"""
# #     yigindi = 0#Yig'indiga 0 qiynat berayapmiz
# #     for son in sonlar:#Kiritiladigan argumentlar ya'ni sonlarning har birini son o'zgaruvchisiga yuklayapmiz
# #         yigindi += son#Yig'indiga sonni qo'shayapmiz
# #     return yigindi#Yi'indini funktsiyaga qaytarayapmiz
# # print(summa(5, 5, 9, 8, 26))#funktsiyani chaqirib uni konsolga chiqarayapmiz
# # print(summa(5))
# 
# # # Bu misolimizna yanada osonlashtirishimiz mumkun
# # def summa(*sonlar):#Argumentlar soni noaniq bo'lgan funktsiya kiritayapmiz
# #     """Kiritilgan sonlarning yig'indisini hisoblovchi funktsiya"""
# #     return sum(sonlar)#Sonlarning yig'indisini funktsiyaga qaytarayapmiz
# # print(summa(5, 7, 9, 12, 45, 36))
# # print(summa(4))
# =============================================================================


# =============================================================================
# # Bazi hollarda majburiy argumentlar kiritishga to'g'ri kelishi mumkun
# # Yuqoridagi misolimizda 2 ta agument aniq mavjud bo'lishi kerak bo'lsin
# def summa(x, y, *sonlar):#ikkita argument kiritilishi shart qolgan argumentlar ixtiyoriy bo'lgan sonlar yig'indisini chiqaruvchi funktsiya
#     """Kiritilgan sonlarning yig'indisini hisoblovchi funktsiya"""
#     return x+y+sum(sonlar)
# print(summa(5, 4))#Ikkita majburiy argument kiritilgan holat
# print(summa(14, 54, 12, 45, 14))#Ikkita argumentga qo'shimcha argumantlar kiritilgan holat
# print(summa(5))#Bu holatda bitta argument kiritsak xatolik beradi chunki majburiy argumentlar ikkita bo'lishi kerak
# =============================================================================

# =============================================================================
# *args usulida kiritilgan sonlar o'zgarmas ro'yhatga(tuples) saqlanadi
# va uning elementlari ustida amallar bajariladi
# =============================================================================


# =============================================================================
# # **kwargs usuli
# # Agar funktsiyaga kalit so'z k'rinishidagi argumentlar uzatilishi tala qilinsa
# # Va bunday argumantlar soni nomalun bo'lsa argumant oldidan ikkita yulduzcha qo'yiladi
# 
# # Masalan
# def talaba_info(ismi, familiyasi, **malumotlar):#ikkita parametr va undan keyin ixtiyoriy sondagi parametr kiritish mumkun
#     malumotlar['ismi'] = ismi#Ismi parametrini lug'atning kaliti sifatida argumentni esa qiymat sifatida lug'atga qo'shayapdi
#     malumotlar['familiyasi'] = familiyasi
#     return malumotlar#Ma'lumotlar nomli lug'atni funktsiyaga qaytarayapdi
# #funktsiyamizni talaba nomli o'zgaruvchiga yukladik
# #t_yili va t_joyi argumentlarni esa kalitso'z va qiymat ko'rinishida qo'shib oldik
# talaba = talaba_info('Faxriddin', 'Mamadiyev', t_yili = 1995, t_joyi = 'Surhondaryo')
# #Natijani ya'ni funktsiyani elon qilganimizda bq qo'shgan argumentlar lug'aning boshiga 
# #majburiy argumantlar esa lug'atning oxiriga o'tadi
# print(talaba)
# =============================================================================



# =============================================================================
# # AMALIYOT
# # 1.Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
# def kopaytma_top(*sonlar):#Funktsiya kiritib olayapmiz. Bu yerda argumentlar soni nomalum
#     """Sonlarning ko'partmasini chiqaruvchi funktsiya"""
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma
# print(kopaytma_top(2, 5, 8))
# print(kopaytma_top(2, 8, 9, 7))
# 
# # Ikkinchi usul
# def kopaytma_top(*sonlar):#Funktsiya kiritib olayapmiz. Bu yerda argumentlar soni nomalum
#     """Sonlarning ko'partmasini chiqaruvchi funktsiya"""
#     import math
#     return math.prod(sonlar)
# print(kopaytma_top(5, 7, 9))
# =============================================================================


# =============================================================================
# # 2.Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
# def talaba_info(ismi ,familiyasi, **malumotlar):
#     """Talaba haqida ma'lumotlar chiqaruvchi funktsiya"""
#     malumotlar['ism'] = ismi
#     malumotlar['familiya'] = familiyasi
#     return malumotlar
# print(talaba_info('faxriddin', 'mamadiyev', t_joyi='surhondaryo', t_yili=1995, malumoti='magistr'))
#     
# =============================================================================
