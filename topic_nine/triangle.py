class Triangle_checker():
    def __init__(self, botom , lside ,rside):
        self.sides = [botom , lside ,rside]
        for i in self.sides:
            if i <= 0:
                print('Із від’ємними числами нічого не вийде!')
        self.max_side = max(self.sides)
                
    def is_triangle(self):
        self.sides.remove(self.max_side)
        if sum(self.sides) >= self.max_side:
            print('Ура, можна побудувати трикутник!')
        else:
            print('На жаль, з цього трикутник не зробити.')

trianglechecker = Triangle_checker(int(input()),int(input()),int(input()))
trianglechecker.is_triangle()