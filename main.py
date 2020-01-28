"""Poniższy kod został napisany w języku Python. Jest on interpretacją lindek list, oryginalnie
    tworzonej w C. Python posiada wiele cech wspolnych z C (zbieżny syntax) i nie posiada
    mechanizmów autmatycznych dla linked list jak Java.
    Ponieważ zauważyłem że mechanizm linked list przypomina działania na obiektach, po moim
    pytaniu na wykładzie Podstawy programowaniaa, uzyskałem zgodę na użycie języka obiektowego do tego celu"""

from datetime import datetime

timestamp = 1545730073

def switch_menu(option):
    switcher = {
        1: "Dodaj element",
        2: "Usuń element",
        3: "Podaj liczbę elementów"
    }

class CarNode:
    def __init__(self, reg_numb, color, next_link=None):
        self.time = datetime.fromtimestamp(timestamp)
        self.regNumb = reg_numb
        self.color = color
        self.next = next_link


first = CarNode(datetime, 'WPR2153E', 'blue')


def main():
    if __name__ == '__main__':
        main()


print('Hello World! \nThis is linked list, please choose your option:')


