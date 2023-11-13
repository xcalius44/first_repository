class Soda():

    def __init__(self , saplement):
        self.saplement = saplement

    def show_my_drink(self):
        if self.saplement != 'no_saplement':
            print('Газована вода та ' ,self.saplement)
        else:
            print('Звичайна газована вода')

soda = Soda(input())
soda.show_my_drink()
