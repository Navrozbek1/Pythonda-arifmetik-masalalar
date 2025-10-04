""" Pythonda arifmetik operatorlar mavzusidan algoritmik masalalar  """

# 1.1

# a = int(input("A-sonni kiriting: "))
# b = int(input("B-sonni kiriting: "))
# print("Javob:",a+b)

# 1.2

# L = int(input("Uzunligini kiriting: "))
# W = int(input("Enini kiriting: "))
# print("Yuzasi: ",L*W)

# 1.3

# x = int(input("x-sonni kiriting: "))
# y = int(input("y-sonni kiriting: "))
# z = int(input("z-sonni kiriting: "))
# print(f"Uch ta sonni o'rta airfmetigi: {x+y+z // 3}")

# 1.4

# a = int(input("A-sonni kiriting: "))
# b = int(input("B-sonni kiriting: "))
# print("Peremetri:",(2 * (a+b)))

# 1.5

# h = int(input("Soatni kiriting: "))
# m = int(input("Minutni kiriting: "))
#
# print(f"Javob: {(h*60)+m} minut!")

# 1.6

# usd = int(input("$ ni kiriting: "))
# print(f"Sizda: {usd*11_500} Ming So'm bor !")

# 1.7

# a = int(input("A-sonni kiriting: "))
# b = int(input("B-sonni kiriting: "))
# farq = abs(a - b)
# print("Farqi: ",farq)

# 1.8

# x = int(input("x-sonni kiriting: "))
# n = int(input("n-sonni kiriting: "))
# daraja = x**n
# print("X ni n darajasi: ",daraja)

# 1.9

# x = int(input("x-sonni kiriting: "))
# n = int(input("n-sonni kiriting: "))
# son = x//n
# q = x%n
# print("Sonni ozi: ",son, "Qoldiqi: ", q)

# 1.10

# a = int(input("A-sonni kiriting: "))
# b = int(input("B-sonni kiriting: "))
#
# a,b = b,a
#
# print(f"Javob: \n A: {a} \n B: {b}")

# 2.1

# tolov = int(input("Tolovni kiriting: "))
# oy = int(input("Necha oyga tolamoqchisiz: "))
# som = tolov // oy
# print(f"Oylik tolov soumasi: {som} ming so'm !")

# 2.2

# d = int(input("Masaofani (KM) da kiriting: "))
# v = int(input("Tezlikni kiriting: "))
# print(f"Siz berilgan masaofanai: {d / v} soatda bosibib O'tasiz !")

# 2.3

# son = int(input("Nechta yolovchi sigimi mavjud: "))
# x = int(input("Nechta odam chiqdi: "))
#
# nechta_yetadi = son // x
# nechta_qoldi = son % x
# print(f"Har bir yolovchiga: {nechta_yetadi} yetdi. Ortib qoldi: {nechta_qoldi}")

# 2.4

# litr = int(input("100 km ga Nechta litr benzin ketadi: "))
# km = int(input("Nechta KM yurildi: "))
# print(f"Bu masofani bosib otish uchun: {litr * km / 100} litr yonilg'i ketdi !")

# 2.5

# maosh = input("Oylik maoshni kiriting: ")
# print(f"Xodim 12% ushlab qolish bilan: {int(maosh) * (1-0.12)} so'm olasiz!")

# 2.6

# amount = int(input("Oladigan pul: "))
# days = int(input("kechikkan kunlar: "))
# penalty = amount * 0.001 * days
# total = amount + penalty
# print(f"Siz beriladigan pul: {total}")

# 2.7

# price = int(input("Maxsulot narxi: "))
# discount = int(input("Xaridor chegirmasi: "))
# paid = price * (1 - discount / 100)
# print(f"Maxsulot chegirma bilan: {paid}")

# 2.8

# P = int(input("Asosiy summa: "))
# r = int(input("Yillik foiz stavkasi : "))
# t = int(input("Yillar soni: "))
# interest = (P * r * t) / 100
# total = P + interest
# print(f"Natija Hisoblangan foiz: {interest}. Umumiy summa: {total}")

# 2.9

# base_qty = int(input("Retseptdagi asosiy miqdor (gram): "))
# people = int(input("Necha kishi uchun hisoblasin: "))
# per_person = base_qty / 4
# needed = per_person * people
# print(f"{people} kishi uchun kerakli miqdor: {needed} gramm")

# 2.10

# bill = int(input("Hisob-kitob summasi (so'm): "))
# tip = bill * 0.10
# total = bill + tip
# print(f"10% choychaqa bilan umumiy summa: {total} so'm.")