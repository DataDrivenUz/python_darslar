# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 13:22:43 2025

Mavzu:Obyekt va klaslar

@author: f.mamadiev
"""
# Biz dasturlashga ilik qadam qo'yganimizda foydalanuvchidan biror o'zgaruvchini qabul qilib u o'zgaruvchilar ustida turli arfimetik amallar 
# bajarib uning nadijasini olganmiz
# Bunday dasturlar matemetik yohud klassik dasturlar deyiladi
# Klassik dastrurlar kichkina dasturlarda yoki o'zgaruvchilar soniakam bo'lgan dasturlarda qo'l kelishi mumkun
# O'zgaruvchilar va funktsiyalar soni ko'paygan dasturlarda klassik dasturlar ish bermay qoladi
# Bunday holatda biz obyektga yo'naltirilgan dasturlardan foydalanishimiz kerak bo'ladi

# Obyektga yonaltirilgan dasturlash bu bo'g'liq o'zgaruvchilar va funktsiyalarni bitta konteynerga joylashtiradi
# Bu konteyner ichidagi o'zgaruvchilar dasturning xususityatlari funktsiyalar esa metodlari deyiladi

# Misol sifatida aftomabilni ko'radigan bo'lsak
# Avtomabilning rangi, modeli, narhi uning hususiyatlariga misol bo'ladi
# stop(), start(), teslashish() uning metodlari deyiladi 

# real hayotda dasturlar o'nlab baylki yuzlab obyektlar bo'lishi mumkun va bu obyektlarda qatiy ketma-ketlik tushunchasi nisbiy
# Yani foydalanuvchi istalgan obyektga birinchi bo'lib murojat qilishi mumkun
# Yoki bitta obyektga murojat qilib boshqalarini faollashtirishi mumkun

# Obyektga yo'naltirilgan dasturlash aqida gapirar ekanmiz klaslarga to'xtalmaslikning iloji yo'q
# Klas bu obyektlar yaratish uchun shablon hisoblanadi
# Bitta klasdan yuzlab obyektlar yaratib olishimiz mumkun
# Masalan avtomabil nomli klas yaratib undan yuzlab, minglab abyektlar yaratish mumkun
# Klas nomi o'zgarmas bo'lib undan yaratilgan obyektlar esa turli hil no,larda bo'lishi mumkun
# Avromabil nomli klas yaratganimisda bu klas o'zgarmas bo'adi undan nusha olib laseti, malyubu, honda va hokazo nomli abyektlar yaratishimiz mumkun


# Obyektga yo'naltirilgan dasturlashda biz obyektga tegishli bo'lgan matod va hususiyat xususiyatlarni bitta kotenerga joylashtirib kelajakda undan klaslar yaratishda foydalanishimiz mumkun
# Dasturlashda bu jarayon INKAPSULYATSIYA deyiladi

# ABSTRAKTSIYA
# Abstraktsiyada biz kodimiz va uning ichki tuzilishini yashirishimiz mumkun
# Tashqaridan qaraganimizda kodimiz ikkita parametr va ikkita metoddan iboratdek ko'rinadi 
# lekin uning ichida o'nlab funktsiya va o'zgaruvchilar bo'lishi mumkun
# Klaslardan foydalanishda bizga kodning ichini to'liq bilishimiz unchalik muhum emas

# Dasturlash jarayonida biz bir klasdan birnechta klas yaratib olishimiz mumkun
# Masalan transport nomli klas yaratib undan avtomabi, avtobus, kema, poyez nomli klaslar yaratib olishimiz mumkun
# Bunda transport klasi ota klas yoki super klas deb ataladi undan yaratilgan klaslar esa voris klaslar deb ataladi


# KLASLAR YARATISH
# Klas yaratishda klass operatoridan foydalanamiz va unga Tushunarli nom beramiz
# Klas bu obyekt emas obyekt yaratish uchun shablon edi
# Shu sababli obyektlarga tegishli bo'lgan umumiy hususiyat va funktsiyalarni o'ylashimiz kerak
# Klass yaratayotganimizda klas nomi katta harfda berganimiz maqul

# Talaba nomli klass yarataylik
# =============================================================================
# class Talaba:#klass yaratayotganimizda class operatoridan foydalanamiz va klasnomimi katta harfda boshlaymiz
#       """Talaba nomli klass yaratayapmiz"""
#       def __init__(self, ism, familiya, tyil):#def __init__(self) klasga tegishli xususiyatlarni saqlovchi mahsus metod(funktsiya)
#       #Yaratayotgan klasimizga hos xususiyatlarni def __init__(self) funksiya argumenti sifadida uzatayapmiz 
#       #Talaba nomli klasimiz ism, familiya, tyil xususiyatlariga ega
#           """Talabaning xususiyatlari"""
#           self.ism = ism#Uzatilgan argumentni klassning xususiyati bilan bog'layapmiz
#           self.familiya = familiya#Uzatilgan argumentni klassning xususiyati bilan bog'layapmiz
#           self.tyil = tyil#Uzatilgan argumentni klassning xususiyati bilan bog'layapmiz
#           #Bu yerda uzatilgan argument classning xususiyatiga teng bo'lishi shart emas
# 
# # Klassimizdan bir nechta obyekt yarataylik
# talaba1 = Talaba("Avaz", "Olimov", 1985)
# talaba2 = Talaba("Olim", "Avazov", 1987)
# talaba3 = Talaba("Eshmat", "Toshmatov", 1990)
# #Yaratgan klasimiznad istalgancha obyekt yaratishimiz mumkun
# # Endi bu obyektlarimizni xususiyatlarini ko'raylik
# print(talaba1.ism)
# print(talaba2.familiya)
# print(talaba3.tyil)
# =============================================================================

      
# =============================================================================
# # Klass yaratib oldik va u orqali obyektlar ham yaratdik
# # Endi klasimizga metod(funktsiya) qo'shishni ko'raylik
# class Talaba:  # Klass yaratayotganimizda class operatoridan foydalanamiz
#     """Talaba nomli klass yaratayapmiz"""
#     
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism  # Uzatilgan argumentni klassning xususiyati bilan bog'layapmiz
#         self.familiya = familiya
#         self.tyil = tyil
#     
#     def tanishtir(self):
#         """Talabaning ma'lumotlarini chiqaruvchi metod"""
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tug'ilganman.")
# 
# # Yangi obyekt yaratamiz va uning metodlariga murojaat qilamiz
# talaba4 = Talaba("Hasan", "Husanov", 1990)
# talaba4.tanishtir()
# =============================================================================


