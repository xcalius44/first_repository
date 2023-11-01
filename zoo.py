import random

class Pet:
    """Віртуальний вихованець"""
    total = 0
    food = 0
    fun = 0
    @staticmethod   
    def status():
        print("Загальна кількість звірят", Pet.total)

    def __init__(self, name):
        Pet.total += 1
        self.__name = name
        self.hunger = random.randint(0, 7)
        self.boredom = random.randint(0, 7)

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1     
        
    def __str__(self):
        ans = self.__name + '\n'
        ans += str(self.hunger) + '\n'
        ans += str(self.boredom) + '\n'
        return ans
    
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        return unhappiness
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Ім'я звірятка не може бути порожнім рядком.")
        else:
            self.__name = new_name
            print("Ім'я успішно змінено.")

    def talk(self):
        self.__pass_time()
    
    def eat(self, food):
        print("Мррр...  Дякую!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Уііі!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    list_pet: [Pet] = [Pet(i) for i in input().split()]
    choice = None  
    while choice != "0":
        print \
        ("""
        Моє звірятко
    
        0 - Вийти
        1 - Дізнатися про самопочуття звірят
        2 - Годувати звірятка
        3 - Пограти зі звіряткоми
        """)
    
        choice = input("Ваш вибір: ")
        print()
        lenth = len(list_pet) - 1
        # вихід
        if choice == "0":
            print("До побачення.")

        # бесіда зі звірятком
        elif choice == "1":
            for i in range(lenth):
                unhappines =+ list_pet[i].mood
            if unhappines <= 5*lenth:
                print(" і зараз ми почуваемося прекрасно")
            elif 5*lenth <= unhappines <= 10*lenth:
                print(" і зараз ми почуваемося непогано")
            elif 11*lenth <= unhappines <= 15*lenth:
                print(" і зараз ми почуваемося не сказати щоб добре")
            else:
                print(" і зараз ми почуваемося жахливо")
        
        # годування звірятка
        elif choice == "2":
            food = int(input("скільки їжі насипати: "))
            for i in range(lenth):
                list_pet[i].eat(food)
         
        # гра зі звірятком
        elif choice == "3":
            fun = int(input("скільки годин грати: "))
            for i in range(lenth):
                list_pet[i].play(fun)

        # back_door
        elif choice == "back_door":
                print(list_pet)

        # незрозуміле введення користувача
        else:
            print("Вибачте, у меню немає пункту", choice)
        
main()
