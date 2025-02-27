# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:36:28 2025

@author: 123
"""

# 1. Boshlang‘ich daraja:
# 1.1 For tsikli va shart operatori
# Masala:
# Foydalanuvchidan N sonini kiriting va 1 dan N gacha bo‘lgan sonlarning kvadratlarini chiqaradigan dastur yozing. Faqatgina juft sonlarni ekranga chiqaring.
# son = int(input('Biror son kiriting: \n'))
# sonlar = range(1, son+1)
# for raqam in sonlar:
#     if (raqam > 0 and raqam%2==0) :
#         print(f'{raqam}ning kvadrati {raqam**2} ga teng')
    



# 1.2 Ro‘yxatlar (List)
# Masala:
# Foydalanuvchidan 5 ta son kiritishini so‘rang va ularni ro‘yxatga saqlang. Keyin, ushbu ro‘yxatdagi eng katta va eng kichik sonni ekranga chiqaring.
# sonlar = []
# n = range(5)
# for n in range(5):
#     raqam = int(input(f'{n+1}-raqamni kiriting: '))
#     sonlar.append(raqam)
# print(sonlar)
# print(f'Eng katta raqam {max(sonlar)} ')
# print(f'Eng kichik raqam {min(sonlar)}. ')
# print(f'Barcha sonlar yig\'indisi {sum(sonlar)} ')
    
# 1.3 Lug‘atlar (Dictionary)
# Masala:
# Quyidagi lug‘at berilgan:
# Foydalanuvchidan meva nomini so‘rab, agar lug‘atda bo‘lsa, uning narxini chiqaring. Agar lug‘atda mavjud bo‘lmasa, "Kechirasiz, bu meva bizda yo‘q." degan xabar chiqaring.
# mevalar = {"olma": 5000, "banan": 18000, "gilos": 25000, "nok": 8000}
# meva = input('Biror meva nomimi kiriting: ').lower()
# if meva in mevalar.keys():
#     narh = mevalar[meva]
#     print(f'{meva.title()}ning narhi {narh} so\'m.')
# else:
#     print(f'Kechirasiz bizda {meva.title()} yo\'q.')



# 1.4 While tsikli
# Masala:
# Foydalanuvchidan son kiritishini so‘rang. Agar son musbat bo‘lsa, dastur ushbu sonning kvadrat ildizini chiqaradi. Agar manfiy son kiritsa, dastur tugaydi.
# while True:
#     son = int(input('Biror son kiriting: '))
#     if son < 0:
#        break
#     print(f'{son}ning kvadrati {son**2} ga teng')

# 2. O‘rta daraja:
# 2.1 For tsikli + Ro‘yxatlar
# Masala:
# Foydalanuvchidan 10 ta son kiritishini so‘rang va ro‘yxatga saqlang. Keyin, ro‘yxatdagi barcha toq sonlarni yangi ro‘yxatga ajratib chiqaring.
# sonlar = []
# toq_son = []
# for n in range(10):
#     raqam = int(input(f'{n+1}-sonni kiriting: '))
#     sonlar.append(raqam)
#     if raqam%2!=0:
#        toq_son.append(raqam)
# print(sonlar)
# print(toq_son)


# 2.2 While tsikli + Lug‘at
# Masala:
# Dastur "login tizimi" sifatida ishlasin. Lug‘atda mavjud foydalanuvchilar va ularning parollari bor:
# Foydalanuvchidan login va parol so‘rang. Agar to‘g‘ri kiritsa, "Xush kelibsiz!" deb chiqaring, aks holda, "Login yoki parol xato" deb qayta urinishga imkon bering. Uch marta xato kiritsa, dastur tugasin.
# foydalanuvchilar = {"ali": "1234", "vali": "5678", "salim": "abcd"}
# urunishlar = 3
# while urunishlar > 0:
#     login = input('Loginni kiriting: ')
#     parol = input('Parolni kiriting: ')
#     if login in foydalanuvchilar and foydalanuvchilar[login]==parol:
#         print('Xush kelibsiz!')
#         break
#     else:
#         urunishlar -= 1
#         print(f'Login yoki parol xato. Qolgan urunishlar soni {urunishlar} ta.')
#     if urunishlar == 0:
#         print('Siz 3 marta xato login yoki parol kiritdingiz. Dastur tugadi!')




# 2.3 For tsikli + Lug‘atlar
# Masala:
# Quyidagi lug‘at berilgan:
# Har bir talabaning bahosini tekshirib, "Yaxshi o‘quvchi" deb ataladigan talabalarni alohida ro‘yxatga joylashtiring. "Yaxshi o‘quvchi" bo‘lish uchun balli 80 dan yuqori bo‘lishi kerak.
# studentlar = {"Ali": 78, "Vali": 90, "Salim": 56, "Dilfuza": 88}
# yaxshi_oquvchi = []
# for talaba, baho in studentlar.items():
#     print(f'{talaba}ning olgan bali: {baho} ball')
#     if baho > 80:
#        yaxshi_oquvchi.append(talaba)
# print('Alo baho olgan o\'quvchilar:')
# for alo in yaxshi_oquvchi:
#     print(alo)
# # print(yaxshi_oquvchi)




# 3. Murakkab daraja:
# 3.1 While tsikli + Ro‘yxat + Shart operatorlari
# Masala:
# Dastur do‘konning savdo tizimi sifatida ishlasin. Foydalanuvchi har safar mahsulot nomini kiritadi va uning narxini ham yozadi. Barcha kiritilgan mahsulotlar va narxlar ro‘yxatga joylanadi.
# Agar foydalanuvchi "stop" deb yozsa, dastur to‘xtaydi va barcha xarid qilingan mahsulotlarning umumiy summasini chiqaradi.
# Agar mahsulot oldin kiritilgan bo‘lsa, foydalanuvchiga "Bu mahsulot allaqachon kiritilgan!" deb xabar beriladi.
# mahsulotlar = {}
# while True:
#     mahsulot = input('Mahsulot nomini kiriting(dasturni to\'htatish uchun "stop" deb yozing): ').lower()
#     if mahsulot == "stop":
#         print('Dastur tugadi.')
#         break
#     if mahsulot in mahsulotlar:
#         print('Bu mahsulot allaqachon ro\'yhatda bor.')
#         continue
#     narh = float(input(f'{mahsulot.title()} ning narhini kiriting: '))
#     mahsulotlar[mahsulot] = narh
# print(f'\nHarid uchun jami {sum(mahsulotlar.values())} so\'m ketdi.')
# print('\nHarid qilingan mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())


# 3.2 For tsikli + Ro‘yxatlar + Lug‘atlar
# Masala:
# Maktabda 5 ta sinf bor va har bir sinfda 3 tadan o‘quvchi mavjud. Quyidagi lug‘at shaklida o‘quvchilar va ularning baholari keltirilgan:
# maktab = {
#     "5A": {"Ali": 89, "Vali": 78, "Karim": 56},
#     "6B": {"Salim": 45, "Dilfuza": 99, "Gulnoza": 78},
#     "7C": {"Nodir": 100, "Jasur": 67, "Madina": 88},
#     "8D": {"Shoxrux": 56, "Diyor": 76, "Malika": 91},
#     "9E": {"Zarina": 87, "Kamola": 69, "Olim": 80}
# }
# # Dastur eng yaxshi o‘quvchini topishi kerak:
# # Har bir sinfdagi eng yuqori bahoga ega o‘quvchini aniqlash.
# # Umuman olganda, eng yaxshi bahoga ega bo‘lgan o‘quvchini topish.
# eng_yaxshi_sinf = {}
# eng_yaxshi_oquvchi = {}
# for sinf, info in maktab.items():
#     print(f'\n{sinf} ichida eng yaxshi o\'quvchi: ')
#     for oquvchi, baho in info.items():
#         eng_yaxshi_oquvchi[oquvchi] = int(baho)
#         eng_yaxshi = max(info, key=oquvchi)
        
        
   
    


# 3.3 While tsikli + For tsikli + Lug‘atlar
# Masala:
# Bankda mijozlar va ularning hisob raqamlaridagi pullar bor. Lug‘at ko‘rinishida berilgan:
# Dastur foydalanuvchidan ismni so‘raydi va quyidagi amallarni bajarish imkonini beradi:
# "1" ni bossangiz – hisobdagi pulni ko‘rish.
# "2" ni bossangiz – hisobga pul qo‘shish.
# "3" ni bossangiz – hisobdan pul yechish. Agar balans yetarli bo‘lmasa, "Balans yetarli emas!" deb xabar chiqarish.
# "0" ni bossangiz – dastur to‘xtaydi.


# hisoblar = {"Ali": 100000, "Vali": 50000, "Hasan": 75000}

# habar = 'Operatsiyalardan birini tanlang:\n'
# habar += '#1 - hisobdagi pulni ko\'rish.\n'
# habar += '#2 - hisobga pul qo\'shish.\n'
# habar += '#3 - hisobdan pul yechish.\n'
# habar += '#0 - dastur to\'xtaydi.\n'

# print(habar)#Habarni chiqarayapmiz
                
# ism = input('Iltimos ismingizni kiriting: ').capitalize()#Foydalanuvchidan ismini so'rayapmiz

# if ism not in hisoblar:#Agar ism hisoblar ichida bo'lmasa pastdagi habar chiqadi
#     print('Kechirasiz, sizning ismingiz mavjud emas')
# else:#Aks holda tsikl boshlanadi
#     while True:#Abadiy tsikl
#         try:#Foydalanuvchi notog'ri ma'lumot kiritsa error chiqmaydi
#             operation = int(input('Kerakli operatsiya raqamini tanlang:\n'))#Foydalanuvchidan operatsiya raqamini kiritishini so'raymiz
#             if operation == 0:#Agar foydalanuvchi 0 raqamini kiritsa 
#                 print('Dastur to\'xtadi.')
#                 break#Dastur to'xtaydi
#             elif operation == 1:#Foydalanuvchi 0 raqamini kiritsa
#                 print(f"Hisobingizdagi mablag' {hisoblar[ism]} so'm.")#Quyidagi habar chiqadi
#             elif operation == 2:#Agar foydalanuvchi 2 raqamini kiritsa
#                 hisob = float(input('Hisobingizga qo\'shmoqchi bo\'lgan mablag\'ni kiriting:\n'))#Yechmoqchi bo'lgan summani kiritishini so'raymiz
#                 if hisob > 0:#Agar foydalanuvchi kiritgan summa musbat bo'lsa
#                     hisoblar[ism] += hisob#Uning hisobidagi summaga kiritilgan summani kiritamiz
#                     print(f"Hisobingizdagi mablag' {hisoblar[ism]} so'm.")#Va yangi mablag'ni elon qilamiz
#                 else:#Aks holda ya'ni foydalanuvchi manfiy summa kiritsa
#                     print('Noto\'g\'ri ma\'lumot kiritildi.')#Quyidagi habar chiqadi
#             elif operation == 3:#Agar foydalanuvchi 3 raqamini kiritsa 
#                 hisob = float(input('Hisobingizdan yechmoqchi bo\'lgan mablag\'ni kiriting:\n'))#Foydalanuvchi hisobidan yechmoqchi bo'lgan summani so'raymiz
#                 if hisob > 0:#Agar foydalanuvchi musbat summa kiritsa 
#                     if hisob < hisoblar[ism]:#Va agar yechmoqchi bo'lgan summa hisobdagi summadan kichkina bo'lsa
#                         hisoblar[ism] -= hisob#Hisobdagi summadan kiritilgan summani ayiramiz
#                         print(f"Hisobingizdan mablag' yechildi. Hisobingiadagi mablag': {hisoblar[ism]} so'm")#Va bu habarni chiqaramiz
#                     else:#Aks holda ya'niy foydalanuvchi yechmoqchi bo'lgan summa balansdan ko'p bo'lsa
#                         print('Hisobingizda mablag\' yetarli emas. ')#Quyidagi habar chiqadi
#                 else:#Aks holda ya'ni kiritgan summa 0 dan kichkina bo'lsa
#                     print('Xatolik! Faqat musbat summa kiriting.')#Bu habar chiqadi
#             else:#Aks holda ya'niy noto'g'ri operatsiya raqami tanlansa
#                 print('Noto\'g\'ri operatsiya raqami qayta urunib ko\'ring.')#Bu habar chiqadi
#         except ValueError:#Agar foydalanuvchi raqam emas matin yoni bshqa ma'lumot kiritsa
#             print('Iltimos, faqat son kiriting.')#Bu habar chiqadi
                    
                      

# 1. Sug‘urta polislari hisoboti (For tsikli + Lug‘at + Ro‘yxat)
# Siz sug‘urta kompaniyasida ishlaysiz va mijozlarning polislari bo‘yicha hisobot tayyorlashingiz kerak. Quyidagi lug‘at berilgan:
# from collections import Counter
# polislar = {
#     "Ali": {"tur": "hayot", "muddati": 10, "summasi": 100_000},
#     "Vali": {"tur": "avto", "muddati": 1, "summasi": 5_000},
#     "Salim": {"tur": "hayot", "muddati": 15, "summasi": 150_000},
#     "Madina": {"tur": "tibbiy", "muddati": 2, "summasi": 20_000},
# }
# # Vazifa:
# # Har bir sug‘urta turi bo‘yicha nechta mijoz borligini aniqlang.
# # Eng uzoq muddatga olingan sug‘urta polisini aniqlang.
# # Hayot sug‘urtasi bo‘yicha jami summani hisoblang.
# tur_sanash = Counter(polis["tur"] for polis in polislar.values())#Polislar lug'ati ichidagi har bir qiymatnin yani lug'atni polis o'zgaruvchisiga yuklayapmiz
   


# 2. Ijaraga uy topish (While tsikli + Ro‘yxat + Shart operatori)
# Siz Toshkentda uy sotib olish uchun ijarada yashayapsiz va uylarga doir ma’lumotlar bor ro‘yxat quyidagicha:
# uylar = [
#     {"manzil": "Chilonzor", "narx": 60_000, "xona": 3},
#     {"manzil": "Yunusobod", "narx": 80_000, "xona": 2},
#     {"manzil": "Olmazor", "narx": 50_000, "xona": 1},
#     {"manzil": "Mirzo Ulug‘bek", "narx": 100_000, "xona": 4},
# ]
# # Vazifa:
# # Foydalanuvchidan maksimal byudjetini so‘rang va shunga mos keladigan uylardan ro‘yxat tuzing.
# # Agar hech qaysi uy mos kelmasa, "Sizning byudjetingizga mos keladigan uy topilmadi." deb xabar bering.
# # Foydalanuvchi "stop" deb yozmaguncha yangi byudjet kiritishiga ruxsat bering.
# while True:#Abadiy tsikil yaratayapmiz
#     byudjet = input('Qancha pulingiz bor(Yoki "stop" deb yozing): ')#Foydalanuvchidan qancha puli borligini so'rayapmiz
#     if byudjet == "stop":#Agar foydalanuvchi stop deb yozsa 
#         print('Dastur tugadi.')#Quyidagi matin chiqadi
#         break#Va dastur tugaydi
#     try:#Foydalanuvchi xato malumot kiritsa ishlatiladi
#         byudjet = int(byudjet)#Foydalanuvchi kiritgan pul qiymatini butun songa o'tkazib olayapmiz
#         mos_uylar=[]#mos uylar degan bo'sh ro'yhat yaratayapmiz
#         for uy in uylar:#uylar ro'yhatidagi har bir elementni uy nomli o'zgaruvchiga yuklayapmiz
#             if uy["narx"]<=byudjet:#Agar uyning narhi foydalanuvchi kirotgan qiymatdan katta bo'lsa
#                 mos_uylar.append(uy)#Mos uylar ro'yhatiga bu uyning ma'lumotini kiritayapmiz                
#         if mos_uylar:
#             print('\nSizning pulingizga mos keladigan uylar:')#va quyidagi xabarni chiqarayapiz
#             for uy in mos_uylar:#uy o'zgaruvchisiga mos uylar ro'yhatidagi har bir elementni qo'shayapmiz
#                 print(f'{uy["manzil"]} tumanida {uy["xona"]} xonali, narhi: {uy["narx"]}$')#va bu matinni chiqarayapmiz
#         else:#Aks holda ya'niy foydalanuvchi kiritgan narh uy narhlaridan kam bo'lsa 
#             print('Sizning pulingizga mos uy mavjud emas.')#Quyidagi matin chiqadi
#     except ValueError:#try ni yopilishi. Agar foydalanuvchi hato malumot kiritsa quyidagi matin chiqadi.
#         print('Iltimos to\'g\'ri ma\'lumot kiriting.')
    
                
                



# 3. Mijozlarning qarzlarni to‘lash tizimi (While + Lug‘at + Ro‘yxat)
# Sug‘urta kompaniyangizda mijozlarning to‘lanmagan qarzlari bor va siz avtomatik tizim yaratmoqchisiz. Quyidagi lug‘at berilgan:
# qarzdorlar = {
#     "Ali": 1_200_000,
#     "Vali": 500_000,
#     "Hasan": 2_300_000,
#     "Madina": 700_000
# }
# # Vazifa:
# # Foydalanuvchidan ism va to‘layotgan pul miqdorini so‘rang.
# # Agar ism lug‘atda bo‘lsa, pulni hisobdan ayirib yangilangan qarzni chiqaring.
# # Agar to‘liq to‘lagan bo‘lsa, "Tabriklaymiz! Qarz yopildi!" deb xabar bering va lug‘atdan o‘chirib tashlang.
# # "stop" deb yozmaguncha mijozlardan pul qabul qilishda davom eting.

# while True:
#         ism = input('Ismingizni kiriting(Dasturni to\'xtatish uchun stop deb yozing): ').capitalize()
        
#         if ism.lower() == 'stop':
#             print('Dastur tugadi.')
#             break
#         if ism in qarzdorlar:
#             qarz = int(input("To'lamoqchi bo'lgan mablag'ni kiriting: "))
#             if qarzdorlar[ism]-qarz>0:
#                qarzdorlar[ism] -=qarz
#                print(f"Sizning qarzingiz: {qarzdorlar[ism]:,} so'm")
#             elif qarzdorlar[ism]-qarz==0:           
#                 print('Tabriklaymiz! Qarz yolidi.')
#                 del qarzdorlar[ism]
#             elif qarzdorlar[ism]-qarz<0:
#                 ortiqcha = qarz-qarzdorlar[ism]
#                 print(f"Siz {ortiqcha:,} ortiqcha pul to'ladingiz.")
#                 del qarzdorlar[ism]
#         else:
#             print('Siz qarzdorlar ro\'yhatida yo\'qsiz.')




# 4. Avtomobil sug‘urtasi narxlash tizimi (If + For + Lug‘at)
# Avtomobil sug‘urtasi uchun mijozlarga har yili yangilangan narx taqdim qilishingiz kerak. Tariflar quyidagicha:
# Yangi mashina (0-3 yil): 5% sug‘urta narxi
# O‘rta yoshdagi mashina (4-10 yil): 3% sug‘urta narxi
# Eski mashina (10 yildan katta): 1% sug‘urta narxi
# Lug‘at shaklida mashinalar ro‘yxati bor:
# avtomobillar = {
#     "Cobalt": {"yili": 2023, "narxi": 150_000_000},
#     "Nexia": {"yili": 2018, "narxi": 90_000_000},
#     "Damas": {"yili": 2010, "narxi": 50_000_000},
# }
# # Vazifa:
# # Har bir mashina uchun sug‘urta narxini hisoblang.
# # Natijani quyidagicha ekranga chiqaring:
# # Cobalt uchun sug‘urta narxi: 7 500 000 so‘m  
# # Nexia uchun sug‘urta narxi: 2 700 000 so‘m  
# # Damas uchun sug‘urta narxi: 500 000 so‘m  
# for mashina, info in avtomobillar.items():
#     if 0 < 2025 - info['yili'] <= 3:
#         narh = info['narxi']*0.05
#     elif 4 <= 2025 - info['yili'] < 10:
#         narh = info['narxi']*0.03
#     elif 10 <= 2025 - info['yili']:
#         narh = info['narxi']*0.01
#     print(f"{mashina} uchun sug'urta narxi: {narh} so'm")


        
# 5. Ish haqi indeksatsiyasi (For + Ro‘yxat + If shart operatori)
# Siz kompaniyangizdagi xodimlarning ish haqini inflyatsiya darajasiga qarab oshirish tizimini ishlab chiqmoqdasiz. Quyidagi ro‘yxat berilgan:
ishchilar = [
    {"ism": "Ali", "oylik": 7_000_000, "tajriba": 2},
    {"ism": "Vali", "oylik": 8_500_000, "tajriba": 5},
    {"ism": "Madina", "oylik": 10_000_000, "tajriba": 10},
]

for info in ishchilar:
    staj = info['tajriba']
    if 0<staj<=3:
        info['oylik'] += info['oylik']*0.05
    elif 4<=staj<=7:
        info['oylik'] += info['oylik']*0.1
    else:
        info['oylik'] += info['oylik']*0.15
    print(f"{info['ism'].title()} ning yangi oyligi: {info['oylik']:,} so'm")
# Qoidalar:
# 0-3 yil tajribasi bo‘lsa – 5% oshiriladi.
# 4-7 yil tajribasi bo‘lsa – 10% oshiriladi.
# 8+ yil tajribasi bo‘lsa – 15% oshiriladi.
# Vazifa:
# Har bir xodimning ish haqini oshirib, yangi oylikni chiqarish.
# Natijani quyidagicha ko‘rsating:
# Ali ning yangi oyligi: 7 350 000 so‘m  
# Vali ning yangi oyligi: 9 350 000 so‘m  
# Madina ning yangi oyligi: 11 500 000 so‘m  