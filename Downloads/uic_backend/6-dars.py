class ATM:

    def __init__(self,balance_card=1_000_000, password_card=7777 ):
        self.password_card = password_card
        self.balance_card = balance_card


    def main_window(self):
        print("\n")
        print("-> Uzbek tili uchun 1 ni bosing")
        print("-> Rus tili uchun 2 ni bosing")
        print("-> English tili uchun 3 ni bosing")
        til = int(input("-> "))
        if til != 0:
            self.password_score()


    def menu(self):
        print("             MENU")
        print("-> Balanc ni tekshirish 1 ")
        print("-> Naqt pul yechish     2 ")
        print("-> Parolni uzgartirish  3 ")
        print("-> Bosh oynaga qaytish  4 ")
        menu_input = int(input("-> "))
        if menu_input == 1:
            print(f"-> Hisobingizda {self.balance_card} so'm mavjut")
            self.menu()
        elif menu_input == 2:
            self.withdraw()
        elif menu_input == 3:
            self.edit_password()
        elif menu_input == 4:
            self.main_window()
        else:
            print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.\n")
            self.menu()


    def withdraw(self):
        getting = int(input("-> Summani kiriting "))
        if getting < self.balance_card - (self.balance_card * 0.1):
            res = self.balance_card - getting - (getting * 0.1)
            print(f"-> Marxamat {getting} so'm")
            print(f"-> Qolgan mablag' {res}")
        else:
            print("-> Hisobingizda yetarli mablag' mavjut emas!")


    def edit_password(self):
        old_password = int(input("-> Eski parolni kiriting: "))

        if old_password == self.password_card:
            new_password = int(input("-> Yangi parolni kiriting: "))
            self.password_card = new_password
            print("Parol muvaffaqiyatli o'zgartirildi!")
            self.password_score()
        else:
            print("Eski parol noto'g'ri kiritildi!")


    def password_score(self):
        score = 0
        while True:
            parol = int(input("-> Parolingizni kiriting -> "))
            score += 1
            if parol == self.password_card:
                self.menu()
            if score >= 3:
                print("-> Noto'g'ri parol kiritdingiz! Kartangiz bloklandi")
                self.main_window()


bankomat = ATM()
bankomat.main_window()

