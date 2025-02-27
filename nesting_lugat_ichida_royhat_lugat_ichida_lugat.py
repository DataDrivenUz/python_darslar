# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:34:19 2025

MAVZU: NESTING LUGAT ICHIDA O'YHAT LUGAT ICHIDA LUG'AT

@author: 123
"""

#Biz avvalgi darslarda talaba ma'lumotlaridan ro'yhat tuzdik va uning ustida turli amallar bajardik
#Bunday talabalar lug'atidan yuzlab bo'lishi mumkun 
#Bunday hollarda bu lug'atlarni bitta ro'yhatga jamlab ular ustida amallar bajarish mumkun

#LUG'ATLAR RO'YHATI
#Biz misol ko'raylik
car_0 = {
        'model':'laseti',
        'rang':'oq',
        'yil':2020,
        'narh':10000,
        'brobeg':'avtomat'
         }

car_1 = {
        'model':'nexia-3',
        'rang':'seriy',
        'yil':2021,
        'narh':12000,
        'brobeg':'mehanika'
        }

car_2 = {
        'model':'cobalt',
        'rang':'qora',
        'yil':2018,
        'narh':11000,
        'brobeg':'mehanika'
        }

#Agar biz lug'atimizga alohida murojat qiladigan bo'lsak har bir lug'at nomini eslab qolishimiz kerak
#Har bir lug'atga murojatqilamiz
# car = car_0
# print(f'{car["model"].title()},\
#   {car["rang"]} rang, {car["yil"]}-yil,\
#   {car["narh"]}$')
  
# car = car_1
# print(f'{car["model"].title()},\
#   {car["rang"]} rang, {car["yil"]}-yil,\
#   {car["narh"]}$')
  
# car = car_2
# print(f'{car["model"].title()},\
#   {car["rang"]} rang, {car["yil"]}-yil,\
#   {car["narh"]}$')

#Ko'rib turganimizdek bir nechta lug'atga bu usulda murojat qilishimiz qiyinchilik tug'duradi
#Buning o'rniga lug'atlarni bitta ro'yhatga jamlab for sikli yordamida unga murojat qilsak osonroq bo'ladi

#Masalan
# cars = [car_0, car_1, car_2]#Lugatlar ro'yhatini tuzib olayapmiz
# for car in cars:#Ro'yhatdagi har bir elementni car o'zgaruvchisiga yuklayapmiz
#     print(f'{car["model"].title()},\
#     {car["rang"]} rang, {car["yil"]}-yil,\
#     {car["narh"]}$')
#Ikkala usulda ham bir hil natija chiqadi
#Lekin ikkinchi usulimiz bir muncha ishimizni osonlashtiradi

#Biz yuqoridagi ro'yhatimizdan har bir lug'atga ham murojat qilishimiz mumkun
# print(cars[0])

#Lug'atimiz ichidagi elementga esa quyidagi tarzda murojat qilishimiz mumkun
# print(cars[2]['model'])


#for tsikli yordamida bo'sh ro'yhat yaratib uni to'ldirishimiz mumkun
# malibus = []#Bo'sh ro'yhat yaratib olayapmiz
# for n in range(10):#n 0 da 10 gacha qiymat qabul qiladi
#       new_car = {
#                'mode':'malibu',
#                'rang':'none',
#                'yil':2020,
#                'narh':'none',
#                'km':0,
#                'korobka':'avto'
#                }
#       malibus.append(new_car)
# print(malibus)
#Yuqoridagi misolimizda bo'sh ro'yhat yaratdik ve unga 10 ta new_car nimli lug'atni element qilib qo'shib oldik

#Endi birinchi uchta malibuni rangini oq qilamiz
# for malibu in malibus[:3]:
#     malibu['rang']='qora'
#     malibu['narh']=40000
# # print(malibus)

#Keyingi uchtasini qizil qilamiz va karobkasini mehanika qilamiz
# for malibu in malibus[3:6]:
#     malibu['rang']='oq'
#     malibu['korobka']='mehanika'
# print(malibus)

#Qolganini seriy qilamiz
# for malibu in malibus[6:]:
#     malibu['rang']='kulrang'
# print(malibus)

#Endi quyidagi shartlar orqali narh qo'yamiz
# for malibu in malibus:
#     #Agar malibuning rangi qora va korobka avt bo'lsa uning narhi 40000$
#     if malibu['rang']=='qora' and malibu['korobka']=='avto':
#         malibu['narh']=40000
#         #Agar malibuning rangi oq yoki kulrang va korobka avto bo'lsa 38000$
#     if (malibu['rang']=='oq' or malibu['rang']=='kulrang') and malibu['korobka']=='avto':
#         malibu['narh']=38000
#         #Aks holda
#     else:
#         malibu['narh']=35000
# print(malibus)



#LUG'AT ICHIDA RO'YHAT
#Bazi hollarda lug'atdagi kalit qiymatlari bir nechta bo'lishi mumkun
#Bunday hollarda qiymatlar birra ro'yhatga olinib ularga murojat qilinadi
#Quyida bir nechta ishchining ismini lug'at kalitiga
#Ular biladigan dasturlash tillarini bitta yo'yhatga kiritib qiymat sifatida qabul qilib murojat qilamiz
# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }
#Lugat elementlarini ism va tillar o'zgaruvchilariga yuklaymiz va ularni ekranga chiqaramiz
# for ism, tillar in dasturchilar.items():
#     print(f'\n{ism.title()} ning biladigan dasturlash tillari: ')
#     for til in tillar:#til o'zgaruvchisiga tillar yani lug'at qiymati elementlarin yuklayapmiz
#         print(til.upper())
        
#Ko'rib turganimizdek print funksiyasi keyingi habarni pastki qatorga tushurib yuborayapdi
#Buni bartaraf qilish uchun yani matinlarni bir qatorga chiqaridh uchun print ichidagi amaldan kelin end = '' ifodani qo'yishimiz kerak
# for ism, tillar in dasturchilar.items():
#     print(f'\n{ism.title()} ning biladigan dasturlash tillari: ', end = ' ')
#     for til in tillar:#til o'zgaruvchisiga tillar yani lug'at qiymati elementlarin yuklayapmiz
#         print(til.upper(), end = ' ')
#Ko'rib turganimzdek barcha stringlar bitta qatorga joylashdi


#LUG'AT ICHIDA LUG'AT
#Lug'at ichida lug'at kiritib ishlash tavsiya qilinmasada bazi hollarda qo'l kelishi mumkun
#Masalan hamkasblarni isimlarini lug'at kaliti sifatida ular haqidagi ma'lumotlarni lug'at qiymati sifatida kiritishga to'g'ri kelishi mumkun
# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }
# #Bu lug'atimizdagi kaltlarni yani ismlarni ism o'zgaruvchisiga
# #Qiymatlarni ya'ni malumotlar lug'atini info o'zgatuvchisiga yuklaymiz
# for ism, info in hamkasblar.items():
#     print(f"\n\n{ism.title()} {info['familiya'].title()} " 
#           f'{info["tyil"]}-yilda tug\'ilgan. '
#           f'{info["malumot"]} ma\'lumotli. '
#           f'Biladogan dasturlash tillari: ', end = ' ')
#     for til in info['tillar']:#Biladigan tillarini til o'zgaruvchisiga yuklayapmiz
#         print(til.upper(), end = ' ')




#AMALIYOT
#1.Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
adib_0 = {
         'ism':'lev tolstoy',
          'tyil':1828,
          'vyil':1910,
          'tjoy':'rossiya',
          'asarlar':['urush va tinchlik', 'anna karenina', 'bolalik', 'ivan ilichning o\'limi']
          }

adib_1 = {
         'ism':'albert enshteyn',
          'tyil':1879,
          'vyil':1955,
          'tjoy':'germaniya',
          'asarlar':['mahsus nisbiylik nazariyasi', 'fotoeffekt tushuntirish', 'umumiy nisbiylik nazariyasi']
          
          }

adib_2 = {
         'ism':'leanardo davinchi',
          'tyil':1452,
          'vyil':1519,
          'tjoy':'anglya',
          'asarlar':['mono liza', 'oxirgi kechlik', 'vitruviy odam']
          }

adib_3 = {
         'ism':'alisher navoiy',
          'tyil':1411,
          'vyil':1501,
          'tjoy':'o\'zbekiston',
          'asarlar':['sheriy devonalari', 'xamsa', 'muhokamat ul-lug\'atayin', 'mahbub ul-qulb']
          }
#Lug'atlarni bitta ro'yhatga joylaymiz
adib = [adib_0, adib_1, adib_2, adib_3]
# print(adib)
#Consolga chiqarish
# for shaxs in adib:
#     print(f'\n{shaxs['ism'].title()}, {shaxs['tyil']}-yilda, {shaxs["tjoy"].title()}da tug\'ilgan.'
#           f'{shaxs["vyil"]}-yilda olamdan o\'tgan ')

#2.Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
# for shaxs in adib:
#     print(f'\n\n{shaxs['ism'].title()}ning asarlari: ')
#     for asar in shaxs['asarlar']:
#         print(asar.capitalize())


#3.Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. Natijani konsolga chiqaring.
# yaqinlar = {
#             'ali':['qashqirlar makoni', 'shaytanat', 'cho\'qintirgan ota'],
#             'vali':['biz yolg\'iz emasmiz', 'tundan tongacha', 'janob hechkim'],
#             'husan':['doktor haus', 'alovuddin', 'qasos'],
#             'rustam':['uol strit bo\'risi', 'savdo san\'ati']
#            }
# for ism, kinolar in yaqinlar.items():
#     print(f'\n{ism.title()} ning sevimli kinolari: ')
#     for kino in kinolar:
#         print(kino.capitalize())


#4.Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.
davlatlar = {
             'aqsh':{
                     'poytahti':'vashington',
                     'hududi':'9.8 mln km kvadrat',
                     'aholisi':'332 mln kishi',
                     'rasmiy tili':'ingliz tili',
                     'pul birligi':'usd'},
             'xitoy':{
                     'poytahti':'pekin',
                     'hududi':'9.6 mln km kvadrat',
                     'aholisi':'1.4 mlrd kishi',
                     'rasmiy tili':'xitoy tili',
                     'pul birligi':'yuang'},
             'germaniya':{
                     'poytahti':'berlin',
                     'hududi':'357 ming km kvadrat',
                     'aholisi':'84 mln kishi',
                     'rasmiy tili':'nemis tili',
                     'pul birligi':'eur'},
             'yaponiya':{
                     'poytahti':'tokio',
                     'hududi':'377 ming km kvadrat',
                     'aholisi':'125 mln kishi',
                     'rasmiy tili':'yapon tili',
                     'pul birligi':'jpy'},
             'brazilya':{
                     'poytahti':'brazilya',
                     'hududi':'8.5 mln km kvadrat',
                     'aholisi':'216 mln kishi',
                     'rasmiy tili':'portugal tili',
                     'pul birligi':'brl'},
            }

for davlat, info in davlatlar.items():
    if davlat.lower()=='aqsh':
        davlat=davlat.upper()
    else:
        davlat=davlat.capitalize()
    # print(f'\n{davlat.title()} davlatining poytahti: {info['poytahti'].title()} shahri. '
    #       f'\nHudui: {info['hududi']} . \nAholisi {info['aholisi']}. '
    #       f'\nTili {info['rasmiy tili']}. \nPul birligi {info['pul birligi'].upper()}')
    
#Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
davlatlar = {
             'aqsh':{
                     'poytahti':'vashington',
                     'hududi':'9.8 mln km kvadrat',
                     'aholisi':'332 mln kishi',
                     'rasmiy tili':'ingliz tili',
                     'pul birligi':'usd'},
             'xitoy':{
                     'poytahti':'pekin',
                     'hududi':'9.6 mln km kvadrat',
                     'aholisi':'1.4 mlrd kishi',
                     'rasmiy tili':'xitoy tili',
                     'pul birligi':'yuang'},
             'germaniya':{
                     'poytahti':'berlin',
                     'hududi':'357 ming km kvadrat',
                     'aholisi':'84 mln kishi',
                     'rasmiy tili':'nemis tili',
                     'pul birligi':'eur'},
             'yaponiya':{
                     'poytahti':'tokio',
                     'hududi':'377 ming km kvadrat',
                     'aholisi':'125 mln kishi',
                     'rasmiy tili':'yapon tili',
                     'pul birligi':'jpy'},
             'brazilya':{
                     'poytahti':'brazilya',
                     'hududi':'8.5 mln km kvadrat',
                     'aholisi':'216 mln kishi',
                     'rasmiy tili':'portugal tili',
                     'pul birligi':'brl'},
            }

davlat = input('Qaysi davlat haqida ma\'lumot olishni hohlaysiz: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f'\n{davlat.title()} davlatining poytahti: {info['poytahti'].title()} shahri. '
          f'\nHudui: {info['hududi']} . \nAholisi {info['aholisi']}. '
          f'\nTili {info['rasmiy tili']}. \nPul birligi {info['pul birligi'].upper()}')
else:
    print('Kechirasiz bu davlat haqida bizda ma\'lumot yo\'q.')
    

    
    
