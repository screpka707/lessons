# x = int(input("Введите сторону квадрата: "))
# per = x*4
# plo = x*x
# print(plo)
# print(per)
import copy

# print(2**10)

# print(101%10)

# a = 111 // 19
# print(a)

# a = int(input('введите число: '))
# b = int(input('Введите число2: '))
# print((a * b) ** 0.5)

# a = int(input('введите число: '))
# b = int(input('введите число2: '))
# print((a ** 2 + b ** 2) ** 0.5)
#
# a = 5
# b = 10
# print((a + b)* 2)
# print(a * b)

# print(60*60*24*7)

# print(111 %19)
#
# print(23 // 10)

# a = int(input('Введите число: '))
# b = int(input('Введите число2: '))
# print((a + b) * 2)
# print(a * b)

# a = int(input('ваше число: '))
# print(a // 100)

# x = int(input('число: '))
# # print(x ** 2 - x + 3)

# x = int(input('ваше число: '))
# print(x ** 9)

# a = int(input(' ваше число: '))
# a1 = a // 100
# a2 = a // 10 % 10
# a3 = a % 10
# print(a1 + a2 + a3)

# a = float(input(' first number: '))
# b = float(input(' second number: '))
# print(int(a) + int(b) )p

# print('hello' * 100)

# a = float(input('enter '))
# print((int(a * 100) % 10) + (int(a *10) % 10))

# a = float(input('enter number' ))
# print(int(a))
# x = 'int - это целочисленный тип данных'
# # print(x.count(' '))

# a = 'Иванов'
# b = 'Степан'
# c = 'Александрович'
# print(f'{a[0]}.{b[0]}.{c[0]}.')

# a = int(input('enter: '))
# b = int(input('enter2: '))
# if a > b:
#     print(a)
# else:
#     print(b)

# a = int(input('enter: '))
# if a > 0:
#     print(a + 3)
# elif a == 0:
#     print(a + 1)
# else:
#     print(a - 2)

# a = int(input('enter: '))
# b = int(input('enter1: '))
# c = int(input('enter2: '))
# if a < 0 or b < 0 or c < 0:
#     print(1)
# elif a < 0 and b < 0 and c < 0:
#     print(3)
# else:
#     print(2)
#
# a = -10
# if a % 2 == 0:
#     print(1)
# else:
#     print(0)

# a = int(input('health: '))
# if a <= 0:
#     print(0)
# else:
#     print(1)

# x = input('Enter: ')
# if len(x) ==  4 and x.isdigit():
#     print(1)
# else:
#     print(0)

# x = input('Enter: ')
# if x[::-1] == x:
#     print(1)
# else:
#     print(0)

# a = int(input('Enter: '))
# b = a ** 0.5
# if b % 1 == 0:
#     print((b + 1) ** 2)
# else:
#     print(-1)

# a = int(input('Enter: '))

# a = int(input('Enter: '))
# b = int(input('Enter2: '))
# if a % 2 == 0 or b % 2 == 0:
#     print(a * 10 + b)
# else:
#     print(a + b)

# a = int(input('Enter: '))
# b = int(input('Enter1: '))
# c = int(input('Enter2: '))
# if a == b and a == c  and b == c:
#     print(3)
# elif a == b or a == c or b == c:
#     print(2)
# else:
#     print(0)

# a = int(input('Enter: '))
# # if a % 4 == 0 and not a % 100 == 0 or a % 400 == 0:
# #     print(1)
# # else:
# #     print(0)

# a = int(input('Enter: '))
# b = int(input('Enter1: '))
# c = int(input('Enter2: '))
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# a = int(input('Enter: '))
# if (a // 100) % 2 == 0 and (a // 10 % 10) % 2 == 0 and (a % 10) % 2 == 0:
#     print(3)
#     elif

# year1 = int(input('Enter year1: '))
# year2 = int(input('Enter year2: '))
# month1 = int(input('Enter month1: '))
# month2 = int(input('Enter month2: '))
# day1 = int(input('Enter day1: '))
# day2 = int(input('Enter day2: '))
# if year1 < year2:
#     print(1)
# elif month1 < month2:
#     print(1)
# elif day1 < day2:
#     print(1)
# else:
#     print(2)

