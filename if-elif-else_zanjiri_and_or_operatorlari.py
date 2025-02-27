# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:19:15 2025

MAVZU: if-elif-else zanjiri, and, or operatorlari. BIR NECHTA SHARTLARNI TEKSHIRISH

@author: f.mamadiev
"""

#Kod yozishimiz davomida bizdan bitta emas bir nechta shartlarni tekshirish talab qilinishi mumkun
#Bunday hollarda biz if, else operatorlaridan tashqari elif operatoridan ham foydalanishimiz mumkun
#elif ingliz tilidan tarjima qilinganda aks holda, agar deb tarjima qilinadi

#Misol
#Foydalanuvchi kiritgan yoshga qarab chipta ranxini chiqaruvchi dastur yozaylik
# yosh = int(input('Yoshingiz nechida?\\n>>>'))
# if yosh<=4:#Agar yosh 4 dan kichik yoki teng bo'lsa
#     print('Chipta narhi 4000 so\'m')
# elif yosh<=12:#Yosh 4<yosh<=12 bo'lsa
#     print('Chipta narhi 8000 so\'m')
# else:#Yosh 12 dan katta bo'sa ya'ni yuqoridagi ikkita shart bajarilmasa
#     print('Chipta narhi 10000 so\'m')


#Biz yuqoridagi misolimizda elfni bir marta ishlatdik aslida elifni bir nrcha marta ishlatish mumkun
#Masalan
#Hayvonot bog'iga kirish 4 yoshdan kichkinalar uchun bepul qaryalar uchun esa chegirma narhda chiqarish dasturi chiqarish talab qilinsin
# yosh = int(input('Yoshingiz nechida?\n'))
# if yosh<=7:#Yosh 7 dan kichik yoki teng bo'lsa
#     print('Kirish bepul.')
# elif yosh<=18:#Yosh 12 dan katta 18 dan kichik yoki teng bo'lsa
#     print('Chipta narhi 5000 so\'m')
# elif yosh<=60:#Yosh 18 dan katta 60 dan kichik yoki teng bo'lsa
#     print('Chipta narhi 10000 ming so\'m')
# else:#Yuqoridagi shartlar bajarilmasa
#     print('Chipta narhi 8000 so\'m')


#Dasturlashda bitta kodni qayta qayta yozmaslik uchun takrorlanuvchi kodlarni biror o'zgaruvchiga yuklanadi
# yosh = int(input('Yoshingiz nechida?\n'))
# if yosh<=7:#Yosh 7 dan kichik yoki teng bo'lsa
#      narh = 0
# elif yosh<=18:#Yosh 12 dan katta 18 dan kichik yoki teng bo'lsa
#      narh = 5000
# elif yosh<=60:#Yosh 18 dan katta 60 dan kichik yoki teng bo'lsa
#      narh = 10000
# else:#Yuqoridagi shartlar bajarilmasa
#      narh = 8000
# print(f'Chipta narhi {narh} so\'m')

#Birnechta shartlarni bajarishda ham else operatorini ishlatish itiyoriy
#if-elif-else shart operatorlarining kamchiligi agar shartlarni bittasi bajarilgan taqdirda keyingi shartlarni tekshirmaydi va to'g'ri chiqqan shart bilan ishni to'xtatadi
#Shartlarni hammasini tekshirish uchun or va and operatorlaridan foydalanish kerak
#Masalan
#Fordalanuvchidan bugungi kunni kiritganda u ish kuni yoki dam olish kuni ekanligini chiqaruvchi dastur tuzaylik
#Foydalanuvchidan kunni so'raymiz
# kun = input('Bugun kun nima?\n')
# if kun.lower()=='yakshanba' or kun.lower()=='shanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun ish kuni')


#or operatori shartlarning u yoki bunis bajarilganda ishlaydi.
#Amaliyotda berilgan shartlarni hammasi bajarilganda kodimiz ishlashi talab qilinishi mumkun.
#Bunday holatlarda and ya'ni va operatoridan foydalanamiz
#Masalan
#Biz foydalanivchidan kunni va haroratni so'raymiz.
#Agar kun yakshanba va harorat 30 dan baland bo'lsa kettik cho'milishga degan agar kun yakshanba va 30 dan past bo'lsa uyda o'tiramiz degan habar chiqsin
#Foydalanuvchidan kunni so'rayapmiz
# kun = input('Bugun qanday kun?\n')
# #Foydalanuvchidan haroratni so'rayapmiz
# harorat = float(input('Harorat qanday\n'))
# #Agar kun yakshanba va harorat 30 dan baland bo'lsa
# if kun.lower()=='yakshanba' and harorat>30:
#     print('Kettik cho\'milishga')
# #Agar kun yakshanba va harorat 30 dan past bo'lsa
# elif kun.lower()=='yakshanba' and harorat<30:
#     print('Uyda o\'tiramiz')

#Yuqoridagi misolimizda shartlarning ikkalasi ham bajarilganda kodimiz ishlaydi. Agar shartlarning bittasi bajarilmasa ham kodimiz ishlamaydi

#or va and operatorlarini birga ishlatish
#Yuqoridagi masalamizda dam olish kuni sifatida faqat yakshanba kunni oldik
#Foydalanuvchi shanba yoki yskshabmba kunni kiritganda va haroratni kiritganda kodimiz ishlasin
#Foydalanuvchidan kunni so'raymiz
# 



#BOOLEN ma'lumot turi
#Biz avvalgi darslarimizda true va false amallarini ko'rdik. Bu amallar boolen qiymatlar ya'ni mantiqiy amallar deyiladi
#Mandiqiy amallar dasturlashda keng qo'llaniladi
#Biz o'zgaruvchilarga mantiqiy qiymatlarni ham yuklab qo'yishimiz bumkun
#Bir bisol ko'raylik. Mijoz 15000 so'mga ovqat olgan bo'lsin
#Agar mijoz ovqatga qo'shib choy va salat yoki ulardan birini olgan bo'lsa yakuniy narhni ekranga chiqaruvchi dastur tuzaylik
# narh = 15000
# choy = True
# salat = False
# #Agar mijoz ovqat bilan birga choy va salat olgan bo'lsa
# if choy and salat:
#    narh = narh + 10000
# #Agar migoz choy yoki salat olgan bo'lsa
# elif choy or salat:
#     narh = narh + 5000
# else:
#     narh = narh
# print(f'Jami {narh} so\'m')


#if-elif-else zanjirining kamchiligi shartlardan biri bajarilganda qolgan shartlarni tekshirmaydi. Shu sababli shartlar jetma ketligini har birini tekshirish uchun har bir shartni alohida ish operatori bilan tekshiramiz
#Yuqoridagi misolimizni kengaytirib har bir shartni ef bilan tekshiraylik
# narh = 15000#Mijoz 15000 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = True
# if choy:#Agar mijoz choy olsa
#    print('Mijoz choy oldi.')
#    narh = narh + 5000
# if salat:#Agar mijoz salat olsa
#    print('Mijoz salat oldi.')
#    narh = narh + 5000
# if non:#Agar mijoz non olsa
#     print('Mijoz bob oldi.')
#     narh = narh + 2000
# if kompot:#Agar mijoz kampot olsa
#     print('Mijoz kompot oldi.')
#     narh = narh + 10000
# if assorti:#Agar mijoz assorti olsa
#     print('Mijoz assorti oldi.')
#     narh = narh + 15000
# print(f'Jami narh {narh} so\'m bo\'ldi')  


#Ro'yhat tarkibini tekshirish
#in operatori yordamida biz ro'yhatning tarkibida ma'um element borligini tekshirishimiz mumkun
#Mijoz kiritgan ovqat menyuda bo'lsa buyurtma qbul qilindi degan agar menyuda bo'lmasa avfsusku bunday ovqat menyuda yo'q degan matin chiqaraylik
#Menyu
# menyu = ['salat', 'osh', 'shorva', 'lag\'mon']
# #MIJOZDAN NIMA YEYISHINI SO'RAYAPMIZ
# ovqat = input('Nima yeysiz?\n')
# #aGAR MIJOZ KIRITGAN OVQAT MEYNUDA BO'LSA
# if ovqat.lower() in menyu:
#     print('Buyurtma qabul qilindi.')
# #Agar mijoz kiritgan ovqat menyuda no'lmasa
# else:
#     print('Avfsusku bizda bunday ovqat yo\'q.')


#not in operatori orqali element ro'yhatda yo'qligini tekshirishimiz mumkun
#Yuqoridagi misolimizni not in operatori orqali bajaramiz
# menyu = ['salat', 'osh', 'shorva', 'lag\'mon']
# #MIJOZDAN NIMA YEYISHINI SO'RAYAPMIZ
# ovqat = input('Nima yeysiz?\n')
# #aGAR MIJOZ KIRITGAN OVQAT MEYNUDA BO'LSA
# if ovqat.lower() not in menyu:
#     print('Avfsusku bizda bunday ovqat yo\'q.')
# else:
#     print('Buyurtma qabul qilindi.')
    

#Ikki ro'yhatni solishtirish
#Bizga menyu va buyurtmalar ro'yhati berilgan bo'lsin
#Restaran menyusi
# menyu = ['assarti', 'shashlik', 'osh', 'shorva', 'non', 'choy', 'salat']
# #Mijozning buyurtmasi
# buyurtmalar = ['lagmon', 'non', 'choy', 'manti', 'somsa', 'salat']
# #Mijozning buyurtmasidagi har bir elementni taom o'zgaruvchisiga yuklaymiz
# for taom in buyurtmalar:
#     #Agar taom menyu ichida bo'lsa
#     if taom in menyu:
#         print(f'Menyuda {taom} bor')
#         #Aks holda
#     else:
#         print(f'Menyuda {taom} yo\'q')


#Yuqoridagi misolimizda mijoz tenlagan buyurtmalar menyuda borligini tekshirdik
#Agar mijoz hechnarsa tanlamagan ya'mi savat bo'sh bo'lsachi
#Bundar holatlarda for aperatorini ishlatishdan avval buyurtmalar ro'yhati bo'sh emasligini tekshirishimiz kerak
#Restaran menyusi
# menyu = ['assarti', 'shashlik', 'osh', 'shorva', 'non', 'choy', 'salat']
# # Mijozning buyurtmasi
# buyurtmalar = ['lagmon', 'non', 'choy', 'manti', 'somsa', 'salat']
# if buyurtmalar:#Agar buyurtmalar ro'yhati bo'sh bolmasa True qiymat qaytaradi ya'ni shat bajariladi
#    #Mijozning buyurtmasidagi har bir elementni taom o'zgaruvchisiga yuklaymiz
#    for taom in buyurtmalar:
#        #Agar taom menyu ichida bo'lsa
#        if taom in menyu:
#            print(f'Menyuda {taom} bor')
#            #Aks holda
#        else:
#            print(f'Menyuda {taom} yo\'q')
# else:#Agar buyurtmalar ro'yhati bo'sh bo'lsa
#     print('Savatingiz bo\'sh')



#AMALIYOT
#1-MASALA
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# son = int(input('Juft son kiriting\n'))
# #Agar kiritilgan sonni 2 ga bo'lganda qoldiq 0 bo'lsa
# if son%2==0:
#     print('Rahmat!')
# else:
#     print('Bu son juft emas.')
           
   
#2-MASALA
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# yosh = int(input('Yoshingiz nechida?\n'))
# # Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa
# if yosh<4 or yosh>60:
#     narh = 0
# elif yosh<18:
#     narh = 10000
# elif yosh<60:
#     narh = 20000
# print(f'Chipta narhi {narh} so\'m')


#3-MASALA
#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# birinchi_son = int(input('Birinchi sonni kiriting\n'))
# ikkinchi_son = int(input('Ikkinchi sonni kiriting\n'))
# if birinchi_son==ikkinchi_son:
#     print('Kiritilgan sonlar teng')
# elif birinchi_son>ikkinchi_son:
#     print('Birinchi son ikkinchi sondan katta')
# else:
#     print('Ikkinchi son birinchi sondan katta')


#4-MASALA
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ['olma', 'tuz', 'sharbat', 'un', 'tuhum', 'moy', 'go\'sht', 'banan', 'qatiq', 'non', 'kartoshka', 'sabzi', 'guruch', 'piyoz']
# savat = []
# #n 0 dan 5 gacha bo'lgan sonlarni har birini n ga yuklayapdi
# for n in range(5):
#     #n 0 dan boshlanganligi chun n+1 mahsulot kiritish so'ralayapdi va kiritilgan mahsulot bo'sh ro'yhatga qo'shilayapdi
#     savat.append(input(f'{n+1}-mahsulotni kiriting\n'))
#     #Agar savatdagi mahsulotlar mahsulotlar ro'yhatida bo'lsa 
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         print(f'{mahsulot.lower()} do\'konimizda bor.')
#     else:
#         print(f'{mahsulot.lower()} do\'konimizda yo\'q.')



#5-MASALA
#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
# mahsulotlar = ['olma', 'tuz', 'sharbat', 'un', 'tuhum', 'moy', 'go\'sht', 'banan', 'qatiq', 'non', 'kartoshka', 'sabzi', 'guruch', 'piyoz']
# savat = []
# for n in range(5):
#     savat.append(input(f'{n+1}-mahsulotni kiriting\n'))
# bor_mahsulotlar =[]
# mavjud_emas = []
# #Savatdagi har bir narsabni mahsulot o'zgaruvchisiga yuklayapmiz
# for mahsulot in savat:
#     #Agar mahsulot mahsulotlar ro'yhatida bo'lsa
#     if mahsulot in mahsulotlar:
#         #Bor mahsulotlar ro'yhatiga qo'shayapmiz
#         bor_mahsulotlar.append(mahsulot)
#         #Aks holda yani mahsulot mahsulotlar ichida bo'lmasa
#     else:
#         #mavjud emas mahsulotlar ro'yhatiga qo'shayapmiz
#         mavjud_emas.append(mahsulot)
# #Agar mavjud emas ro'yhati bo'sh bo'lsa
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print('Siz tanlagan barcha ahsulotlar do\'konimizda bor.')


#6-MASALA
#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
# foydalanuvchilar = ['olim', 'anvar', 'husan', 'sodiq', 'xurshid']
# login = input('Login kiriting\n')
# if login.lower() in foydalanuvchilar:
#     print('Login band, Yangi login tanlang.')
# else:
#     print('Xush kelibsiz!')



#7-MASALA
# son = float(input('Birorta son kiriting\n'))
# for n in range(2, 11):
#     if son%n==0:
#         print(f'{son} soni {n} ga qoldiqsiz bo\'inadi')

   

    

# QO'SHIMCHA MASALALAR

# 1. Boshlang‘ich daraja (1–10-masalalar)
# 1. Juft yoki toq?
# Foydalanuvchi kiritgan son juft yoki toq ekanligini aniqlang.
# son = int(input('Biror son kiriting\n'))
# if son%2==0:
#     print('Kiritilgan son juft.')
# else:
#     print('Kiritilgan son toq.')  
    
    
    
    
# 2. Musbat, manfiy yoki nol?
# Foydalanuvchi son kiritadi. U musbat, manfiy, yoki nol ekanligini aniqlang.
# son = int(input('Biror son kiriting:\n'))
# if son > 0:
#     print('Musbat son.')
# elif son==0:
#     print('Son 0 ga teng')
# else:
#     print('Manfiy son')




# 3. Eng katta son
# Foydalanuvchi uchta son kiritadi. Ushbu sonlarning eng kattasini toping.
# x = int(input('Birinchi sonni kiriting:\n'))
# y = int(input('Ikkinchi sonni kiriting:\n'))
# z = int(input('Ikkinchi sonni kiriting:\n'))
# if x>y and x>z:
#     print(f'Eng katta son: {x}')
# if y>x and y>z:
#     print(f'Eng katta son: {y}')
# if z>x and z>y:
#     print(f'Eng katta son: {z}')





# 4. Uchburchak hosil bo‘ladimi?
# Berilgan a, b, c tomonlardan uchburchak yasash mumkinligini tekshiring. Uchburchak sharti:
# a+b>c,a+c>b,b+c>a
# 5. Baholash tizimi
# 0–100 oralig‘idagi baho uchun quyidagi harfli baholarni ekranga chiqaring:
# x = int(input('Birinchi sonni kiriting:\n'))
# y = int(input('Ikkinchi sonni kiriting:\n'))
# z = int(input('Ikkinchi sonni kiriting:\n'))
# if x+y>z and x+z>y and y+z>x:
#     print('Sonlar uchburchak tengsizligini qanoatlantiradi.')
# else:
#     print('Sonlar uchburchak tengsizligini qanoatlantirmaydi.')





# 5. Baholash tizimi
# 0–100 oralig‘idagi baho uchun quyidagi harfli baholarni ekranga chiqaring:
# 90–100 → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# 0–59 → F
# baho = int(input('Bahoni kiriting: '))
# if baho>=0 and baho<=59:
#     daraja = 'F'
# if baho>=60 and baho<=69:
#     daraja = 'D'
# if baho>=70 and baho<=79:
#     daraja = 'C'
# if baho>=80 and baho<=89:
#     daraja = 'B'
# if baho>=90 and baho<=100:
#     daraja = 'D'
# print(f'Siz oralig\'da {daraja} oldingiz!')




# 6. Haftaning kuni
# Foydalanuvchi 1 dan 7 gacha son kiritadi. Ushbu songa mos keluvchi hafta kunini chiqaruvchi dastur yozing.
# son = int(input('1 dan 7 gacha biror son kiriting\n'))
# hafta_kunlari = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba']
# if 1<=son<=7:
#     print(hafta_kunlari[son - 1])
# else:
#     print('Iltimos 1 dan 7 gacha son kiriting')
    



# 8. Sonlar tartibi
# Foydalanuvchi uchta son kiritadi. Ularni kichikdan kattaga qarab tartiblang.
# x = int(input('x = '))
# y = int(input('y = '))
# z = int(input('z = '))
# sonlar = [x, y, z]
# sonlar.sort()
# print(sonlar)


# 9. Yoz yoki qish?
# Foydalanuvchi oy raqamini (1–12) kiritadi. Ushbu oyga mos keluvchi faslni ekranga chiqaring.
# raqam = int(input('1 dan 12 gacha biror raqam kiriting:\n'))
# if 1<=raqam<=3 :
#     fasil = 'Bahor'
# elif 3<=raqam<=6:
#     fasil = 'Yoz'
# elif 6<=raqam<=9:
#     fasil = 'Kuz'
# elif 9<=raqam<=12:
#     fasil = 'Qish'
# else:
#     fasil = 'noto\'g\'ri'
# print(f'Siz {fasil} fasli raqamini kiritdingiz')




# 10. Chegirma hisoblash
# Xarid summasi berilgan. Chegirma qoida bo‘yicha hisoblanadi:
# 100$ dan kam → chegirma yo‘q
# 100$–200$ → 5% chegirma
# 200$ dan yuqori → 10% chegirma
# Dastur xariddan keyin to‘lanishi kerak bo‘lgan summani hisoblasin.
# harid = float(input('Harifingiz summasi: '))
# if harid<100:
#     jami = harid
# elif 100<=harid<200:
#     jami = (harid/100)*95
# elif 200<=harid:
#     jami = (harid/100)*90
# print(f'Sizning haridingiz {jami}$ bo\'ldi.')



# 11. Raqamli lotereya
# Foydalanuvchi ikki xonali son kiritadi. Agar sonning ikkala raqami bir xil bo‘lsa, "Mukofot yutdingiz!", aks holda "Omad keyingi safar!" deb chiqaring.
# son = float(input('Ikki honali son kiriting'))
# onlik = son//10
# birlik = son%10
# if onlik==birlik:
#     print('Mukofot yutdingiz')
# else:
#     print('Omad keyingi sagar')



# 12. Tenglik tekshiruvi
# Foydalanuvchi ikkita son kiritadi. Ular teng, birinchisi katta, yoki ikkinchisi katta ekanligini aniqlang.
# x = int(input('Birinchi sonni kiriting: '))
# y = int(input('Ikkinchi sonni kiriting: '))
# if x>y:
#     print(f'{x}>{y}')
# elif x<y:
#     print(f'{x}<{y}')
# elif x==y:
#     print(f'{x}={y}')

# 13. Uchburchakning turini aniqlash
# Agar uchta tomon uchburchak hosil qilsa:
# a = int(input('Uchburchakning birinchi tomoni: '))
# b = int(input('Uchburchakning ikkinchi tomoni: '))
# c = int(input('Uchburchakning birinchi tomoni: '))
# if a+b>c and a+c>b and b+c>a:
#     if a==b==c:
#         print('Teng tomonli uchburchak')
#     elif a==b or a==c or b==c:
#         print('Teng yonli uchburchak')
#     else:
#         print('Turli tomonli uchburchak')
# else:
#     print('Bunday uchburchak mavjud emas')

# Teng tomonli bo‘lsa → "Teng tomonli uchburchak"
# Teng yonli bo‘lsa → "Teng yonli uchburchak"
# Turli tomonli bo‘lsa → "Turli tomonli uchburchak"


# 20. Yil fasllari
# Foydalanuvchi oy nomini kiritadi (Yanvar, Fevral, ...). Dastur oy qaysi faslga tegishli ekanligini aniqlasin.
# oy = input('Oy nomini kiriting: ')
# if oy.lower()=='mart' or oy.lower()=='aprel' or oy.lower()=='may':
#     fasil='Bahor'
# elif oy.lower()=='iyun' or oy.lower()=='iyul' or oy.lower()=='avgust':
#     fasil='Yoz'
# elif oy.lower()=='sentyabr' or oy.lower()=='oktyabr' or oy.lower()=='noyabr':
#     fasil='Kuz'
# elif oy.lower()=='dekabr' or oy.lower()=='yanvar' or oy.lower()=='fevral':
#     fasil='Qish'
# else:
#     print('Bunday oy nomi yoq')
# print(f'Hozir {fasil} fasli ekan')



# 3. Murakkab daraja (21–25-masalalar)
# 21. Bank omonati
# Foydalanuvchi ombor miqdorini kiritadi. Agar 5000$ dan oshsa, unga 3% foiz qo‘shiladi. Yangi balansni hisoblang.

# 22. Sport bahosi
# Foydalanuvchi yugurish bo‘yicha natijasini (sekundda) kiritadi. Baholash tizimi:

# 10 sek va undan tez → "Zo‘r sportchi"
# 10-15 sek → "O‘rtacha"
# 15 sek dan ko‘p → "Kamroq shug‘ullanish kerak"
# 23. Temperatura bo‘yicha tavsiyalar
# Foydalanuvchi havo haroratini kiritadi.

# 0°C dan past → "Issiq kiyining"
# 0-20°C → "O‘rtacha kiyining"
# 20°C dan yuqori → "Yengil kiyining"
# 24. Qiziqarli son
# Foydalanuvchi uch xonali son kiritadi. Agar raqamlar yig‘indisi 10 ga karrali bo‘lsa, "Bu qiziqarli son!", aks holda "Oddiy son" deb chiqaring.

# 25. Uchburchak burchaklari
# Foydalanuvchi uchburchakning uchta burchagini kiritadi. Agar burchaklar yig‘indisi 180° bo‘lsa, "Bu haqiqiy uchburchak", aks holda "Bu uchburchak emas" deb chiqaring.


