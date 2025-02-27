# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:39:37 2025

#MAVZU: QIYMAT QAYTARUVCHI FUNKTSIYA

@author: 123
"""

#Biz avvalgi darsda funktsiya kiritishni va bu funktsiya natijasini print funktsiyasi orqali chiqargandik
#Bu usul doim qo'l kelmaydi
#Chunki biz consolga chiqqan malumotni qayta ishlolmaymiz
#Bunday hollarda qiymatni dasturga qaytarish unumli bo'ladi
#Qiymat qaytayuvchi funktsiyani return orqali yaratamiz

#MASALAN
#Ism va familiya parametrlarini olib to'liq ism qaytaruvchi sodda funktsiya tuzib olamiz
# def toliq_ism_yasa_yasa(ism, familiya):#Funktsiya kiritib olayapmiz
#     """To'liq ismni qaytaruvchi funktsiya"""
#     toliq_ism = f"{ism} {familiya}"#ism va familiya paramertlarini toliq ism o'zgaruvchisiga yuklab olayapmiz
#     return toliq_ism #To'liq ism qiymatini saqlab dasturga qaytaradi

# #Endi talaba_1 va talaba_2 o'zgaruvchilariga funktsiya qaytargan qiynmatni saqlaymiz
# talaba_1 = toliq_ism_yasa_yasa("olim", "hakimov")#
# talaba_2 = toliq_ism_yasa_yasa("hakim", "olimov")#

# #Endi funktsiyamiz qaytargan qiymatlarni consolga chiqaramiz
# print(f'Darsga kelmagan talabalar: {talaba_1.title()} va {talaba_2.title()}')
    
#Yuqoridagi misolimizda ism va familiyani toliq ism nomli o'zgaruvchiga yukladik
#Uning qiymatini return orqali qaytardik
#Funktsiya qaytargan qiymatlarni tababa_1 va talaba_2 o'zgaruvchilariga yukladi va consolga chiqardik



#Ixtiyoriy argumentlar
#Biz avvalgi darsimizda starndart qiymat tushunchasini o'rgangan edik
#Parametrga standartqiymat bersak argumentda uni ko'rsatish shart emas edi
#Yuqoridagi misolimizga otasining_ismi = "" deb nomlangan standarq qiymatli parametr qo'shib olamiz
# def toliq_ism_yasa(ism, familiya, otasining_ismi = ""):
#     """To'liq ism qaytaradigan funktsiya"""
#     if otasining_ismi:#Otasining ismi parametri mavjud bo'lsa
#        toliq_ism = f"{ism} {otasining_ismi} {familiya}"#iSM FAMILIYA OTASINING ISMI PARAMETRLARI KETMAKETLIGINI TOLIQ ISM O'ZGARUVCHISIGA SAQLAYAPMIZ
#     else:#Aks holda ya'ni otasining ismi parametri bo'sh bo'lsa ism va familiyani o'zin saqa
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism #Toliq_ism o'zgaruvchisini return orqali qaytarayapmiz

# talaba_1 = toliq_ism_yasa('olim', 'hakimov')#Otasining ismi kiritilmadi
# talaba_2 = toliq_ism_yasa('hakim', 'olimov', 'abrorovich')

# print(f'Darsga kelmagan talabalar: {talaba_1.title()} va {talaba_2.title()}')



# FUNKTSIYADAN LUG'AT QAYTARISH
# Yuqoridagi misollarda funktsiyadan qiymat qaytarishni ko'rdik
# Endi funktsiyadan lug'at qaytarishni ko'ramiz
# Quyidagi aftomabil haqidagi lug'atni ko'raylik
# def afto_info(kompaniya, model, rangi, korobka, yili, narhi=None):#Parametrlarni kiritib oldik
#      """Avtomabil haqidagi ma'lumotlar lug'atini qaytaruvchi funktsiya"""
#      avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#      return avto
# # Ko'rib turganimizdek narx parametriga None qiymat berdik
# # Bu python dasturlash tilida mavjud emas degan ma'noni bildiradi

# avto_1 = afto_info('GM', 'Malibu', 'qora', 'avto', 2018)#argumentlarni yangi o'zgaruvchiga narhni kieitmasdan ukladik
# avto_2 = afto_info('GM', 'Gentra', 'oq', 'mehanika', 2018, 15000)#endi narhni kiritdik
# avtolar = [avto_1, avto_2]#Ikkala o'zgarvchini yangi lug'at elementi sifatida kiritayapmiz
# print('Onlayn bozordagi avtomabillar narhi:')
# for avto in avtolar:#avto o'zgaruvchisiga avtolar ro'yhatidagi har bir elementni yuklayapmiz
#     if avto['narh']: #Agar avtoning narhi bor bo'lsa 
#        narhi = avto['narh']#narhi parametriga narhni yukla
#     else:#Aksholda
#        narhi = 'Nomalum'#Narhi parametriga Nomalum matnini yukla
#     print(f"{avto['rang']} {avto['model']}. Narhi: {avto['narh']}")#Natijani consolga chiqarayapmiz




