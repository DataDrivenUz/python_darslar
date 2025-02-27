# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:12:58 2025

MAVZU: FUNKTSIYA KIRITISH.

@author: 123
"""
#Funktsiya malum bir vazifani bajarishga mo'ljallangan bo'lib bir nechta kodlar jamlanmasi hisoblanadi
#Biz avvalgi darslarimizda bir nechta funktsiyalarni ishlatdik va bu funktsiyalarni faqatgina nomi bilan unga murojat qildik
#Aslida biz ishlatgan funktsiyalar uchida bir nechta kod mavjud bo'lib u bizga ko'rinmaydi
#Funktsiyalar biz kiritgan malumotni konsolga chiqarishi yoki malumot ustida bir nechta amallar bajarishi
#Yoki foydalanuvchi tomonidan hechqanday qiymat qabul qilmasligi mumkun
#Dasturlash davvomida biz ma'lum bir kodni qyta qayta yozmaslik uchun ularni malum bir funktsiyaga birirktirib qo'yishimiz mumkun
#Kod yozishdavomida esa bu funksiya nomi bilan murojat qilishimiz mumkun
#Bu darsimizda biz pythonda yangi funktsiya yaratish, unga murojat qilish,
#T'g'irlash va tekshirishni o'rganamiz


#Keling oddiy funktsiya yaratib ko'raylik
#Funktsiyamiz salom beruvchi funktsiya bo'lsin
#pythonda funktsiya kiritayotganda def bilan poshlaymiz

# def salom_ber():#Funktsiya nomi
#     """Salom beruvchi funktsiya"""#Funktsiya haqida ma'lumot
#     print('Assalomu alaykum!')#Funktsiyani chaqirganda konsolga chiqadigan matinni kiritayapmiz
# salom_ber()

#Yuqoridagi funktsiyamizda 1-qatorda funktsiyani nomlab oldik
#Ikkinchi qatorni o'ngroqqa surib 3 talik qo'shtirnoq ichida funktsiya haqida ma'lumot berdik
##Funktsiyamiz ustiga sichqonchani olib borsak funktsiya haqida shu ma'lumot chiqadi
#Uchinchi qatorda funktsiyani chaqirganimizda consolga chiqadigan matinni kiritdik
#To'rtinchi qatorda funktsiyani chaqirdik


#FUNKTSIYAGA QIYMAT BERISH
#Yuqoridagi funktsiyamizda biz funktsiyaga hech qanaqa qiymat permadik
#Endi funktsiyaga qiymat berishni ko'ramiz

# def salom_ber(ism):#Funktsiya kiritib oldik va unga qiynmat uzatdik
#     """Foydalanuvchi ismini qabul qilib, unga salom beruvchi funktsiya"""
#     print(f'Assalomu alaykum! {ism.title()}.')#Consolga chiqadigan matinni kiritdik
# salom_ber('faxriddin')#Funktsiyani chaqirdik

#Konsolga Assalomu alaykum! Faxriddin degan matin chiadi
#Funktsiyani chaqirganda unga qiymat bermasak xatolik chiqadi
#Agar kiritgan funktsiyamiz haqida malumotuzun bo'lib ketsa uni bir necha qatorga yozishimiz mumkun
#Funktsiya haqida kiritgan ma'lumotimiz docstrip deyiladi
#Funktsiya haqida ma'lumotni konsolga chiqarishimz uchun print(funksiya_nomi.__doc__) deb yozishimiz mumkun

#Funktsiya yaratishimizning asil maqsadlaridan biri biz unga qayta qayta yangi nom bilan murojat qilishimiz mumkun
#Biz yuqarida qiymat bberib kiritgan funktsiyamizda parametr va argumentni farqlab olishimiz kerak
#Yuqoridagi salom_ber(ism) funktsiyamizda ism funktsiya parametri
#Foydalanuvchi funktsiyani salom_ber('faxriddin') kabi chaqiganda faxriddin bu funktsiyani argumenti hisoblanadi

# salom_ber('hasan')
# salom_ber('husan')

#Yuqorida biz yaratgan funktsiyamizga ikki marta ikki hil argument bilan murojaq qildik


#Biz funktsiya kiritayotganimizda unga bir emas bir nechta qiymat berishimiz mumkun
#Faqat funktsiyani chaqirayorganimizda parametrlar qanday tartibda kiritilgan bo'lsa argumentlar ham shu tartibda kiritilishi kerak
#Foydalanuvchining ismi, familiyasi va yoshini chiqaruvchi funktsiya kiritamiz

# def toliq_ism(ism, familiya, yosh):#Fuktsiya kiritayapmiz
#     """Foydalanuvchi simi, familiyasi,
#     va yoshini chiqaruvchi funktsiya"""#Funktsiya haqida ma'lumot berayapmiz
#     print(f'Foydalanuvchining ismi: {ism.title()}\n'
#           f'Foydalanuvchining familyasi: {familiya.title()}\n'
#           f'Foydalanuvchining yoshi: {yosh} yosh')#Konsolga chiqadigan ma'lumotni kiritayapmiz
# toliq_ism('faxriddin', 'mamadiyev', 30)