# a = int(input('Enter: '))
# a1 =  a // 100 % 2
# a2 = a % 10 % 2
# a3 = a // 10 % 10 % 2
# if a1 == 0 and a2 == 0 and a3 == 0:
#      print(3)
# elif (a1 == 0 and a2 == 0) or (a1 == 0 and a3 == 0) or (a2 == 0 and a3 == 0):
#     print(2)
# elif a1 == 0 or a2 == 0 or a3 == 0:
#     print(1)
# else:
#     print(0)


# a,b,c,d, = map(int, input('Enter: ').split())
# if a != b and a != c and a != d:
#     print(a)
# elif a != b and a == c and a == d:
#     print(b)
# elif a == b and a != c and a ==d:
#     print(c)
# else:
#     print(d)

# x1 = int(input('Enter x 1: '))
# y1 = int(input('Enter y 1: '))
# x2 = int(input('Enter x 2: '))
# y2 = int(input('Enter y 2: '))
# if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
#     print(1)
# else:
#     print(0)

# x1 = int(input('Enter x 1: '))
# y1 = int(input('Enter y 1: '))
# x2 = int(input('Enter x 2: '))
# y2 = int(input('Enter y 2: '))
# if abs(x1 - x2) == abs(y1 - y2):
#     print(1)
# elif abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 or x1 == x2 or y1 == y2:
#     print(1)
# else:
#     print(0)

# a = int(input('Enter: '))
# b = int(input('Enter1: '))
# c = int(input('Enter2: '))
# if a + b > c and a + c > b and b + c > a:
#     print('Можно')
# else:
#     print('Нельзя')

# num = int(input('Enter: '))
# n1 = (num // 1000) ** 2
# n2 = (num // 100 % 10) ** 2
# n3 = (num // 10 % 10) ** 2
# n4 = (num % 10) ** 2
# print(str(n1) + str(n2) + str(n3) + str(n4))

# x = 89987654321
# s1 = str(x)
# print(f'+7 ({s1[1:4]}) {s1[4:7]}-{s1[7:9]}-{s1[9:]}')

# x1 = int(input('Enter x1: '))
# y1 = int(input('Enter y1: '))
# x2 = int(input('Enter x2: '))
# y2 = int(input('Enter y2: '))
#
# if x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
#     print(1)
# else:
#     print(0)

# a = input('Enter: ')
# if len(a) >= 8 and not a.isdigit() and not a.isalpha() and a.isupper() and a.islower():
#     print('Хороший')
# elif len(a) >= 8 and a.islower() and not a.isalpha():
#     print('Средний')
# elif len(a) >= 8 and (a.isalpha() or a.isdigit()):
#     print('Слабый')
# else:
#     print('Очень слабый')

# a,b = map(int,input('Enter: ').split(' '))
# for i in range(a,b + 1):
#     print(i,end =' ')

# N = int(input('Enter: '))
# reg = 0
# for i in range(1,N + 1):
#     reg += i
# print(reg)

# a,b= map(int,input('Enter: ').split())
# reg = 0
# for i in range(a,b + 1):
#     if i % 2 == 0:
#         reg += i
# print(reg)

# n = int(input('Enter: '))
# reg = 0
# for i in range(1,n + 1):
#     if i % 3 == 0:
#         reg += i
# print(reg)

# n = int(input('Enter: '))
# reg = 0
# for i in range(1,n):
#     reg += i * (i + 1)
# print(reg)

# a = int(input('Enter: '))
# b = int(input('Enter1: '))
# zn = str(input('enter sign: '))
# if zn == "+":
#     print(a + b)
# elif zn == "-" :
#     print(a - b)
# elif zn == "*":
#     print(a * b)
# else:
#     print(a / b)
#
# n = int(input('Enter: '))
# reg = 1
# for i in range(1,n + 1):
#     reg /= i
# print(round(reg,4))

# n = int(input('Enter: '))
# reg = 0
# for i in range(1,n + 1):
#     reg += i ** i
# print(reg)

# n = int(input('Enter: '))
# reg = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         reg -= i ** i
#     else:
#         reg += i ** i
# print(reg)

# a =int(input('Enter1" '))
# b =int(input('Enter2" '))
# i = a
# while i < b + 1 and i >= a:
#     print(i)
#     i += 1

