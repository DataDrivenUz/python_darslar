# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:04:53 2025

MAVZU: FUNKTSIYAGA RO'YHAT UZATISH

@author: 123
"""

# Biz oldingi darslarda funktsiyaga parametr sifatida yagona qiymat berayotgan edik
# Aslida funktsiyalarga ro'yhat ham uzatish mumkun
#Keling quyidagi misolimizni ko'ramiz
#Bu yerda funktsiya ro'yhatdagi har bir talabani baholashni so'raydi
#Va kiritilgan natijalar bilan birgalika ttalabalar va ularning bahosidan lug'at yaratib oladi
# def bahola(ismlar):#Ro'hatdagi talabalerni baholash uchun funktsiya kiritib olayapmiz
#     """Ro'yhatdagi talabalarni baholaovchi va lug'at yaratuvchi funktsiya"""
#     baholar = {}#Bosh ro'yhat yaratib olayapmiz
#     while ismlar:#Toki ismlar ro'yhatida element bor ekan
#         ism = ismlar.pop()#ismlar ro'yhatidan oxirgi elementni sug'urib olib ism o'zgaruvchisiga yuklaydi
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")#Talabaning bahosini kiritishni so'rayapmiz
#         baholar[ism] = int(baho)#ismni baholar ro'yhatining kalit elementi qo'yilgan bahoni qiymati sifatid asaqlayapmiz
#     return baholar#Baholar lug'atini qaytarayapmiz
# talabalar = ['faxriddin', 'umidjon','sarvar', 'xayrullo', 'sherzod']#Talabalar ro'yhati
# #Bu yerda talabalar va ismlar bitta ro'yhatga bog'lanayapdi
# baholar = bahola(talabalar[:])#Talabalar ro'yhatining nushasini funktsiya parametriga kiritayapmiz va baholar o'zgaruvchisiga yuklayapmiz
# print(baholar)#Natijani elon qilayapmiz
# print(talabalar)#Talabalar ro'yhatining nushasi bilan ishlaganimiz uchun talabalar ro'yhati bo'shab qolmaydi
    


# AMALIYOT
# 1-MASALA
# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.
# def katta_harf(matinlar):#Funktsiya kiritib olayapmiz
#     """Ro'yhatdagi matinni bitinchi harfini katta harfda chiqaruvchi funktsiya"""
#     for i in range(len(matinlar)):
#         matinlar[i] = matinlar[i].title()
#     return matinlar
# ismlar = ['faxriddin', 'umidjon','sarvar', 'xayrullo', 'sherzod']
# mijozlar = katta_harf(ismlar[:])
# print(mijozlar)
# print(ismlar)


# 2-masala
def bahola(ismlar):#Funktsiya kiritib olayapmiz
    """Ro'yhatdagi talabalarni baholaovchi va lug'at yaratuvchi funktsiya"""
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar
talabalar = ['faxriddin', 'umidjon','sarvar', 'xayrullo', 'sherzod']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)