# FUNKTSIYADAN RO'YHAT QAYTARISH
# Biz avvalgi darslarda range() yani oraliq funktsiyasini ko'rgan edik
# Endi bu funktsiyani o'zimiz yaratib olamiz
# def oraliq(min, max):#Sonlar nomli funktsiya argumentlarini min va max ko'rinshida kiritib oldik
#     """Oraliqdagi sonlarni chiqaruvchi funktsiya"""
#     sonlar = [] #Bo'sh ro'yhat yaratib olayapmiz
#     while max>min:#Toki max katta min ekan
#           sonlar.append(min)#Sonlar ro'yhatiga min qiymatni qo'shayapmiz
#           min += 1#minga 1 ni qo'sh
#     return sonlar#Sonlar ro'yhatini qaytar
# print(oraliq(5, 25))
# print(oraliq(1, 23))



#Yuqoridagi misolimizni biror qadamga farq qiluvchi oraliq sonlar misolida ko'ramiz
# def oraliq(min, max, qadam = 2):#Qadamga 2 standart qiymatni berdik
#     """Qadamli oraliqdagi sonlar ro'yhatini uzish funktsiyasi"""
#     sonlar = []
#     while max>min:
#         sonlar.append(min)
#         min += qadam
#     return sonlar
# print(oraliq(5, 20))

# # Endi Qadamni o'zimiz beradigan holatni ko'ramiz
# def oraliq(min, max, qadam):#Qadamga 2 standart qiymatni berdik
#     """Qadamli oraliqdagi sonlar ro'yhatini uzish funktsiyasi"""
#     sonlar = []
#     while max>min:
#         sonlar.append(min)
#         min += qadam
#     return sonlar
# print(oraliq(1, 35, 3))   



# Yuqorudagi afto_info funktsiyasini chaqirib avtomabillar ro'yhatini shakillantiramiz
# def afto_info(kompaniya, model, rangi, korobka, yili, narhi):#Parametrlari bilan funktsiya kiritib olayapmiz
#     """Avtomabil haqidagi ma'lumotlar lug'atini qaytaruvchi funktsiya"""#Funktsiya nomini kiritaypmiz
#     avto = {'kompaniya':kompaniya,
#            'model':model,
#            'rang':rangi,
#            'korobka':korobka,
#            'yil':yili,
#            'narh':narhi}#Lug'at tuzib oldik
#     return avto#Lug'atni funktsiyaga qaytarayapmiz

# print('Saytimizdagi avtomabillar ro\'yhati')
# avtolar = [] #Bo'sh lug'at yaratib olayapmiz
# while True:#Abadiy tsikl
#         print('Quyidagi ma\'lumotlarni kiriting: ', end = ' ')#Habar chiqarayapmiz
#         kompaniya = input('Ishlab chiqaruvch: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
#         model = input('Model: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
#         rangi = input('Rangi: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
#         korobka = input('Korobka: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
#         yili = input('Ishlab chiqarilgan yili: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
#         narhi = input('Narhi: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
#         #afto_info funktsiyasi orqali har bir avtomabil uchun lug'at yaratib bu lug'atni avtolar ro'yhatiga qo'shamiz
#         avtolar.append(afto_info(kompaniya, model, rangi, korobka, yili, narhi))
#         #Yangi avto qo'shish qo'shmaslikni so'raymiz
#         javob = input('Yangi avto qo\'shasizmi? (yes/no) ')#Foydalanuvchidan javob olayapmiz
#         if javob == 'no':#Agar javob no bo'lsa
#             break#tsikl to'xtaydi
# for avto in avtolar:#avto o'zgaruvchisiga avtolar ro'yhatidagi har bir elementni yuklayapmiz
#     print(f"{avto['rang']} {avto['model']}. Narhi: {avto['narh']}$")#Natijani consolga chiqarayapmiz



# AMALIYOT
# 1-MASALA
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# def mijoz_info(ismi, familyasi, t_yili, t_joyi, yoshi, emaili = '', telefoni = None):
#     """Foydalanuvchidan ma'lumotlarni qabul qilib 
#     lug'at ko'rinishida qaytaruvchi funktsiya"""
#     mijoz = {
#                      'ism':ismi,
#                      'familya':familyasi,
#                      't_yil':t_yili, 
#                      't_joy':t_joyi, 
#                      'yosh':yoshi,
#                      'email':emaili,
#                      'telefon':telefoni
#                      }
#     return mijoz

# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar = []
# while True:
#     print("Quyidagi ma'lumotlarni kiriting: ")    
#     ismi = input("Ismingizni kiriting: ")
#     familyasi = input("Familiyangizni kiriting: ")
#     t_joyi = input("Tug'ilgan viloyatingizni kiriting: ")
#     t_yili = int(input("Tug'ilgan yilingizni kiriting: "))
#     yoshi = 2025-t_yili
#     emaili = input("e-mailingizni kiriting: ")
#     telefoni = input("Telefon raqamingizni kiriting: ")
#     mijozlar.append(mijoz_info(ismi, familyasi, t_yili, t_joyi, yoshi, emaili = '', telefoni = None))
#     javob = input("Yana ma'lumot kiritasizmi(ha/yo'q): ")
#     if javob == "yo'q":
#         break
# for mijoz in mijozlar:
#     print(f"\n{mijoz['familya'].title()} {mijoz['ism'].title()}, {mijoz['t_yil']} yil "
#           f"{mijoz['t_joy'].title()} viloyatida tug'ilgan. {mijoz['yosh']} yoshdada.")
    



# 2-masala
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# def kattasini_chiqar(x, y, z):#Funktsiya kiritib olayapmiz
#     """Kiritilgan 3 ta sondan kattasini chiqaruvchi funktsiya"""
#     # print("Uchta son kiriting: ")
#     # x = int(input("x = "))
#     # y = int(input("y = "))
#     # z = int(input("z = "))
#     if x<y and z<y:
#         kattasi = y
#     elif x<z and y<z:
#         kattasi = z
#     else:
#         kattasi = x
#     return kattasi

# kattasi = kattasini_chiqar(5, 6, 9)
# print(kattasi)   



#4-masala
# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
# def info_aylana(radiusi):
#     """Aylananing radiusi orqali u haqida ma'lumotlarni chiqaruvchi funktsiya"""
#     aylana = {
#              'radius':radiusi,
#              'diametr':radiusi*2,
#              'peremetr':2*3.14*radiusi,
#              'yuza':3.14*radiusi**2
#              }
#     return aylana
# print(info_aylana(5))



# 5-masala
# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# def tub_son_top(min, max):#Funktsiya kiritib olayapmiz
#     """Berilgan oraliqdagi tub sonlarni chiqaruvchi funktsiya"""
#     tub_sonlar = []#Tub son deb nomlangan bo'sh ro'yhat kiritib olayapmiz
#     for son in range(min, max+1):#Oraliqdagi sonni har birini son o'zgeruvchisiga yuklayapmiz
#         if son>1:#Agar son 1 dan katta bo'lsa
#             tub = True#Tubga true qiymat berayapmiz
#             for x in range(2, son):#x o'zgaruvchisiga 2 dan songacha bo'zgan sonlarni har birini yuklayapmiz
#                 if son%x==0:#Arar son x ga bo'linsa bu tun son emas
#                     tub = False
#                     break
#             if tub:#Agar tub son mavjud bo'lsa
#                 tub_sonlar.append(son)#sonni tub sonlar ro'yhatiga qo'shayapmiz
#     return tub_sonlar#Tub son;ar ro'yhatini qaytarayapmiz
# print(tub_son_top(12, 100))



#6-masala
# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
def fibonachi(n):#Funktsiya kiritib olayapmiz
    """Kiritilgan sonlar miqtorigacha fibonachi sonlar ketma ketligini chiqarish funktsiyasi"""
    fibonachi_ketmaketlik = []#Ketmaketlik uchun bo'sh ro'yhat yaratib olayapmiz
    for x in range(n):#x ga 0 dan n gacha bo'lgan sonlarni har birini yuklayapmiz
        if x==0 or x==1:#Agar x 0 yoki 1 ga teng bo'lsa 
            fibonachi_ketmaketlik.append(1)#ro'yhatga 1 ni qo'shayapmiz
        else:#Aks holda ya'ni x 1 dan katta bo'lsa 
            fibonachi_ketmaketlik.append(fibonachi_ketmaketlik[x-1]+fibonachi_ketmaketlik[x-2])
    return fibonachi_ketmaketlik#Fibonachi ketma ketligi ro'yhatini qaytarayapmiz
print(fibonachi(25))#0 dan 25 gacha oraliqdai fibonachi ketma ketligini qaytaradi
            