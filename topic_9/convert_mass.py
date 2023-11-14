class Kg_to_pounds_2():

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205
    
    @property
    def kg(self):
        return self.__kg
    
    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Кілограми задаються лише числами')
        
  
kg_to_pounds_2 = Kg_to_pounds_2(200)
print(kg_to_pounds_2.kg)
kg_to_pounds_2.kg = 202
print(kg_to_pounds_2.kg)
print(kg_to_pounds_2.to_pounds())
