# 1-misol
# from collections import namedtuple
#
# Talaba = namedtuple('Talaba', ['name', 'age', 'major'])
# talaba1 = Talaba(name='Ali', age=20, major='Matematika')
# talaba2 = Talaba(name='Ona', age=22, major='Fizika')
# talaba3 = Talaba(name='Sardor', age=21, major='Informatika')
#
# for talaba in [talaba1, talaba2, talaba3]:
#     print(f'Ism: {talaba.name}, Yosh: {talaba.age}, Mutaxassislik: {talaba.major}')

# 2-misol
# from collections import namedtuple
#
# Mahsulot = namedtuple('Mahsulot', ['nom', 'narx', 'miqdor'])
#
# mahsulot1 = Mahsulot(nom='Olma', narx=1000, miqdor=50)
# mahsulot2 = Mahsulot(nom='Banan', narx=1500, miqdor=30)
# mahsulot3 = Mahsulot(nom='Apelsin', narx=1200, miqdor=20)
# for mahsulot in [mahsulot1, mahsulot2, mahsulot3]:
#     print(f'Nom: {mahsulot.nom}, Narx: {mahsulot.narx}, Miqdor: {mahsulot.miqdor}')

# 3-misol
# from collections import namedtuple
#
# Shahar = namedtuple('Shahar', ['city_name', 'country', 'population'])
#
# shahar1 = Shahar(city_name='Toshkent', country='O\'zbekiston', population=25000)
# shahar2 = Shahar(city_name='Andijon', country='O\'zbekiston', population=120000)
# shahar3 = Shahar(city_name='fargana', country='O\'zbekiston', population=90000)
#
# largest_city = max([shahar1, shahar2, shahar3], key=lambda city: city.population)
# print(f'Eng katta shahar: {largest_city.city_name}, Aholisi: {largest_city.population}')

# 4-misol
# from collections import namedtuple
#
# Avtomobil = namedtuple('Avtomobil', ['make', 'model', 'year'])
#
# avtomobil1 = Avtomobil(make='coblt', model='GM', year=2020)
# avtomobil2 = Avtomobil(make='taho ', model='GM', year=2021)
# avtomobil3 = Avtomobil(make='onx', model='GM', year=2019)
#
# newest_car = max([avtomobil1, avtomobil2, avtomobil3], key=lambda car: car.year)
# print(f'Eng yangi avtomobil: {newest_car.make} {newest_car.model}, Yili: {newest_car.year}')

# 5-misol
# def outer_function():
#     def ichki_funktsiya():
#         return "Bu ichki funktsiya."
#     return ichki_funktsiya
# yopish_funktsiyasi = outer_function()
# print(yopish_funktsiyasi())

# 6-misol
# def salomlashish(name):
#     def greet():
#         return f'Salom, {name}!'
#     return greet
# greet_function = salomlashish("Husanboy")
# print(greet_function())

# 7-misol
# def d(x):
#     def add(y):
#         return x + y
#     return add
#
# a = d(5)
# print(a(10))

# 8-misol
# def counter():
#     a = 0
#     def b():
#         nonlocal a
#         a += 1
#         return a
#     return b
#
# d = counter()
# print(d())
# print(d())

# 9-misol
# def a():
#     return lambda x: x ** 2
#
# b = a()
# print(b(10))

# 10-misol
# def name_list_closure():
#     names = []
#     return lambda name: names.append(name) or names
# isim_qoshish = name_list_closure()
# print(isim_qoshish("hasan"))
# print(isim_qoshish("husan"))

# 11-misol
# def discount_closure(chegirma):
#     return lambda pul: pul - (pul * (chegirma / 100))
#
# q = discount_closure(10)
# print(q(200))

# 12-misol
# def product_multiplier():
#     mahsulot = 1
#     def multiply(number):
#         nonlocal mahsulot
#         mahsulot *= number
#         return mahsulot
#     return multiply
#
# a = product_multiplier()
# print(a(2))
# print(a(3))

# 13-misol
# def string_adder():
#     natija = ""
#     def add_string(string):
#         nonlocal natija
#         natija += string
#         return natija
#     return add_string
#
# qoshish = string_adder()
# print(qoshish("Hello"))
# print(qoshish(" World"))

# 14-misol

# def filter_odd_numbers():
#     def raqam(raqamlar):
#         return [num for num in raqamlar if num % 2 != 0]
#     return raqam
#
# filtr = filter_odd_numbers()
# print(filtr([1, 2, 3, 4, 5]))

# 150misol
# def exponent_function():
#     def kalkulyatr(base, korsatkich):
#         return base ** korsatkich
#     return kalkulyatr
#
# yechim = exponent_function()
# print(yechim(2, 3))

# 16-miso''

# def teskari_harf():
#     def taskari(s):
#         return s[::-1]
#     return taskari
#
# teskari_funksiya = teskari_harf()
# print(teskari_funksiya("hello"))


# 17-misol
#
# def arava_dokom():
#     jami = 0
#     def savatchaga_qoshish(pul):
#         nonlocal jami
#         jami += pul
#         return jami
#     return savatchaga_qoshish
#
# aracva = arava_dokom()
# print(aracva(1000))
# print(aracva(1200))


# 18-misol

# def product_prices():
#     pular = []
#     def pul_qoshish(pul):
#         pular.append(pul)
#         return pular
#     return pul_qoshish
#
# dolr = product_prices()
# print(dolr(100))
# print(dolr(150))  
