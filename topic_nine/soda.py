class Soda():

    def __init__(self , supplement):
        self.supplement = supplement

    def show_my_drink(self):
        if self.supplement != 'no_supplement':
            print('Газована вода та ' ,self.supplement)
        else:
            print('Звичайна газована вода')

soda = Soda(input())
soda.show_my_drink()
