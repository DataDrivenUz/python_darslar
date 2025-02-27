# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:53:05 2025

MAVZU: WHILE TSIKL OPERATORI

@author: f.mamadiev
"""
#Dasturlar odatda foydalanuvchiga yengillik berish, ularning ishlarini osonlashtirish uchun yaratiladi
#Input funnktsiyasi foydalanuvchidan biror narsani ya'ni savol so'raganimizda ko'proq ishlatishimiz mumkun
#Input funktsiyasi orqali kiritilgan savolni ham boshqa o'zgaruvchiga yuklashimiz mumkun
#Masalan
# ism =input('Ismingiz nima? ')#Foydalanuvchidan ismini so'rayapmiz
# savol = f'Salom, {ism.title()}. Yoshingiz nechida? '#Foydalanuvchi bergan javobni va qo'shimcha savolni yangi o'zgaruvchiga saqlayapmiz
# yosh = input(savol)#Foydalanuvchi bergan javobni va qo'shimcha savolni bitta savol ko'rinishiga o'tkazayapmiz


#input() va sonlar
#Input ichiga kiritilgan savoj javobi qanday turda bo'lishidan qatiy nazar input funktsiyasi uni matin ko'rinishida qabul qiladi
#Agar foydalanuvchi kiritayotgan javob son ko'rinishida bo'lsa uni butun son yoki o'nlik son turiga o'tkazib olishimiz kerak
#Masalan
# ism =input('Ismingiz nima? ')#Foydalanuvchidan ismini so'rayapmiz
# savol = f'Salom, {ism.title()}. Yoshingiz nechida? '#Foydalanuvchi bergan javobni va qo'shimcha savolni yangi o'zgaruvchiga saqlayapmiz
# yosh = input(savol)#Foydalanuvchi bergan javobni va qo'shimcha savolni bitta savol ko'rinishiga o'tkazayapmiz
# yosh = int(yosh)#Foydalanuvchi yoshini kiritganda uni butun songa o'tkazib olayapmiz
# heigh = input('Bo\'yingiz nechi? ')
# heigh = float(heigh)


#Biz avvalroq for takrorlash tsikl operatori bilan tanishgandik.
#For operatori malum bir ro'yhatni olib indagi elementlar tugagunga qadar biror kodni takrorlayveradi
#While operatori esa biritilgan shart bajarilar ekan yani True qiymat qaytarar ekan shart qaytarilay veradi
#Qachonki shart bajarilishdan to'xtasa ya'ni False qiymat qaytarsa sikl bajarilishdan to'xytaydi
#while so'zi ingiz tilidan "toki" yoki "-gacha" deb tarjima qilinadi.
#Keling bir misol ko'raylik

son = 1#Songa 1 qiymat berayapmiz
while son<=5:#Toki son 5 dan kichik ekan
     # print(son, end=' ')
     son = son+1
     
#Yuqoridagi kodimizda avval songa 1 qiymat berdik
#Songa 5 dan kichik yoki teng shartini berdik. Agar son<=5 bajarilar ekan sonni consolga chiqarish buyrug'ini berdik
#4-qatorda songa 1 ni qo'shib olish buyrug'ini berdik
#Binda sikl yana 2-qatorga qaytadi. son<=5 bo'lsa yana uni elon qiladi
#4-qatorda elon qilingan songa ya'ni 2 ga 1 qo'shadi son<=5 bo'lsa sonni yana elon qiladi
#Bu jarayon son<-5 bo'lguncha takrorlanadi


#Python dasturlash tilida += operatoti mavjud. Bu operator o'ng tomonda ishlatiladigan + belgisini o'rniga ishlatish mumkun

#While tsikli yordamida foydalanuvchiga dasturni to'ztatish imkoniyatini berishimiz mumkun
# print('Kitritilgan sonning kvadratini chiqaruvchi dastur:')
# savol = 'Istalgan sonni kiriting: '
# savol+='(Dasturni to\'xtatish uchun "exit" deb yozing): '#savol matniga shu matinni qo'shib olayapmiz
# qiymat = ""#Qiymat o'zgaruvchisiga hech qanday qiymat bermayapmiz
# while qiymat!='exit':#Toki qiymat 'exit' matniga teng bo'lmaguncha
#     qiymat = input(savol)#Qiymat o'zgaruvchisiga savol matnini kiritib qo'ydik
#     if qiymat!='exit':#Agar qiymat 'exit bo'lsa 
#         print(float(qiymat**2))#Sonning kvadratini chiqaradi
        

#Yuqoridagi masalamizda faqat bitta shart uchun ko'rdik. Bazi paytlarda katta dasturlarda bir nechta shartlar bajarilganda dasturni to'xtatish talab qilinishi mumkun
#Bunday holatlarda o'zgaruvchidan ishora sifatida foydalanib shartlarni tekshirish mumkun
# print('Kitritilgan sonning kvadratini chiqaruvchi dastur:')
# savol = 'Istalgan sonni kiriting: '
# savol+="(Dasturni to\'xtatish uchun 'exit' deb yozing): "#savol matniga shu matinni qo'shib olayapmiz
# ishora = True
# while ishora:#Ishora Truega teng ekan
#     qiymat = input(savol)
#     if qiymat=='exit':
#         ishora=False
#     else:
#         print(float(qiymat)**2)
        
        
        
#BREAK OPERATORI
#break operatori yordamida ma'lum bish shartni tekshirish va while sikl operatorini to'xtatib qo'yish mumkun
# print('Kitritilgan sonning kvadratini chiqaruvchi dastur:')
# savol = 'Istalgan sonni kiriting: '
# savol+="(Dasturni to\'xtatish uchun 'exit' deb yozing): "#savol matniga shu matinni qo'shib olayapmiz
# while True:#Agar sikl cheksiz bdavom etsa
#     qiymat = input(savol)#Qiymatga savolni yukla
#     if qiymat=='exit':#Agar qiymat exit bo'lsa 
#         break#Sikl to'xtatiladi
#     else:#Aks holda quyidagi ifoda bajariladi
#         print(float(qiymat)**2)


#Break operatori for tsiklini to'xtatish uchun ham ishlatlishi mumkun
# sonlar = list(range(1, 11))#1 dan 10 gacha sonlar ro'yhatini kiritib olayapmiz
# for son in sonlar:#Sonlar ro'yhatidagi har bir qiymatni son o'zgaruvchisiga yuklayapmiz
#     if son == 5:#Agar son 5 ga teng bo'lsa 
#         break#Sikl to'xtasin yani ro'yhatdagi qiymatnni son o'zgaruvchisiga yuklasin
#     print(f'{son} sonining kvadrati {son**2} ga teng')
    
    
    
#continue OPERATORI
#Continue operatori break operatorini teskarisi bo'lib malum shart bajarilganda shu shart bajarilgan jarayonni tashlab keyingi qadamga o'tib ketadi
#Masalan
# sonlar = list(range(1, 11))#1 dan 10 gacha sonlar ro'yhatini kiritib olayapmiz
# for son in sonlar:#Sonlar ro'yhatidagi har bir qiymatni son o'zgaruvchisiga yuklayapmiz
#     if son==5:#Agar son 5 ga teng bo'lsa 
#         continue#Son 5 ga teng bo'lganda sikl bajarilmayapdi va keyingi qadamga o'tib ketayapdi
#     print(f'{son} sonining kvadrati {son**2} ga teng.')
#Consolga etibor beradigan bo'lsak 5 ning kvadratini hisoblamayapdi

#Keling yana bir misol ko'raylik
# son = 0#Songa 0 qiymat berdik
# while son<10:#Son toki 10 dan kichkina ekan
#     son+=1#songa 1 ni qo'shib qo'yayapdi
#     if son%2!=0:#Agar son toq son bo'lsa
#         continue#Siklni bajarma ya'ni keyingi qadamga o'tib ket
#     else:#Aks holda
#         print(son)#Sonni chiqar


#ABADIY TSIKL TUZOG'I
#Dasturlash davomida abadiy tsikllar yaratib qo'yishdan ehtiyot bo'lish kerak
#Abadiy tsikllar noto'g'ri shartlar kiritish, noto'g'ri amallar bajarish mantiqiy amallarni noto'g'ri kiritish orqali kelib chiqadi
#Abadiy tsikllar uni to'xtatmaguncha to'ctamaydi. Uni to'xtatish uchun ctrl+c ni bosish kerak
#Masalan
# son = 0#Songa 0 qiymat berayapmiz
# while son<10:#Toki son 10dan kichkina ekan
#     if son%2!=0:#Agar son juft bo'lasa
#         continue#Keyingi qadamga o't
#     else:#Aks holda sonni chiqar
#         print(son)
        
#Bu buyrug'ni bajarganimizda sikl uni to'xtatmagunimizcha davom etib ketayvaeradi.
#Chunki songa 0 qiymat berdik 0 esa 10 dan kichkina

#Misol
# son = 1#Songa 1 qiymat berdin
# while son>0: #Toki son 0 dan katta ekan
#     son += 1#Songa 1 ni qo'sh
#     if son%2!=0:#Agar son toq bo'lsa
#         continue#Keyingi qadamga o'tib ket
#     else:#Aks holda sonni chiqar
#         print(son)
#Bu misolimizda abadiy sikl bo'lishiga sabab 0 dan katta sonlar cheksiz shuning uchun sikl cheksiz just sonlarni chiqaradi


