class Triangle_checker():
    def __init__(self, botom , lside ,rside):
        self.sides = [botom , lside ,rside]
        self.stop_retry = ''
        for i in self.sides:
            if i <= 0:
                self.stop_retry = 'Із від’ємними числами нічого не вийде!'
                
    def is_triangle(self):
        self.max_side = max(self.sides)
        self.sides.remove(self.max_side)
        if self.stop_retry == 'Із від’ємними числами нічого не вийде!':
            print(self.stop_retry)
        elif sum(self.sides) >= self.max_side:
            print('Ура, можна побудувати трикутник!')
        else:
            print('На жаль, з цього трикутник не зробити.')

trianglechecker = Triangle_checker(int(input()),int(input()),int(input()))
trianglechecker.is_triangle()