# =============================================================================
# # Klasimiz bir nechta metodlar(funktsiyalar)dan ham iborat bo'lishi mumkun
# class Talaba:  # Klass yaratayotganimizda class operatoridan foydalanamiz
#     """Talaba nomli klass yaratayapmiz"""
#     
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism  # Uzatilgan argumentni klassning xususiyati bilan bog'layapmiz
#         self.familiya = familiya
#         self.tyil = tyil
#         
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#     
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#     
#     def get_fulname(self):
#         """Talabaning to'liq ismini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
#     
#     def tanishtir(self):
#         """Talabaning ma'lumotlarini chiqaruvchi metod"""
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tug'ilganman.")
#         
# talaba5 = Talaba("Avaz", "Olimov", 1985)
# print(talaba5.get_name())#talaba5 obyektini ismini chiqaradi
# print(talaba5.get_lastname())#talaba5 obyektini familiyasini chiqaradi
# print(talaba5.get_fulname())#talaba5 obyektini to'liq ismini chiqaradi
# talaba5.tanishtir()#obyekt haqidato'liq ma'lumotlarni chiqaradi
# =============================================================================


# =============================================================================
# # Yuqoridagi misoldabarcha fmetodlaf faqatgina self paramatrini qabul qilishayapdi
# # Aslida klass ichidagi funktsiyalar ham argumentlar qabul qilishi mumkun
# class Talaba:  # Klass yaratayotganimizda class operatoridan foydalanamiz
#     """Talaba nomli klass yaratayapmiz"""
#     
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism  # Uzatilgan argumentni klassning xususiyati bilan bog'layapmiz
#         self.familiya = familiya
#         self.tyil = tyil
#         
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#     
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#     
#     def get_fulname(self):
#         """Talabaning to'liq ismini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
#     
#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil
#     
#     def tanishtir(self):
#         """Talabaning ma'lumotlarini chiqaruvchi metod"""
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tug'ilganman.")
# 
# talaba6 = Talaba("Mamadiyev", "Faxriddin", 1995)
# print(talaba6.get_age(2025))#Obyektning obyektini consolga chiqaradi
# =============================================================================


# Pythonda hechqanday vazifani bajarmaydigan pass operatori mavjud bo'lib bu operator klas ichidagi metod badani bo'sh bo'lganda ishlatiladi
# Masalan
class User:#User nomli klass yaratib olayapmiz
    def __init__(self, name, usrename, email):#klasning hususiyatlarini kiritib olayapmiz
        self.ism = name # Uzatilgan argumentni klassning xususiyati bilan bog'layapmiz
        self.username = usrename
        self.elektron_pochta = email
    
    def discrppt(self):
        pass
    
    def username(self):
        pass

# Yuqorida discrppt(self) va username(self) metodlarini badani hali tayyor emas bo'shliqni to'ldirish uchun esa pass operatoridan foydalandik
