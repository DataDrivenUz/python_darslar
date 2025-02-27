# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Biz lug'atlar bi;an ishlaganimizda ulardagi kalit so'zlar orqali ularni elementlariga murojat qilishni ko'ril
#Bazi hollarda lug'atimiz katta bo'lib undagi hamma kalit so'zlarni ilmasligimiz mumkun
#Bunday hollarda lug'atdagi kuftliklarni items() metodi yordamida chiqarib olshimiz mmkun
#Quyidagi misoln ko'raylik
# malumot={'ism':'Faxriddin',
#          't_joy':'Surhondaryo viloyati',
#          't_yil':'1995',
#          'daraja':'magistr',
#          'ish_joy':'Ingo-Uzbekstan'}
# print(malumot.items())#Lug'atdagi kalit va elementlar juftligini chiqaradi

#Lug'atlardagi juftliklarni bunday holatda chiqarish har doim ham qulay bo'layvermaydi
#Juftliklarni tushunarli tarzda ishodalash uchun for siklidan foydalanamz

# for kalit, qiymat in malumot.items():#lug'atdaggi kalit so'zlarni kalitga qiymatlarni qiymatga yuklayapmiz
#     print(f'Kalit: {kalit}')
#     print(f'Qiymat: {qiymat}\n')
#Biz for siklidagi kalit va qiymat o'rniga ixtiyoriy qiymat berishimiz mumkun

#Yana mir misol ko'raylik
# telefon={'ali':'iphone 15 Pro',
#          'vali':'galaxy S23+',
#          'anvar':'redmi Not 11',
#          'faxriddin':'honor X7b',
#          'hurshid':'galaxy a12'}
# #For sikli yordamida yuqoridagi lug'atdagi kalit va qiymatni ixtiyoriy o'zgaruvchiga yuklaymiz
# for t, q in telefon.items():
#     print(f'{t.title()} ning telefoni {q.upper()}\n')#Har bir kalit va qiymatga moz matin chiqarayapmiz



#Agar bizga lug'atdagi kalit so'zlar kerak bo'ladigan bo'lsa keys() metodidan foydalanamiz
#Bir misol ko'raylik
# mahsulotlar = {
#     'olma':10000,
#     'nok':25000,
#     'uzum':30000,
#     'shaftoli':35000,
#     'banan':20000
#     }
#Lug'atdagi kalitso'zlarni kranga chiqaramiz
# print('Do\'konda bor mahsulotlar:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())
    
#if va for metodlari yordamida bozorlik nomli ro'yhat tuzib unda bor elementlar do'konda bor bo'lsa ularni narhi bilan chiqaramiz
# bozorlik=['non', 'shakar', 'olma', 'banan']#Bozorlik ro'yhatini tuzib layapmiz
# for mahsulot in mahsulotlar:#mahsulot o'zgaruvchisiga mahsulotlar ro'yhatidagi elemetlarni har birini yukalyapmiz
#     if mahsulot in bozorlik:#Agar mahsulot bozorlik ro'yhatining ichida bor bo'lsa
#        #Ekranga mahsulotning narhi nilan chiqarayapmiz
#        print(f'{mahsulot.title()}ning narhi {mahsulotlar[mahsulot]} so\'m')
       
#Agar bozorlik ro'yhatidagi melement mahsulotlar ichida bo'lmasa habar chiqaramiz
#Bozorlik ro'yhatidagi her bir elementni buyib nomli o'zgaruvchiga yulaymiz


#Bazi hollarda lug'at elementlarini tartiblashga to'gri kelishi mumkun
#Bunday hollarda biz sorted() metodidan foydalanamiz
#Yuqoridagi mahsulotlar lug'ti misolida ko'ramiz
# mahsulotlar = {
#     'olma':10000,
#     'nok':25000,
#     'uzum':30000,
#     'shaftoli':35000,
#     'banan':20000
#     }
# print('Do\'konimizda quyidagi mahsulotlar mavjud:\n')
# for mahsulot in sorted(mahsulotlar):#Mahsulotlar nomli lug'at elementlarini tartiblab har birini mahsulot nomli o'zgaruvchiga yuklayapmiz
#     print(mahsulot.title())
#Bu usulmizda asil ro'yhatimiz o'zgarmaydi.

