do_kondagi_mahsulotlar = ["un", "qovun", "non", "olma", "anor", "uzum", "sut"]
bor_mahsulotlar = []
mavjud_emas = []

for i in range(5):
    mahsulot = input("Savatga " + str(i + 1) + "-mahsulotni qo'shing: ")
    if mahsulot in do_kondagi_mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Quyidagi mahsulotlar do'konimizda yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

foydalanuvchilar = ["admin", "ali", "vali", "hasan", "husan"]
yangi_login = input("Yangi login tanlang: ")

if yangi_login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz, " + yangi_login + "!")