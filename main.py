# coding=utf-8

"""Poniższy kod został napisany w języku Python. Jest on interpretacją lindek list, oryginalnie
    tworzonej w C. Python posiada wiele cech wspolnych z C (zbieżny syntax) i nie posiada
    mechanizmów autmatycznych dla linked list jak Java.
    Ponieważ zauważyłem że mechanizm linked list przypomina działania na obiektach, po moim
    pytaniu na wykładzie Podstawy programowaniaa, uzyskałem zgodę na użycie języka obiektowego do tego celu"""

from datetime import datetime  # Dal używania timestampu, użyję gotowych bibliotek Pythona

option = None


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
        car = self.root
        while car is not None:
            print(car.reg_numb)
            car = car.nextval


if __name__ == '__main__':
    print("Hello World! \nThis is linked list, please choose your option:")
    c1 = CarNode('WPR2153E', 'blue')
