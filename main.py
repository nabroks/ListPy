# coding=utf-8

"""Poniższy kod został napisany w języku Python. Jest on interpretacją lindek list, oryginalnie
    tworzonej w C. Python posiada wiele cech wspólnych z C (zbieżny syntax) i nie posiada
    mechanizmów automatycznych dla linked list jak Java.
    Na wykładzie zapytałem odnośnie struktur w C, czy nie jest to próba programowania obiektowego w języku
    strukturalnym. Wspomniał mi Pan że zasada jest podobna i ma to pomóc zrozumieć obiekty.
    Wspomniał Pan że mogę zrobić zadanie w języku obiektowym, i choć pewnie chodziło Panu o C, to skorzystałem
    z języka z którym wiążę przyszłość, a który na C bazuje. Proszę o zrozumienie i mam nadzieję że to zadanie
    będzie przynajmniej dowodem że rozumiem problematykę i pozwoli mi projekt zaliczyć.
    Ponieważ zauważyłem że mechanizm linked list przypomina działania na obiektach, po moim
    pytaniu na wykładzie Podstawy programowania, uzyskałem zgodę na użycie języka obiektowego do tego celu"""

from datetime import datetime  # Dla używania timestampu, użyję gotowych bibliotek Pythona
from sys import exit

selection = None


class CarNode:
    def __init__(self, reg_numb, color, next_link=None):
        self.time = datetime.now()
        self.reg_numb = reg_numb
        self.color = color
        self.next = next_link


class CarPark:
    def __init__(self):
        self.root = None

    # Dodawanie na początku listy - tworzenie pierwszego node
    def at_begining(self, reg_numb, color):
        newCar = CarNode(reg_numb, color)
        if self.root is not None:
            newCar.next = self.root
        self.root = newCar

    # Dodawanie na koniec - to co nasz interesuje czyli opcja 1
    def at_end(self, reg_numb, color):
        newCar = CarNode(reg_numb, color)
        if self.root is None:
            newCar.next = self.root
        else:
            car = self.root
            while car.next:
                car = car.next
            car.next = newCar

    def remove_car(self, reg_number):  # Metoda do usuwania Node czyli opcja druga
        car = self.root
        if car is None:  # Ta część sprawdza tylko pierwszy element listy
            return
        elif car.reg_numb == reg_number:
            self.root = car.next
            car = None
            return
        while car is not None:  # Ta część iteruje listę w poszukiwaniu zgodnej rejestracji
            if car.reg_numb == reg_number:
                break
            prev_car = car
            car = car.next
        if car is None:  # Jeśli nie ma wcale to wyjście z pętli
            return
        prev_car.next = car.next
        car = None

    # Opcja trzecia, drukuje listę
    def print_list(self):
        total = 0
        car = self.root
        while car is not None:
            print(f"{car.reg_numb} koloru: {car.color}")
            car = car.next
            total += 1
        print(f"Ilość samochodów na parkingu: {total}")


def print_menu():  # Funkcja drukująca menu wyboru
    options = ["1 : Dodaj samochód",
               "2 : Usuń samochód",
               "3 : Status parkingu",
               "4 : Wyjście z programu"]
    for opt in options:
        print(opt)


def menu():  # Funkcja wybierania opcji listy i aktywacji połączonych funkcji/metod

    my_parking = CarPark()
    running = True

    #  Te samochody już stały na parkingu!! :D Program jest tak mądry że już je ujmuje.
    my_parking.at_begining("WPR 2153E", "Niebieski")  # Tworzy na początku listy, pierwszy node
    my_parking.at_end("WWL 53893", "Czerwony")
    my_parking.at_end("WPI 534K1", "Czerwony")

    while running:
        print_menu()
        selection = input("Wybierz opcję:")
        print(selection)
        if selection == "1":
            print("== Dodaję samochód na koniec listy ==")
            reg_num = input("Podaj numer rejestracyjny:")
            color = input("Podaj kolor samochodu:")
            my_parking.at_end(reg_num, color)
        elif selection == "2":
            print("== Usuwam samochód z listy ==")
            reg_num = input("Podaj numer rejestracyjny:")
            my_parking.remove_car(reg_num)
        elif selection == "3":
            print("== Drukuję status parkingu ==")
            my_parking.print_list()
        elif selection == "4":
            running = False
        else:
            print("Niepoprawny wybór, prosze podaj poprawną wartość")
    exit(0)  # Służy do eleganckiego zakończenia programu


if __name__ == '__main__':
    print("Program kontroli parkingu samochodowego v 1.0:")
    menu()
