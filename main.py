import csv
from datetime import datetime


# Pizza icin ust class olusturulur
class Pizza:

    def __init__(self):
        self.description = []
        self.cost = 0

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description


# Pizza türleri alt classlar
class Peperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik hamur, domates sosu, mozarella, chili biberi"
        self.cost = 20


class Margarita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "İtalyan pizza"
        self.cost = 30


class Pugliese(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Mozarella, domates, halka soğan"
        self.cost = 40


class Vegan(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Domates, sarımsak sosu, patlıcan, kabak"
        self.cost = 35


class Order():  # Siparis verirken pizzaların fiyatlarını toplamak icin Order sinifi olusturulur
    def __init__(self):
        self.pizzas = []

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getTotal(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.get_cost()
        return total


class Decarator(Pizza):  # Sos superclassı
    def __init__(self, sos):
        super().__init__()
        self.component = sos


class Zeytin(Decarator):

    def __init__(self, sos):
        Decarator.__init__(self, sos)
        self.cost = 7



class Mantar(Decarator):

    def __init__(self, sos):
        Decarator.__init__(self, sos)
        self.cost = 10


class Peynir(Decarator):

    def __init__(self, sos):
        Decarator.__init__(self, sos)
        self.cost = 11


class Et(Decarator):

    def __init__(self, sos):
        Decarator.__init__(self, sos)
        self.cost = 15


class Sogan(Decarator):

    def __init__(self, sos):
        Decarator.__init__(self, sos)
        self.cost = 13


class Misir(Decarator):

    def __init__(self, sos):
        Decarator.__init__(self, sos)
        self.cost = 14


class ToppingOrder():  # Sosların fiyatlarını toplama eklemek için olusturulan sinif

    def __init__(self):
        self.topping = []

    def addTopping(self, toppings):
        self.topping.append(toppings)

    def toppingTotal(self):
        get_topping_total = 0
        for toppings in self.topping:
            get_topping_total += toppings.get_cost()
        return get_topping_total


order = Order()


def run():  # Console da menu olusturulur
    print("\nİstediğiniz pizzanın numarasını girin:\n\n\
    _____________________________________________________________\n\
    |1: Peperoni |  2: Margarita    |  3: Pugliese  |  4: Vegan   |\n\
    |    ₺20     |        ₺30       |        ₺40    |     ₺35     |\n\
    |____________|__________________|_______________|_____________|\n\
    \n- Sos seçimi için 't' ye basın.\n")

    while True:
        try:

            response = input('-')

            if response == 't':
                break
            elif int(response) == 1:  # Secilen pizza 1 numaralı pizza ise acıklaması ekrana yazacak
                pizza1 = Peperoni()
                print(f"Pizza: {pizza1.get_description()}")
                order.addPizza(pizza1)
            elif int(response) == 2:
                pizza2 = Margarita()
                print(f"Pizza: {pizza2.get_description()}")
                order.addPizza(pizza2)  # Pizzaları 'pizzas' a ekliyoruz, birden fazla pizza alınabilir.
            elif int(response) == 3:
                pizza3 = Pugliese()
                print(f"Pizza: {pizza3.get_description()}")
                order.addPizza(pizza3)
            elif int(response) == 4:
                pizza4 = Vegan()
                print(f"Pizza: {pizza4.get_description()}")
                order.addPizza(pizza4)
        except:
            print("Bir sorun oluştu lütfen tekrar deneyin.")


run()  # Ilk menu calısır

print("Şuan ki sepet tutarı: ", "₺" + str(order.getTotal()))  # Sadece pizzalar secildigindeki ucret

topping_order = ToppingOrder()  # Sos siparisi basladi


def runTopping():  # Sos menusu
    print("\nİstediğiniz ek malzemelerin numarasını girin.\n\n\
    ______________________________________________________________________\n\
    |  5: Zeytin 7₺   |   6: Mantar  10₺  |  7: Peynir 11₺  |    8: Et  15₺    |\n\
    |  9: Soğan  13₺  |   10: Mısır  14₺  |                 |                  |\n\
    |_________________|___________________|_________________|__________________|\n\
    Toplam sepet tutarı için f ye basın: \n")

    while True:
        try:
            response = input('-')
            if response == 'f':
                break
            elif int(response) == 5:
                sos1 = Zeytin(Pizza)
                print(f"Topping: {sos1}")
                topping_order.addTopping(sos1)
            elif int(response) == 6:
                sos2 = Mantar(Pizza)
                print(f"Topping: {sos2}")
                topping_order.addTopping(sos2)
            elif int(response) == 7:
                sos3 = Peynir(Pizza)
                print(f"Topping: {sos3}")
                topping_order.addTopping(sos3)
            elif int(response) == 8:
                sos4 = Et(Pizza)
                print(f"Topping: {sos4}")
                topping_order.addTopping(sos4)
            elif int(response) == 9:
                sos5 = Sogan(Pizza)
                print(f"Topping: {sos5}")
                topping_order.addTopping(sos5)
            elif int(response) == 10:
                sos6 = Misir(Pizza)
                print(f"Topping: {sos6}")
                topping_order.addTopping(sos6)
        except:
            print("Bir sorun oluştu tekrar deneyin.")


rows = ["Ad",
        "Soyad",
        "Kart No",
        "Şifre",
        "Tutar",
        "Sipariş Tarihi"]  # Csv dosyasindaki columnlar

local = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")  # Siparis tarihi


def credit():
    print("Kredi kartı bilgilerinizi girin: ")
    name = input("Adınız: ")
    surname = input("Soyadınız: ")
    card = input("Kart Numarası: ")
    password = input("Şifre: ")  # Kullanici bilgileri isteniyor

    filename = "user_data1.csv"
    with open(filename, mode='w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(rows)
        csvwriter.writerow([name, surname, card, password, final_total, local])  # Csv dosyasina yazildi


runTopping()
sub_pizza = int(order.getTotal())  # Pizzalarin toplami
sub_sos = int(topping_order.toppingTotal())  # Soslarin toplami
final_total = sub_pizza + sub_sos  # Toplam fatura
print(f" \nToplam sepet tutarınız ₺{final_total}\n")

credit()

print("Sipariş alındı!")
