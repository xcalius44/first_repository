import random

class Animal:
    def __init__(self):
        self.hunger = 0

    def pass_time(self):
        self.hanger =+ 1
        
    def feed(self):
        self.hunger =- 2
        Animal.pass_time
        
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        Animal.pass_time
        print('miau') 

class Dog(Animal):
    def talk(self):
        Animal.pass_time
        print('gav')  

class Owel(Animal):
    def talk(self):
        Animal.pass_time
        print('owo owo')  

class Zoo():
    def __init__(self):
        self.animals = []

    def add(self, animal: Animal):
        self.animals.append(animal)
        # if typo == "dog":
        #     self.list_dog: [Dog] = [Dog(input().split())]
        #     self.lenght_dog = len()
        # elif typo == "cat":
        #     self.list_cat: [Cat] = [Cat(input().split())]
        #     self.lenght_cat = len()
        # else:
        #     print('error')

    def talk(self):
        for animal in self.animals:
            animal.talk()
            
        # for i in range(self.lenght_cat):
        #     self.list_cat[i].talk()
        # for i in range(self.lenght_dog):
            # self.list_dog[i].talk()
    
    def feed(self):
        for animal in self.animals:
            animal.feed()
            print("мммммм.............")

def main():
    
    zoo = Zoo()
    choice = None  
    while choice != "0":
        print \
        ("""
        Моє звірятко
    
        0 - Вийти
        cat - add cat
        dog - add dog
        owel - add owel
        talk - talk_animals
        feed - feed_animals
        """)
    
        choice = input("Ваш вибір: ")
        
        print()
        if choice == "0":
            print("До побачення.")
        
        elif choice == "dog":
            dog = Dog()
            zoo.add(dog)
        
        elif choice == "owel":
            owel = Owel()
            zoo.add(owel)
            
        elif choice == "cat":
            cat = Cat()
            zoo.add(cat)
            
        elif choice == "talk":
            zoo.talk()
            
        elif choice == "feed":
            zoo.feed()
        
        else:
            print("Вибачте, у меню немає пункту", choice)
        
main()