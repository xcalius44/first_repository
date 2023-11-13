class Tomato:
    
    states = ['nothing' ,'flower' ,'green_tomato' ,'red_tomato']
    
    def __init__(self, index):
        self._index = index
        self._state = 0
    
    def grow(self):
        self._state += 1
        self.print()
        
    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False
        
    def print(self):
        print('Tomato', self._index, 'is', Tomato.states[self._state])

class TomatoBush():
    
    def __init__(self, num):
        self.tomatos: [Tomato] = [Tomato(i) for i in range(0, num)]
    
    def grow_all(self):
        for tomato in self.tomatos:
            tomato.grow()
    
    def all_are_ripe(self):
        for tomato in self.tomatos:
            if tomato.is_ripe():
                return True
    
    def give_away_all(self):
        self.tomatos = []

class Gardener():
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    
    def work(self):
        print('gardener is working...')
        self._plant.grow_all()
        print('gardener is finished')
    
    def harvest(self):
        print("Gardener is harvesting...")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')
    @staticmethod
    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.''')
Gardener.knowledge_base()
tomato_bush = TomatoBush(3)
gardener = Gardener('Artem', tomato_bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()


        