#Bu funktsiyani chaqiyganimizda consolga foydalanuvchi ismi familyasi va yoshi chiqadi
#Eng asosiy shart funktsiya parametrlari qanday tertibda bo'lsa uning argumentlari ham shu tartibda bo'lishi kerak

#Foydalanuvchi kiritgan argumentlar orqali uning ismi va yoshini chiqaruvchi funktsiya tuzaylik

# def yosh_hisobla(ism, t_yil):#Parametrlar bilan funktsiya kiritayapmiz
#     """Foydalanuvchi ismi va tug'ilgan yili orqali,
#     uning yoshini chiqaruvchi dastur"""#Funktsiya haqida ma'lumot berayapmiz
#     print(f'{ism.title()} {2025-t_yil} yoshda')#consolga chqadigan matinni kiritayapmiz
# yosh_hisobla('faxriddin', 1995)#Funktsiyani chaqirayapmi

#Konsolga Faxriddin 30 yoshda degan matin chiqadi
#Agar biz bu funktsiyada ism va tug'ilgan yilni joyini alpashtirib qo'ysak hatolik chiqadi
# yosh_hisobla(1995, 'faxriddin')

#Xatolikni bartaraf etish uchun funktsiya argumentlarini kalit so'z bilan kiritishimiz kerak

# yosh_hisobla(t_yil = 1995, ism = 'faxriddin')

#Yuqoridagi holatda argumantlarni parametrlar ketma ketligida kiritmasak ham funktsiya ishlaydi
#Boshqa funktsiyalarni ham huddi shu kabi ishlatishimiz mumkun


#Funktsiya yaratish jarayonida istalgan parapetrga standart qiymat berib ketishimiz mumkun
#Bu holatda foydalanuvchi standart qiymat berilgan parametrga argument qiymat bermasa ham shlayveradi

# def yosh_hisobla(t_yil, joriy_yil = 2025):#Funksiya argumentiga standart qiymat berib kiritayapmiz
#     """Foydalanuvchi tug'ilgan yiliga qarab uni yoshini
#     hisoblovchi funktsiya kiritayapmiz"""
#     print(f'siz {joriy_yil - t_yil} yoshdasiz')#Konsolga chiqadigan habar
# yosh_hisobla(1995, 2025)

# #Endi funktsiyani standart qiymat berilgan parametr argumentisiz ya'niy joriy yilsiz kiritamiz
# yosh_hisobla(1995)

#Ikkala holatda ham bir hil natija chiqadi
#Faqatgina standart qiymat berilgan parametr funktsiya kiritilayotganda oxirida yozilishi kerak
#Aks holda hatolik chiqadi



#AMALIYOT
#1.Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

# def t_yilni_top(ism, yosh, joriy_yil = 2025):
#     """Foydalanuvchi ismini yoshini kiritganda 
#     unng tug'ilgan yilini hisoblaydigan funksiya"""
#     print(f'{ism.title()} {joriy_yil - yosh} da tug\'ilgan')
# t_yilni_top('hasan', 30)   


#2.Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def son_kirit(son):
#     """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi kunktsiya"""
#     print(f'{son} ning kvadrati: {son**2} ga teng. \n'
#           f'{son} ning kubi: {son**3} ga teng.')
# son_kirit(3)



#3.Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def son_kirit(son):
#     """Kiritilgan sonni juft yoki oq ekanligini aniqlovchi funktsiya"""
#     if son%2 == 0:
#         print(f'{son} uft son')
#     else:
#         print(f'{son} toq son')
# son_kirit(37)



#4.Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def sonlar_kirit(x, y):
#     """Kiritilgan sonlarni kattasini chiqaruvchi, 
#     sonlar teng bo'lsa sonlar teng degan matin chiqaruvchi funktsiya"""
#     if x>y:
#         print(f'{x}>{y}')
#     elif x<y:
#         print(f'{y}>{x}')
#     else:
#         print('Sonlar teng:')
# sonlar_kirit(123, 23)
# sonlar_kirit(25, 69)
# sonlar_kirit(55, 55)


#5.Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# def daraja(x, y):
#     """x ning y darajasini chiqaruvchu funktsiya"""
#     print(f'{x} ning {y}-darajasi {x**y:,} ga teng')
# daraja(15, 12)
# daraja(3, 9)

#6.uqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def daraja(x, y=5):
#     """x ning y darajasini chiqaruvchu funktsiya"""
#     print(f'{x} ning {y}-darajasi {x**y:,} ga teng')
# daraja(15)
# daraja(3)



#7.Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
def sonni_nisbatla(son):
    """Sonni 2 dan 10 gacha qoldiqsiz bo'linishini tekshirish"""
    for sonlar in range(2,10):
        if son%sonlar == 0:
            print(f'{son} soni {sonlar} ga qoldiqsiz bo\'linadi.')
        else:
            print(f'{son} ni {sonlar} ga bo\'lgandagi qoldiq {son%sonlar} ga teng.')
sonni_nisbatla(23)
sonni_nisbatla(24)
    