# n = int(input('Enter: '))
# i = 0
# reg = 0
# while i <= n:
#     reg += i
#     i += 1
# print(reg)

# a =int(input('Enter1: '))
# b =int(input('Enter2: '))
# reg = 0
# while a > b:
#     a -= b
#     reg += 1
# print(reg,a)

# n = int(input('Enter: '))
# factor = 1
# res = 0
# for i in range(1, n + 1):
#      factor = factor * i
#      if i % 2 == 0:
#          res -= factor
#      else:
#          res += factor
# print(res)

# n = int(input('Enter: '))
# reg = 0
# while n > 2 ** reg:
#     print(2 ** reg, end = ' ')
#     reg += 1
#
# N = 15
# res = 0
# while N > 0:
#     lst = N % 10
#     N = N // 10
#     res *= 10
#     res += lst
# print(res)
#
# N = 100
# while N > 0:
#     if N % 2 == 0 or N % 3 == 0:
#         print(0)
#         break
#     else:
#         print(1)
#         break

# N = int(input('Enter: '))
# i1 = 1
# i2 = 1
# print(i1,i2, end = ' ')
# while N > i2:
#     i1, i2 = i2, i1 + i2
#     print(i2, end = ' ')

# n = int(input('enter: '))
# factor = 1
# x = int(input('enter: '))
# res = 1 + x
# for i in range(2, n + 1):
#     factor *= i
#     res += x ** i / factor
# print(round(res, 5))

# a = int(input('enter: '))
# b = int(input('enter: '))
# res = 0
# i = 1
# while 0 < a :
#     res += a ** b
#     a -= 1
# print(res)

# a = 'hello'
# b = list(a)
# c = b[0]
# print(c)

# a = [input(),input(),input()]
# print(a[0],a[-1])

# n = []
# num = 3
# i = 1
# while num > 0:
#     n.append(i)
#     i += 2
#     num -= 1
# print(n)

# n = [int(input()),int(input()),int(input()),int(input())]
# res =  n[0] + n[1] + n[2] + n[3]
# print(res / 4)

# n = int(input('Enter:'))
# a = []
# res = 0
# for i in range(n):
#     a.append(int(input('Enter: ')))
# for k in a:
#     if k > res:
#         res = k
# print(res)

# n = int(input('Enter:'))
# a = []
# res = 0
# for i in range(n):
#     a.append(int(input('Enter: ')))
# for k in a:
#     if k < res:
#         k = res
# if a % 2 != 0:
#     print(1)
# else:
#     print(0)
#
# vod1 = int(input('Enter: '))
# vod2 = input('Enter word: ')
# for i in range (1,vod1 + 1):
#     print(vod2)

# vod = int(input('размер списка:'))
# l = []
# for i in range(vod):
#     l.append(input('номер товара: '))
# for j in l:
#     print(j)
#
# a = []
# n = int(input('Enter: '))
# res = 0
# for i in range(n):
#     a.append(int(input('Enter1: ')))
# for j in a:
#     res += a.count(j) - 1
# print(res // 2)

# a = []
# n = int(input('Enter size: '))
# res = 0
# for i in range(n):
#     a.append(float(input('Enter number:')))
# for j in a:
#     res += j
# print(res / n)

# n = int(input('Enter: '))
# n = str(n)
# res = 0
# currentInd = 0
# for i in range(1,len(n)):
#     if abs (int(n[currentInd]) - int(n[i])) == 1:
#         res += 1
#     currentInd += 1
# if len(n) == res + 1:
#     print(1)
# else:
#     print(0)

# n = int(input())
# n = str(n)
# n_sered = len(n) // 2
# n_sered_l = n[:n_sered]
# res_l = 0
# res_r = 0
# if len(n) % 2 != 0:
#     n_sered += 1
# n_sered_r = n[n_sered:]
# for i in n_sered_l:
#     res_l += int(i)
# for j in n_sered_r:
#     res_r += int(j)
# if res_l == res_r:
#     print(1)
# else:
#     print(0)

# a1 = ['5','10','py']
# a2 = ['510','Python5','Java']
# a3 = []
# for i in a1:
#     for j in a2:
#         if i in j and i not in a3:
#             a3.append(i)
# print(a3)

# from math import *
# print(log(5))