#Biz yuqoridagi misollarda lug'atning kalitlari bilan ishladik
#Bazi hollarda lug'atning qiymatlari bilan ishlashga to'g'ri kelishi mumkun
#Bunday hollarda biz values() metodi yordamida lug'atning qiymatlariga murojat qilamiz
#Bizga telefonlar nomli ug'at berilgan bo'lsin
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }
#Bu lug'atimizdan faqat qiymatlarni uyidagi terzda chiqaramiz
# print('Foydalanuvchilar quyidagi telefonlarni ishlatadi:')
# for tel in telefonlar.values():#Telefonlar nomli lug'atning har bir qiymatni tel nomli o'zgaruvchiga yuklayapmiz
#     print(tel.title())#Lug'at qiymatlarini chiqarayapmiz
    
#Yuqoridagi usulimizni kamchiligi shundagi qiymatlar mir necha marta takrorlangan bo'lsa ularning barchasini ekranga chiqaradi
#Buni bartaraf etish uchun ya'ni takrorlangan elementlarni bir marta chiqarish uchun set() metodidan foydalanamiz
#Telefonlar lug'atinging har bi qiymatini takrorlanishlarsiz tel nomli o'zgaruvchiga yuklayapmiz
# for tel in set(telefonlar.values()):
#     print(tel.title())
#Bu usul yordamida takrorlangan qiymatlarning faqat bittasigina chiqadi


#Pythonda set yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta elementlarni saqlashga mo'ljallangan. Lug'at va ro'yxatdan farqli ravishda, set ichidagi elementlar biror tartibda saqlanmaydi, va ularga indeks orqali murojat qilib bo'lmaydi. Shuningdek, set ichida bir hil elementlar bo'lmayd


#AMALIYOT
#1-MASALA
#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
# lugat = {
#         'boolen':'mantiqiy ifoda',
#         'float':'o\'nlik son',
#         'integer':'buton son',
#         'if':'shart tekshirish operatori',
#         'input':'kiritish operatori',
#         'print':'chiqarish operatori',
#         'for':'tarmoqlanish operatori',
#         'upper':'katta harfda',
#         'lower':'kichik harifda',
#         'title':'Birinchi harfi katta',
#         'capitalize':'matinning birinchi so\'zi bosh harfi katta',
#         'sorted':'alfabet tartibida tartiblash',
#         'reverse':'aylantirish',
#         'items':'lugatdagi juftliklarni chiqarish',
#         'keys':'lugatdagi kalit sozlarga murojat qilish',
#         'values':'lugatdagi qiymatlarga murojat qilish',
#         'tuple':'ozgarmas royhat',
#         'rabge':'oraliq'
#         }
# #Lugatdagi kalit va qiymatlarni for sikli yordamida ikkita yang o'zgaruvchiga yklaymiz
# print('Lug\'at elementlari')
# for k, q in sorted(lugat.items()):
#     print(f'{k}-{q}\n')


#2-MASALA
# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
# davlatlar={'aqsh':'washington',
#            'italiya':'rim',
#            'malayzia':'kualalampur',
#            'tojikiston':'Dushanbe',
#            'qozo\'iston':'ostona',
#            'afg\'oniston':'kobul',
#            'hindisto':'dehli',
#            'turkiya':'istanbul',
#            'o\'zbekiston':'toshkent',
#            'qirg\'iziston':'bishkek'
#            }    
# #for sikli yordamida lug'atdagi kalit va qiymatlarni ikkita o'zgaruvchiga yuklaymiz
# print('Dunyo davlatlari:')
# for k in sorted(davlatlar.keys()):
#     print(k.upper())

# print('\nDavlatlarning poytahtlari:')
# for q in sorted(davlatlar.values()):
#     print(q.title())

# country = input('Qaysi davlatni poytahtini bilishni hohlaysiz: ').lower()
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz bu davlat haqida bizda ma\'lumot yo\'q')
# else:
#     print(f'{country.upper()} davlatining poytahti {capital.title()}')


#3-MASALA
#Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
menyu = {
        'osh':30000,
        'shorva':25000,
        'somsa':8000,
        'xonim':6000,
        'non':4000,
        'shashlik':15000,
        'lag\'mon':20000,
        'bishteks':25000,
        'tushonka':35000,
        'qozonkabob':38000,
        'salat':10000
         }
print('3 ta taom buyurtma qiling; ')
bir = input('1-taom: \n').lower()
ikki = input('2-taom: \n').lower()
uch = input('3-taom: \n').lower()
buyurtma = [bir, ikki, uch]
# print(buyurtma)

for taom in menyu:
    if taom in buyurtma:
       print(f'{taom.title()} {menyu[taom]}')
  
for zakaz in buyurtma:
    if zakaz not in menyu:
        print(f'Kechirasiz bizda {zakaz} yo\'q')
