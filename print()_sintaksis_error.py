# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:14:55 2025

@author: f.mamadiev
"""

print("Assalomu alaykum!") #Matinni consolda chiqarish uchun print funksiyasini ichida matinni qo'shtirnoq "" yoki '' ichiga yozilishi kerak
#print(Assalomu alaykum!) bu ko'rinishda yozadigan bo'lsak consolda sintaksis error chiqadi

print('Men bugun "Dell" markali noutbuk sotib oldim')#Agar matinda biror jumla qo'shtirnoq ichida yozilgan bo'lsa print ichidagi jumlani bir tirnoq ichida yozishimiz kerak

print("""Odami ersang, demagil odami,
Oniki, yo'q xalq g'amidin g'ami""") #Agar matinni bir nechta qatorda yozmoqchi bo'lsak matinni 3 ta qo'shtirnoq ichiga yozishimiz kerak

print("Yurtim senga sher bttim bugun \nQiyosingni topmadi aslo") #Qatorlarni bo'lishni yana bir usuli qbo'lmoqchi bo'lgan joyimiz oldiga \n belgisini qo'yishimiz kerak

print('Odami ersang, demagil odamiy \nOniki yo\'q xalq g\'amidan yo\'q g\'ami') #matinlarni kiritishda bir ham bir tirnoq g' o' hariflarini ishlatish uchun g\' o\' kabi kiritishimiz kerak


#Matematik amallar:
print(9+6) #qo'shish
print(19-7) #Ayirish
print(5*3) #Ko'paytirish
print(20/6) #Bo'lish, natija har doim o'nli kasrda chiqishi uchun bo'lishda / belgisidan foydalanamiz
print(20//6) #Bo'lish, bo'linmaning butun qismini chiqarish uchun bo'lishda // belgisini ishlatamiz
print(20%6) #Bo'linmaning qo'dig'ini topish uchun % belgisini ishlatamiz
print(8**3) # 8 ning uchunchi darajasi. Sonning darajasini ifodalash uchun ** belgisidan foydalanamiz

#VAZIFALAR
print("\"Neksiya\", Tiko, 'Damas', ko'rganlar qilar havas")

#5 ning 4 darajafi
print("5 ning 4-darajasi", 5**4, "ga teng")

#22 ni 4 ga bo'lgandagi qoldiq
print("22 ni 4 ga bo'lgandagi qoldiq", 22%4, "ga teng")

#Tomonlari 125 ga teng bo'lgan kvadratning yuzi va peremetri
print("Tomonlari 125 ga teng bo'lgan kvadratning yuzi", 125**2, "ga teng. \nPeremetri", 4*125, "ga teng")

#Diametri 12 ga teng bo'lgan doiyaning yuzi va aylana uzunligi
print("Diametri 12 ga teng bo'lgan doiraning yuzi", 3.14*(12/2)**2, "ga teng. \nAylana uzunligi", 3.14*12, "ga teng")

#Katetlari 6 va 7 ga teng bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi
print("Katetlari 6 va 7 ga teng bo'lgan tog'ri burchaklu uchburchakning gipotenuzasi", (6**2+7**2)**(1/2), "ga teng")