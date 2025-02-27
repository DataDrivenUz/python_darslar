# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 08:39:11 2025

@author: f.mamadiev
"""

def afto_info(kompaniya, model, rangi, korobka, yili, narhi=None):#Parametrlarni kiritib oldik
      """Avtomabil haqidagi ma'lumotlar lug'atini qaytaruvchi funktsiya"""
      avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
      return avto
  
    

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni 
       bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    avtolar = [] #Bo'sh lug'at yaratib olayapmiz
    while True:#Abadiy tsikl
          print('Quyidagi ma\'lumotlarni kiriting: ', end = ' ')#Habar chiqarayapmiz
          kompaniya = input('Ishlab chiqaruvch: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
          model = input('Model: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
          rangi = input('Rangi: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
          korobka = input('Korobka: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
          yili = input('Ishlab chiqarilgan yili: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
          narhi = input('Narhi: ')#Foydakanuvchidan ma'lumot kiritishini s'rayapmiz
          #afto_info funktsiyasi orqali har bir avtomabil uchun lug'at yaratib bu lug'atni avtolar ro'yhatiga qo'shamiz
          avtolar.append(afto_info(kompaniya, model, rangi, korobka, yili, narhi))
          #Yangi avto qo'shish qo'shmaslikni so'raymiz
          javob = input('Yangi avto qo\'shasizmi? (yes/no) ')#Foydalanuvchidan javob olayapmiz
          if javob == 'no':#Agar javob no bo'lsa
             break#tsikl to'xtaydi
            
            
            
def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")
    
