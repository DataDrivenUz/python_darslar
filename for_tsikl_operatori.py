# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:56:31 2025

Mavzu:For tsikl(takrorlash) operatori

@author: f.mamadiev
"""
#Dasturlash davomida kodimizning biror qissmini bir necha bor takrorlashga to'g'ri kelishi mumkun.
#Masalan sonlar ro'yhatidagi har bir elementni kvadratga ko'tarishga to'g'ri kelishi mumkun.
#Shu va shunga o'xshash boshqa takrorlanuvchi holatlarda for operatoridan foydalanamiz

# # Masalan:
# # Mehmonlar ro'yhati tuzib olinayapdi
# mehmonlar = ['Hasan', 'Yo\'ldosh', 'Karim', 'Sobir', 'Xikmat', 'Vali']
# #Operator boshlanayapdi. Yani mehmon degan o'zgaruvchiga mehmonlar ro'yhatidagi har bir elementni yuklaydi
# for mehmon in mehmonlar:
#     #Mehmon o'zgaruvchisi mehmonlar r'yhatidagi har bir elementni olib elon qilinayapdi
#     print(mehmon)
    
#Yuqoridagi kodimizda for mehmon in mehmonlar: kodimiz siklning boshlanishi  print(mehmon) esa siklning tanasi deyiladi.
#Agar sikl tanasi sikl boshlanishidan o'ngroqda turmasa sikl ishlamaydi. Yuqoridagi kodda print(mehmon) elon qiluvchi mehmonlar ro'yhatidagi har bir elementni alohida alohida elon qiladi

#Yuqoridagi ro'yhatimiz misolida yana bitta amaliyot bajaramiz
# mehmonlar = ['Hasan', 'Yo\'ldosh', 'Karim', 'Sobir', 'Xikmat', 'Vali']
# # #Siklni boshlaymiz
# for mehmon in mehmonlar: #Sikl boshlandi. Mehmonlar ro'yhatidagi har bir elementni mehmon o'zgaruvchisiga yuklayapdi
# #     #mehmon o'zgaruvchisini har birini nahor oshga taklif qilish buyrug'ini elon qilayapdi
#     print(f'Salom {mehmon}, sizni 20 dekabr kuni soat 07:00 ga Nahor oshiga teklif etamiz.\n')
# #     #Kim taklif qilayotgani elon qilinayapdi
#     print("Hurmat bilan Mamadiyevlar xonadoni!")
    
# #Agar sikl tanasi for dan o'ngroqda turmasa buyruq sikldan chiqib ketadi va sikl bajarilmaydi
# #Agar sikl tanasida bir nechta buyruq bersak va birortasini fordan o'nga surmasak o'ng surilgan kod uchun sikl ishlaydi o'ng surilmagan kod uchun ishlamayri
# #Masalan
# mehmonlar = ['Hasan', 'Yo\'ldosh', 'Karim', 'Sobir', 'Xikmat', 'Vali']
# #Siklni boshlaymiz
# for mehmon in mehmonlar: #Sikl boshlandi. Mehmonlar ro'yhatidagi har bir elementni mehmon o'zgaruvchisiga yuklayapdi
#     #mehmon o'zgaruvchisini har birini nahor oshga taklif qilish buyrug'ini elon qilayapdi
#     print(f'Salom {mehmon}, sizni 20 dekabr kuni soat 07:00 ga Nahor oshiga teklif etamiz.\n')
# #Tepadagi print uchun sikl takrorlanadi bu kod uchun esa takrorlanmaydi
# print("Hurmat bilan Mamadiyevlar xonadoni!")


#FOR YORDAMIDA SONLI RO'YHATLAR BILAN ISHLASH
#1 dan 10 gacha sonlar ro'yhati yaratilayapdi
# sonlar = list(range(1,11))
# #Sikl boshlanayapdi. Sonlar ro'yhatidagi har bir elementni son o'zgaruvchiga yuklayapdi
# for son in sonlar:
#     #Yuklangan har bir elementning 2vadratini hisoblab elon qilayapdi
#     print(f'{son} ning kvadrati {son**2} ga teng')

#For yordamida yangi ro'yhat ham yaratish mumkun
#masalan
#1 dan 10 gacha bo'lgan sonlar ro'yhati yaratilayapdi
# sonlar = list(range(11))
# # #Bosh ro'yhat yaratilayapdi
# sonning_kvadrati =[]
#Sonlar ro'yhatidagi har bir element son o'zgaruvchisiga yuklanayapdi
# for son in sonlar:
#    #sonning kvadrati degad ro'yhatga sonlar ro'yhatidagi har bir elementning kvadratini yuklayapdi
#      sonning_kvadrati.append(son**2)
# # #Sonlar va sonning kvadrati ro'yhatini elon qilayapdi
# print(sonlar)
# print(sonning_kvadrati)


#for va input 
#for va input funksiyalarini jamlab ro'yhatni fordalanuvchi kiritgan ma'lumotlar bilan ham to'ldirish mumkun
#Do'stlar degan yangi bo'sh ro'yhat yaratilayapdi
# dostlar = []
# # #Sikl boshlanayapdi. Unda n uchun 0 dan 5 gacha (5 kirmaydi) sonlar yuklanayapdi
# for n in range(5):
# #     #Do'stlar ro'yhatiga n+1 do'stni kiritish so'ralayapdi va kiritilgan malumotning har biri do'stlar ro'yhatiga qo'shilayapdi
# #     #n 0 dan boshlanganligi uchun n+a kiritilayapdi
# #     #Bu sikl foydalanuvchi n ning hamma qiymatlariga ma'lumot kiritib bo'lgandan keyin tugaydi
#      dostlar.append(input(f'{n+1}-do\'stingizni kiriting\n>>>'))
# # #To'ldirilgad do'stlar ro'yhatini elon qilayapdi
# print(dostlar)


#AMALIYOT
#1-MASALA
# ismlar = ['Anvar', 'Dilshod', 'Begzod', 'Sodiq', 'Xurshid', 'Jaxongir', 'Farrux']
# for ism in ismlar:
#     print(f'Assalomaleykum {ism} sizni 20-mart soat 09:00 da Navruz bayramiga taklif qilamiz!')
#     print('Xurmat bilan Ingo-Uzbekistan jamoasi\n')
    
# print('Yuqoridagi sikl tugagandan so\'ng kod', len(ismlar), 'marta takrorlanadi')

# #2-MASALA
# toq_sonlar = list(range(11, 100, 2))
# for son in toq_sonlar:
#     print(f'{son} ning kubi {son**3} ga teng')


# #3-masala
# kinolar = []
# print("5 ta enf yaxshi ko'rgan kinoyingiz qaysilar")
# for n in range(5):
#     kinolar.append(input(f'{n+1}-eng yaxshi ko\'rgan kinoyingizni kiriting\n>>>'))
# print(kinolar)


# #4- masala
# #Foydalanuvchi kiritgan sonni butun songa o'tkazib olayapmiz
# n_odamlar = int(input('Bugun nechta odam bilan uchrashdingiz\n>>'))
# #Bo'sh ro'yhat yaratib olayapmiz
# suhbatlashganlar = []
# #Sikl boshlanayapdi n uchun n_odamlar o'zgaruvchisidan kiritilgan sonni yuklayapdi
# for n in range(n_odamlar):
#     #Bo'sh ro'yhatga foydalanuvchi kiritgan odamlarni qo'shayapdi
#     suhbatlashganlar.append(input(f'{n+1}-suhbatlashgan odamingiz\n>>>'))
# #Royhatni elon qilayapdi
# print(suhbatlashganlar)

