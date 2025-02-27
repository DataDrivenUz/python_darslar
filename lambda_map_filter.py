# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:10:05 2025

MAVZU:lambda, map va filter funktsiyalari

@author: 123
"""

# =============================================================================
# Pythonda qulayliklardan yana biri vaqtincha nomsiz funktsiya yaratish mumkun
# Biz avvalgi darslarda funktsiya yaratganimizda def metodidan foydalangandik
# lambda funktsiyasi orqali funktsiya yaratganimizda def dan foydalanmaymiz
# lambda orqali funktsiya quyidagicha yaratiladi
# 
# lambda argumant:ifoda
# 
# lambda ya'ni nomsiz funktsiyada istalgancha argumanet kiritish mumkun
# Lekin lambda bir marta kritiladi. Bunda return operatori shart emas
# Nomsiz funktsiya orqali biror ifodani tez xisoblash qulay
# =============================================================================



# =============================================================================
# # Quyidagi misolni koraylik. 
# # Bu misolda funktsiya lambda orqali ikkita argument qabul qilib aylanani uzunligini hisoblaydi
# 
# import math #math moduli chaqirib olinayapdi
# uzunlik = lambda pi, r:2*pi*r #funktsiya uzunlik nomli identifikatoriga yuklanayapdi va pi, r argumentlarni qabul qilib ifoda yaratilayapdi
# print(uzunlik(math.pi,10)) #Natija elon qilinayapdi
# 
# #Yana bir misol ko'raylik x ning y darajasini hisoblovchi funktsiya yarataylik
# product = lambda x, y:x**y #lambda funktsiya chaqirib olinayapdi unda argumantlar va ifoda kiritilayapdi
# print(product(5, 4)) #Funktsiya chaqirilib qiymatlar kiritilib natika konsolga chiqarilayapdi
# =============================================================================



# =============================================================================
# Quyida kiritilgan sonning darajasini hidoblovchi funkitsiyani qaraylik
# def daraja(n):#Funktsiya kiritilayapdi
#     return lambda x:x**n#lambda orqali x sonni n- darajasini hisoblovchi funktsiya qartarilayapdi
# kvadrat = daraja(2)#kvadrat uchun yangi funktsiya yaratilayapdi
# kub = daraja(3)#kub uchun yangi funktsiya yaratilayapdi
# print(f'3 ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng')
# =============================================================================



# map() funktsiyasi 
# Bu funktsiya argumant sifatida ro'yhat(lug'at) va boshqa funktsiya qabul qilib
# ro'yhatga qabul qilingan funktsiya orqali ishlov beradadi
# Sodda misol ko'raylik

# from math import sqrt #math modulidan sqrt yani kvadrat ildiz funktsiyasi chaqirib olinayapdi
# sonlar = list(range(11)) #0 dan 10 gacha sonlar ro'yhati yaratilayapdi
# print(list(map(sqrt, sonlar))) #map orqali sonlar ro'yhatidagi sonlarning kvadrat ildizi hisiblanib yangi ro'yhat yaratilib consolga chiqarilayapdi


# Yana bir misol ko'raylik
# Endi ro'yhatdagi sonlarning kvadratini chiqaruvchi funktsiya yasapmiz
# sonlar = list(range(11))
# def daraja2(x):
#     return x*x
# print(list(map(daraja2, sonlar)))

# Yuqoridagi 2- misolimizda sonlar ro'yhati yaratilayapdi
# daraja2 funktsiyasi kiritilayapdi va unda x*x ifoda qaytarilayapdi
# 4-qatorda pap funktsiyasi ordamda lro'yhatdagi sonlarning kvadrati hisoblanib yangi ro'yhatga joylanayapdi
# map ichidagi daraja2 argunment daraja2 funktsiyasi sonlar esa kiritilgan ro'yhat'


# map funktsiyasi bo'lmaganda bu ro'yhatni quyidagicha yaratardik
# sonlar = list(range(11))
# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
# print(kvadratlar)


# map() funktsiyasiga bir nechta ro'yhatlarni ham uzatish mumkun
# a = [2, 5, 8] #Ro'yhatlar kiritilayapdi
# b = [9, 4, 7]
# Ushbu funktsiyada lambda funktsiyasi map funktsiyasining birinchi argumenti
# unda x va y yani lug'atlarning mos elementlari qo'shish ifodasi kiritilayapdi 
# a_plus_b = list(map(lambda x, y:x+y, a, b))
# print(a_plus_b) #Yangi ro'yhat ya'ni ro'yhatlarning mos elementlari qo'shilib yangi ro'yhat tuzilayapdi


# map() funktsiyasi faqat sonlar emas matinlar bilan ham ishlaydi

# ismlar = ['hasan', 'akmal', 'dilshod', 'sherzod', 'zafar']#ismlar ro'yhati tuzib olinayapdi
# katta_harf = list(map(lambda matn:matn.upper(), ismlar))
# print(katta_harf)

# Yuqoridagi misolimizda ismlar ro'yhatidagi matnlarni katta harfda chiqardi



# =============================================================================
# # filter() funktsiyasi
# # Bu funktsiya ham argument sifatida ro'yhat va funktsiya qabul qiladi
# # Bunda argumentga kiritilgan funktsiya mantiqiy qiymat qaytarishi kerak(True yoki False)
# # Tasdodifiy sonlar ro'yhatidan juft sonlar ro'yhatini ajratib oluvchi funktsiya yozamiz
# 
# # import random as r #Random funktsiyasini chaqirib olayapmiz
# # sonlar = r.sample(range(100), 10) #0-99 oralig'idagi tasodifiy 10 ta sonni ajratib olayapmiz
# 
# # def juftmi(x): #Sonlar juftligini tekshiruvchu funktsiya kiritilayapdu
# #    """Son juft bo'lsa True aks holda False qartaruvchi funktsiya"""
# #    return x%2==0
# 
# # juft_ronlar = list(filter(juftmi, sonlar))
# # print(sonlar)
# # print(juft_ronlar)
# 
# 
# # # Keling bu funktsiyani lambda orqali yozamiz
# # import random as r
# # sonlar = r.sample(range(100), 10)
# # juft_fonlar = list(filter(lambda son:son%2==0, sonlar))
# 
# # print(sonlar)
# # print(juft_fonlar)
# =============================================================================


# # filter funktsiyasi orqali matinlarni ham saralaylik
# # Ushbu ro'yhatdan bosh harfi b harfi bilan boshlanuvchi mevani chiqaraylik
# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
# mevalar_b = list(filter(lambda meva:meva.startswith('b'), mevalar))
# print(mevalar_b)


# # Quyidagi misolimizda ro'yhat ichida 5 ta harfdan kam bo'lgan elementlar ro'yhatini chiqaramiz
# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
# mevalar_5 = list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar_5)

# # Quyida bosh harfi a oxirgi harfo r bilan tugaydigan mevalarni ajratib alohid aro'yhatga joylaymiz
# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
# mevalar2 = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
# print(mevalar2)

