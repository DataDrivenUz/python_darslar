# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 08:37:39 2025

MAVZU:MODULLAR

@author: f.mamadiev
"""
# =============================================================================
# 
# Funktsiyalarning qulayliklaridan biri ko'p takrorlanadigan kodlarni uni ichiga 
# yashirish va zarurta tug'ilganda undan foydalanishdur.
# Maqsadimiz dasturimizni ixcham va tushunarli qilib kelajakda o'zimiz va boshqalar foydalanishiga qulay qilish bo'lishi kerak
# Bu yo'nalishda biz dasturimizni bo'laklarga ya'ni modullarga ajratishimiz mumkun
# Bu bizga butub kodimizni bitta faylda emas bir nechta faylda bo'laklarga bo'lib saqlash imkononi beradi
# Bu usul yordamida dasturimiz bitta faylni ichida juda ko'p ko'p va chalkash kodlar yozishni oldimi oladi
# =============================================================================


# =============================================================================
# Modul bu loyihamiz ichida alohida fayl bo'lib unda turli kerakli funktsiyalar va o'zgaruvchilarni saqlashimiz mumkun
# Bu bizga asosiy dasturimizda chalg'imasdan ishlashimizga imkod beradi
# Moduldagi funktsiya va o'zgaruvchilar kerak bo'lganda unga murojat qilib ishlaytayvermiz
# =============================================================================


# =============================================================================
# Moduldagi funktsiya va o'zgaruvchilarni istalgan paytda chaqirishimiz, boshqa dasturchilar bilan ulashishimiz
# Yoki kelajakda o'zimizning boshqa loyihalarimizda ishlatishimiz mumkun
# =============================================================================

# =============================================================================
# Modul yaratish uchun asosiy fayilimizdagi funktsiya va o'zgaruvchilarni boshqa faylga ko'chiramiz holos
# Modul yaratib u bilan ishlashimiz uchun asosiy fayil va modul fayili bitta papkada bo'lgani maqul
# Bunda asosiy faylimizga main.py deb nom berganimiz maqsadga muvofiq
# =============================================================================


# Avvalgi darslarimizda ko'rgan avto_info nomli funktsiyamizni bo'laklarga bo'lib avto_info_mod.py degan faylga saqlaymiz



# =============================================================================
# Modul ichidagi istalgan funktsiyaga murojat qilish uchun uni avval chaqirib olishimiz kerak
# Chaqirib olish quyidagi tartibda amalga oshiriladi
# import modul_nomi
# Modul ichidagi funktsiyaga murojat qilish uchun esa 
# modul_nomi.funksiya_nomi()
# Yani avval modul nomi keyin esa nuqta qo'yib funksiya nomi kiritiladi'
# 
# =============================================================================


# =============================================================================
# # Keling avto_info_mod.py modulimizga va uni ichidagi funktsiyalarga murojat qilamiz
# import avto_info_mod#avto_info_mod fayilini ya'ni modulini chaqirayapmiz
# 
# # avto_info_mod modulidagi afto_info funktsiyasini chaqirib olib uni avto_1 o'zgaruvchisiga yuklayapmiz
# avto_1 = avto_info_mod.afto_info('GM', 'Malyubu', 'qora', 'mehanika', 2020, narhi= 40000)
# # avto_info_mod modulidagi info_print funktsiyasini chaqirib olayapmiz va un orqali avto_1 ni elon qilayapmiz
# avto_info_mod.info_print(avto_1)
# 
# Ko'rib turganimizdek moduldan foydalanganimizda kodimiz 3 qator toza va tushunarli bo'ldi
# Bu urqali biz 20 qatordan ortiq kodimizni yashirdik va ixcham kodga ega bo'ldik
# Bu yerda import modul nomi bir marta kod boshida yoziladi
# =============================================================================


# =============================================================================
# # MODULGA QISQA NOM BERISH
# # Yuqoridagi misolimiz kabi misollarda modul nomi uzun bo'lib noqulayliklarga olib kelishi mumkun
# # Bu holatda as operatori orqali modulga qisqa nom berib unga murojat qilish mumkun
# # Masalan
# 
# import avto_info_mod as aim #avto_info_mod modulini uning bosh harflari orqal qisqacha nomladik
# avto_1 = aim.afto_info('GM', 'malyubu', 'qora', 'mehanika', 2020, narhi=40000)
# aim.info_print(avto_1)
# 
# Ikkala holatda ham kodimiz birhil ishlaydi
# Farqi bu usulimizda kodimiz yanada qisqaroq bo'ladi
# Modulga qisqa nom berganimizda bu nomdi dasturimizda foydalanadigan boshqa mdullarda
# yoki shu faylning o'zida yo'qligiga ishonch hosil qilishimiz kerak
# Agar qisqa nom boshqa joyda bo'lmasa bundan keyin ham bu nomdan foydalanmasligimiz kerak
# =============================================================================



# =============================================================================
# # MODUL ICHIDAGI MA'LUM FUNKTSIYALARNI KO'CHIRIB OLISH
# # Agar modulimiz katta bo'lsa va undagi bazi funktsiyalar bizga kerak bo'lsa ularni 
# # from modul_nomi import funktsiya_nomi orqali murojat qilishimiz mumkun
# # Endi kodimizda funktsiyalarni chaqirganda modul nomisiz to'g'ridan to'g'ri murojat qilishimiz mumkun
# 
# # Yuqoridagi misolimizga qaytaylik
# from avto_info_mod import afto_info, info_print #Modulimizdan afto_info va info_print funktsiyalarini chaqirib olayapmiz
# 
# # Endi funktsiyalarga to'g'ridan to'g'ri murojat qilishimiz mumkun
# avto_1 = afto_info('GM', 'mulyubu', 'qora', 'avtomat', 2024, narhi=4000)
# info_print(avto_1)
# 
# Ko'rib turganimizdek modul domidan faqat br marta foydalandik natija esa bir hil
# =============================================================================



# =============================================================================
# # FUNKTSIYALARGA QISQA NOM BERISH
# # Yuqorida modul ichidagi funktsiyalarni chaqirib oldik va kodimizda bu funktsiyalardan foydalandik
# # Bu funktsiyalarni ham moduldagi kabi qisqa nom bilan murojat qilishimiz mumkun
# from avto_info_mod import afto_info as ainfo, info_print as iprint
# 
# avto_1 = ainfo('GM', 'MALYUBU', 'qora', 'avtomat', 2024, narhi=40000)
# iprint(avto_1)
# 
# Kodimiz yanada ixchamlashdi
# =============================================================================



# =============================================================================
# MODUL ICHIDAGI BARCHA FUNKSIYALARNI KO'CHIRIB OLISH
# Modul ichidagi barcha funksiyalarni asosiy dasturga ko'chirib olish uchun from modul_nomi import * komandasidan foydalanamiz.
# =============================================================================



# PYTHON MODULLARI
# Python dasturlash tilida bir qancha o'zining modillar mavjud
# Ularni ir nechtasini ko'ramiz

# math moduli
# Bu bodulda matematik funktsiyalarni bajaruvchi funktsiyalar va o'zgaruvchilar joylashgan
# Ularni bir nechtasini ko'raylik


# =============================================================================
# # sqrt() - qavs ichida berilgan qiymatning kvadrat idizini chiqaradi
# import math #Modulni chaqirib olayapmiz
# 
# x=400
# print(math.sqrt(x))
# 
# # Bu misolni quyidagicha ham bajarishimiz mumkun
# from math import sqrt
# x=400
# print(sqrt(400))
# =============================================================================



# =============================================================================
# # # pow(x, y) - x ning y darajasini qaytaradi
# # import math 
# # print(math.pow(4, 7))
# 
# # # Ikkinchi usul
# # from math import pow
# # print(pow(4, 7))
# =============================================================================



# =============================================================================
# # # pi ning qiymati
# # from math import pi
# # print(pi)
# =============================================================================


# =============================================================================
# # Logarifm funktsiyalar
# import math
# print(math.log2(8))
# print(math.log10(10000))
# =============================================================================



# =============================================================================
# # random moduli
# # random moduli tasodifiy sonlar bilan ishlash uchun qulay finktsiyalarga boy
# # Masalan biror oraliqdagi tasodifoy sonni ko'ramiz
# 
# import random as r #Random modulini chaqirib oldik va uni r o'zgaruvchisiga yukladik
# son = r.randint(10, 120) # 10 da 120 gacha bo'lgan sonlar ichida ixtiyoriysini chiqaradi
# print(son)
# =============================================================================


# =============================================================================
# # choice(x)
# # choice(x) x ninf ichida tasodifiy qiymatni qaytaruvchi
# import random as r#Modulni chaqirib olayapmiz
# ismlar = ['olim','anvar','hasan','husan']#Ro;yhat
# ism = r.choice(ismlar)#Ro'yhat ichidan ixtiyoriy bittasini qaytarayapmi
# print(ism)#va bu ismni elon qilayapmiz
# print(r.choice(ism))#Bu ism ichidan ham ixtiyoriy harfni qaytarib elon qilayapmiz
# =============================================================================



# shuffle(x) x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funktsiya 
# Bunda x ichida bir birnechta o'zgaruvchi bo'lishi kerak
import random as r
x = list(range(11))
print(x)
r.shuffle(x)
print(x)