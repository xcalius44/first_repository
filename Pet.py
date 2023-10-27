class Pet:
    """Віртуальний вихованець"""
    total = 0
    food = 0
    fun = 0
    @staticmethod   
    def status():
        print("Загальна кількість звірят", Pet.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        Pet.total += 1
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom

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
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "непогано"
        elif 11 <= unhappiness <= 15:
            m = "не сказати щоб добре"
        else:
            m = "жахливо"
        return m
    
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
        print("Мене звати", self.name, ", і зараз я почуваюся", self.mood)
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
    pet_name = input("Як ви назвете своє звірятко?: ")
    pet = Pet(pet_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Моє звірятко
    
        0 - Вийти
        1 - Дізнатися про самопочуття звірятка
        2 - Годувати звірятко
        3 - Пограти зі звірятком
        """)
    
        choice = input("Ваш вибір: ")
        print()

        # вихід
        if choice == "0":
            print("До побачення.")

        # бесіда зі звірятком
        elif choice == "1":
            pet.talk()
        
        # годування звірятка
        elif choice == "2":
            food = int(input("скільки їжі насипати: "))
            pet.eat(food)
         
        # гра зі звірятком
        elif choice == "3":
            fan = int(input("скільки годин грати: "))
            pet.play(fan)
        
        # back_door
        elif choice == "back_door":
                print(pet)

        # незрозуміле введення користувача
        else:
            print("Вибачте, у меню немає пункту", choice)
        
main()