# my_str = input('Введите шифр: ')
# alf = 'abcdefghijklmnopqrstuvwxyz'
# shifr = ''
# for letter in my_str:
#         if letter in alf:
#             shifr += alf[(alf.index(letter) + 13) % 26]
#         else:
#             shifr += letter
#
# from  math import *
# print(ceil(10.

# def temp(temp):
#     return temp * 1.8 + 32
# print(temp(0))

# def temp(temp):
#     return round((temp - 32) * (5/9),2)
# print(temp(42))

# def F_C(temp):
#     return round((temp - 32) * (5 / 9), 2)
#
#
# def C_F(temp):
#     return round((temp - 32) * (5 / 9), 2)


# def abc(temp,shkala):
#     if shkala == 'F':
#         res = F_C(temp)
#     elif shkala == 'C':
#         res = C_F(temp)
#     return res
# print(abc(int(input('Введите температуру: ')),input('Введите шкалу: ')))

# def abc(tekst):
#     temp = int(tekst[:-1])
#     shkala = tekst[-1]
#     if shkala == 'C':
#         return str(round(temp * 1.8 + 32, 2)) + 'F'
#     elif shkala == 'F':
#         return str(round((temp - 32) * (5 / 9), 2)) + 'C'
# print(abc('451F'))

# def addd(ch1,ch2):
#     return ch1 + ch2
# print(addd(451, -96))

# def abc(ch,sh):
#     if sh == 'f':
#         return str(round(ch * 1.8 + 32, 2)) + 'F'
#     elif sh == 'c':
#         return str(round((ch - 32) * (5 / 9), 2)) + 'C'
# print(abc(-191,'c'))

# def abc(chislo):
#     if chislo % 2 == 0:
#         return'Even'
#     elif chislo % 2 == 1:
#         return'Odd'
# print(abc(21))

# def slova(word:str):
#     if len(word) == 1:
#         return word
#     return word[-1] + slova(word[:-1])
# print(slova('!йыннежибо тёдйу ен откин ьтсуп и'))

# def odin(word:str):
#     if word[-1] == '1':
#         return word[:-1] + '!'
#     else:
#         return word
# print(odin('こんにちは、先生1'))

# def por(nas, igr = 3):
#     if nas % igr == 0:
#         return 0
#     else:
#         new_nas = 1
#         while (new_nas + nas) % igr != 0:
#             new_nas += 1
#         return new_nas
# print(por(311,9))
#
# import math
# def abc(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
# print(abc(-1,0,math.inf))

# def abc(ch):
#     return ch ** 2
# print(abc(-12))

# import random
# def roll_dice(gran):
#     return random.randint(1,gran)
# print(roll_dice(6))

# def dnk(chislo):
#     res1 = 0
#     res2 = 0
#     res3 = 0
#     res4 = 0
#     for i in chislo:
#         if i == 'A':
#             res1 += 1
#         elif i == 'T':
#             res2 += 1
#         elif i == 'C':
#             res3 += 1
#         elif i == 'G':
#             res4 += 1
#     return ' '.join([str(res1),str(res2),str(res3),str(res4)])
# print(dnk('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))

# def rnk(dnk):
#     res = ''
#     for i in dnk:
#         if i == 'T':
#             res += 'U'
#         else:
#             res += i
#     return res
# print(rnk('ATTTCAG'))

# def cg(strk):
#     res = 0
#     for i in strk:
#         if i == 'C' or i == 'G':
#             res += 1
#     return res / len(strk) * 100
# print(cg('TCGATCGCATGCCACCCCCTAGCGCGCTAGACAGCTTCTAGGCTA'))

# x = {"один":"one","два":"two","три":"three"}
# x["четыре"] = "four"
# print( "один" in x)

# def  ATCG(strk):
#     res = ''
#     dnk = {"A": "T","T" : "A","C":"G","G":"C"}
#     for i in strk:
#         res += dnk[i]
#     return res
# print(ATCG('TCGATCGCATGCCACCCCCTAGCGCGCTAGACAGCTTCTAGGCTA'))

# def slovar(strk):
#     x ={}
#     for i in strk:
#         if i in x:
#             x[i] += 1
#         else:
#             x[i] = 1
#     return x
# print(slovar('Mad Hatter'))

