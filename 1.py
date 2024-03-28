# """Time nomli class yarating va uning property elementlari quyidagilardan iborat:
# Day(Kun);
# Month(Oy);
# Year(Yil).
# Ushbu classga tegishli 5ta obyekt yarating va ularni ma’lumotlarni foydalanuvchi tomonidan kiriting.
# Sizning vazifangiz quyidagilardan iborat bo‘lgan har bir obyekt uchun metodlar yaratish:
# 1) Barcha obyektlarning yilini 1taga oshirish va o’zgargan sanani chiqarish methodini yozing.
# 2) Har bir obyektlar uchun sanani 2kunga kamaytirish va o’zgargan sanani chiqarish methodini yozing.
# Eslatma: Barcha ma’lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo‘yiladi.
# """



class Time:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def qoshish_year(self):
        self.year += 1
        print(f"Yil o'zgargan sana: {self.year}")

    def ayirish_day(self):
        self.day -= 2
        print(f"Sana 2 kunga kamaytirildi. Yangi sana: {self.day}")

objects = []
for i in range(5):
    day = int(input(f"{i + 1}-o'bject uchun kunni kiriting: "))
    month = int(input(f"{i + 1}-o'bject uchun oyini kiriting: "))
    year = int(input(f"{i + 1}-o'bject uchun yilni kiriting: "))
    objects.append(Time(day, month, year))

for obj in objects:
    obj.qoshish_year()
    obj.ayirish_day()




