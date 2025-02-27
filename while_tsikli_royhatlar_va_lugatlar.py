# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:47:40 2025

MAVZU:whle tsikli ro'yhatlar va lug'atlar

@author: MAMADIYEV FAXRIDDIN
"""

#Ro'yhatlar(lug'atlar) bilan ishlashda while tsiklining foydalari juda ko'p
#Misol uchun foydalanuvchidan bir nechta qiymatlarni qabul qilish
#Ro'yhatdan takrorlanuvchi qiymarlarni o'chirish
#Ro'yhat elementlarini boshqa ro'yhatga ko'chirish va hokazo


#WHILE TSIKILI YORDAMIDA RO'YHATNI TO'LDIRISH
#Quyida foydalanuvchi do'stlari ro'yhatini tuzamiz

# ismlar = []#Do'stlr ro'yhati orqali to'ldirilishi uchun bo'sh ro'yhat yaratib olayapmiz
# n = 1#Do'stlar soni uchun n ga 1 qiymat berayapmiz
# while True:
#    savol = f'{n}-do\'stingiz ismini kiriting: \n'#Foydalanuvchidan yo'stini ismini kiritishini so'rayapmiz
#    ism = input(savol)#Savol o'zgaruvchisini savolga o'tkayapmiz
#    ismlar.append(ism)#ismlar ro'yhatiga foynalanuvchi kiritgan ismni qo'shib olayapmiz
#    javob = input('Yana ism kiritasizmi(ha/yo\'q): ')#Foyda;anuvchidan yana ism kiritish yoki kiritmasligini so'rayapmiz
#    if javob == 'ha':#Agar javob ha bo'lsa
#        n += 1#songa bir qo'shayapmiz
#        continue#va tsikl bishiga o'tib ikkinchi do'stini ismini so'rayapmiz
#    else:#Aks holda ya'ni javob ha bo'lmasa tsiklni to'xtatayapmiz
#        break
# print('\nSizming do\'stlaringiz: ')#Habar chiqarayapmiz
# for ism in ismlar:#Foydalanuvchi kiritgan do'stlari ro'yhatidagi jar bir elementni ism o'zgaruvchisiga yuklayapmiz
#     print(ism.title())#Foydalanuvchi do'stlarini consolga chiqarayapmiz
    


#While tsikli yordamid lug'atlarni ham shakillantirish mumkun
#Quida foydalanuvchidan do'stinging ismini va yoshini so'raymiz
#Foydalanuvchi kiritgan ismni lug'at kaliti yoshni esa lug'at qiymati sifatida saqlaymiz
# print('Do\'stlaringiz yoshini saqlaymiz: ')
# dostlar = {}#Do'stlar nomli bo'sh ro'yhat yaratib olayapmiz
# ishora = True#Ishora o'zgaruvchisiga True qiymat berdik
# while ishora:#Abadiy tsikl yaratayapmiz
#       ism = input('Do\'stingiz ismini kiriting: \n')#Foydalanuvchi do'stini ismini so'rayapmiz
#       yosh = input(f'{ism.title()}ning yoshini kiriting: \n')#Kiritilgan do'st yoshini so'rayapmiz
#       dostlar[ism] = int(yosh)#Kiritilgan ismni ro'yhatning kaliti yoshni qiymati sifatida saqlayapmiz
#       javob = input('Yana ism kiritasizmi(ha/yo\'q): ')#Foydalanuvchidan yana ism kiritadimi yo'qmi so'rayapmiz
#       if javob == 'yo\'q':#Agar javob yo'q bo'lsa 
#           ishora = False#Ishoraga False qiymat beryapmiz va tsiklni to'xtatayapmiz
# for ism, yosh in dostlar.items():#To'dirilgan lug'atni kalit va qiymatini ism va yosh o'zgaruvchilariga yuklayapmiz
#     print(f'{ism.title()} {yosh} da.')#Natijani consolga chiqarayapmiz
      

#While tsikli yordamida ro'yhat elementini o'chirish
#Biz avvalgi darslarimizda ro'yhat elementlarini o'chirish uchun remove(qiymat) metodidan foydalangan edik
#Remove metodi ro'yhatda biror qiymat bir necha marta takrorlamgan bo'lsa faqat birinchi uchraganini o'chiradi
#Ro'yhatda takrorlangan qiymatlarni barchasini o'chirish uchun while tsiklidan foydalanishimiz mumkun

# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# #Yuqoridagi ro'yhatimizda 'nexia' elementi 3 marta takrorlangan
# #While tsikli yordamida bu elementni hammasini ro'yhatdan o'chirib tashlaymiz
# while 'nexia' in cars:#cars ro'yhatida toki nexia elementi bor ekan
#     cars.remove('nexia')#Bu ro'yhatdan nexia elementini o'chirayapmiz
# print(cars)#Nexia elementi 'chirilgan ro'yhatni consolga chiqarayapiz



#Bazi hollarda ro'yhat elementlarini oxirigaxha boshqa ro'yhatga ko'chirishga to'g'ri kelishi mumkun
#Bunday holatlarda bizga whiletsikli qo' keladi
#Bizga talabalar ro'yhati berilhgan bo'lsin, 
#Bu ro'yhatdagi talabalar ismini pop() metodi yordamida sug'urib oldik va uning bahosini so'radik
#talabaning ismini lug'at kaliti uning bahosini qiymati sifatida saqlab qo'yfik

# talabalar = ['hasan', 'husan', 'olim', 'botir']#Talabalar ro'yhati
# baholangat_talabalar = {}#Bosh lug'at
# while talabalar:#Toki talabalar ro'yhatida element bor ekan
#       talaba = talabalar.pop()#Talaba nomli o'zgaruvchiga ro'yhatning oxirisidagi qiymatni yuklayapmiz
#       baho = input(f'{talaba.title()}ning bahosini kiriting: ')
#       print(f'{talaba.title()} baholandi.')
#       baholangat_talabalar[talaba] = baho
# for talaba, baho in baholangat_talabalar.items():
#     print(f'\n{talaba.title()}ning bahosi: {baho}')



#AMALIYOT
#1-MASALA
#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

# mahsulotlar = []#Mahsulotlar nomli bo'sh ro'yhat
# n = 1#Buyurtma tartib raqamiga 1 qiymat berayapmiz
# while True:
#     buyurtma = f'{n}-buyurtmangizni kiriting:\n'
#     savol = input(buyurtma)
#     mahsulotlar.append(savol)
#     javob = input('Yana buyurtma berasizmi(ha/yo\'q):\n')
#     if javob == 'ha':
#         n += 1
#     else:
#         break
# print('Siz quyidagi mahsulotlarni buyurtma qildingiz: ')
# for buyurtma in mahsulotlar:
#     print(buyurtma.title())

#2-MASALA
#e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# e_bozor = {}
# ishora = True
# while ishora:
#     buyurtma = input('Buyurtmangizni kiriting:\n')
#     narh = input(f'{buyurtma}ning narhini kiriting:\n')
#     e_bozor[buyurtma] = int(narh)
#     javob = input('Yana buyurtma kiritasizmi(ha/yo\'q)? \n')
#     if javob != 'ha':
#         break
# print('Sizning muyurtmaniz va ularning narhlari: ')
# for buyurtma, narh in e_bozor.items():
#     print(f'{buyurtma.title()}ning narhi {narh} so\'m.')

#Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating
buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}
while buyurtmalar:#Toki buyurtmalar ro'oyhatida element bor akan
      buyurtma = buyurtmalar.pop()
      if buyurtma in mahsulotlar.keys():
          narh = mahsulotlar[buyurtma]
          print(f'{buyurtma.title()}ning narhi: {narh} so\'m.')
      else:
          print(f'Kechirasiz bizda {buyurtma} yo\'q.')
    
    
    
    
    