# import string
#
#
# def slovar(strk):
#     a = []
#     x = {}
#     strk = strk.translate(strk.maketrans('', '', string.punctuation))
#     for i in strk.split():
#         x[i] = x.get(i, 0) + 1
#     for key,value in x.items():
#         a.append((value,key))
#     return sorted(a,reverse=True)
#
#
#
# text = '''"Would you tell me, please, which way I ought to go from here?"
# "That depends a good deal on where you want to get to," said the Cat."
# "I don't much care where" - said Alice."
# "Then it doesn't matter which way you go," said the Cat."'''
# res = (slovar(text)[:5])
# # print(res)
# for l in res:
#     print(l[0],l[1])

# class Cat:
#     def speak(self,name):
#         self.name = name
#         print('Hello, my name is,', self.name)
#     def introduce_yourself(self):
#         print('My name is,', self.name,', and I am cat')
# murzik = Cat()
# murzik.speak('Murzik')
# murzik.introduce_yourself()
#
# print(murzik.name)

# class Animal:
#     def __init__ (self,name,age,kind):
#         self.name = name
#         self.age  = age
#         self.kind = kind
# class Cat(Animal):
#     def introduce_yourself(self):
#         print('My name is,', self.name,'I am',self.age,'years old',self.kind)
# class Dog(Animal):
#     def fas(self):
#         print('My name is,', self.name, 'I am', self.age, 'years old', self.kind)
# bobik = Dog('Bobik',52,'yuork')
# murzik = Cat('Murzik',5,'sfinks')
# bobik.fas()
# murzik.introduce_yourself()

# class Shop:
#     def __init__(self,*items):
#         self.stock = list(items)
#
#     def list_items(self):
#         output = 'В магазине:\n'
#         for item in self.stock:
#             if item.amount > 0:
#                 output += f'{item.name}:{item.amount}:{item.rarity}\n'
#         return output
#
#     def buy(self,ItemName,amount=1):
#         for item in self.stock:
#             if ItemName == item.name:
#                 item.decrease_amount(amount)
#                 break
#         else:
#             raise ValueError('Такого предмета нету')
#         item_copy = copy.deepcopy(item)
#         item_copy.set_amount(amount)
#         return item_copy
#
#
#     def sell_item(self,item,amount=1):
#         item.decrease_amount(amount)
#         for stock_item in self.stock:
#             if stock_item.name == item.name:
#                 stock_item.increase_amount(amount)
#                 break
#         else:
#             item_copy = copy.deepcopy(item)
#             item_copy.set_amount(amount)
#             self.stock.append(item_copy)
#
#
# class Item:
#     def __init__(self,name,amount,rarity='uncommon'):
#         self.name = name
#         self.amount = amount
#         self.rarity = rarity
#
#     def set_amount(self,value):
#         if value <= 0:
#             raise ValueError('Значение не может быть отрицательным')
#         else:
#             self.amount = value
#
#     def decrease_amount(self,value=1):
#         if self.amount - value >= 0:
#             self.amount -= value
#         else:
#             raise ValueError('Недостачно предметов')
#
#
#     def increase_amount(self,value=1):
#         if value < 0:
#             raise ValueError('Значение не может быть отрицательным')
#         else:
#             self.amount += value
# orange = Item('Orange',12)
# apple = Item('Apple',30)
# potato = Item('Potato',25)
# shop = Shop(orange,apple,potato)
# print(shop.list_items())
# shop.buy('Apple',15)
# print(shop.list_items())
# shop.sell_item(Item('tomato',20,'Arcana'),20)
# print(shop.list_items())


# import requests
# from bs4 import BeautifulSoup
# file = open('книжки.txt','w',encoding='UTF-8')
# for i in range(1, 51):
#     response = requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html').text
#     soup = BeautifulSoup(response, 'html.parser')
#     for book in soup.find_all('article', class_='product_pod'):
#         name = book.h3.a['title']
#         price = book.find('p', class_='price_color').text[1:]
#         rating = book.p['class'][-1]
#         file.write(f'Name: {name}\nPrice: {price}\nRating: {rating}\n\n')

# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'html.parser')

# for article in soup.find_all('div',class_ = 'article'):
#     headline = article.h2.a.text
#     summary = article.p.text
#     print(headline)
#     print(summary)
#     print('')


