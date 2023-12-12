import easygui
import random

def rock_paper_scissors():
    out = easygui.buttonbox("Оберіть ваш варіант", "Rock, Paper, Scissors",
                            choices = '',
                            images = ["topic_11/rock.png", "topic_11/paper.png", "topic_11/scissors.png"])
    game = random.randint(1, 3)
    if game == 1 and out == "rock.png":
        easygui.msgbox("Нічия, супротивник вибрав камінь", "Tie")
    if game == 1 and out == "topic_11/paper.png":
        easygui.msgbox("Гравець вийграв! Супротивник вибрав камінь", "Win")
    if game == 1 and out == "topic_11/scissors.png":
        easygui.msgbox("Гравець програв! Супротивник вибрав камінь", "Lose")
    if game == 2 and out == "topic_11/rock.png":
        easygui.msgbox("Гравець програв! Супротивник вибрав бумагу", "Lose")
    if game == 2 and out == "topic_11/paper.png":
        easygui.msgbox("Нічия, супротивник вибрав бумагу", "Tie")
    if game == 2 and out == "topic_11/scissors.png":
        easygui.msgbox("Гравець вийграв! Супротивник вибрав бумагу", "Win")
    if game == 3 and out == "topic_11/rock.png":
        easygui.msgbox("Гравець вийграв! Супротивник вибрав ножиці", "Win")
    if game == 3 and out == "topic_11/paper.png":
        easygui.msgbox("Гравець програв! Супротивник вибрав ножиці", "Lose")
    if game == 3 and out == "topic_11/scissors.png":
        easygui.msgbox("Нічия, супротивник вибрав ножиці", "Tie")
        
def guess_the_number():
    number = random.randint(1, 100)
    out = 0
    
    while out != number:
        out = easygui.integerbox("Введіть число", "Guess the number", lowerbound=1, upperbound=100)
        if out < number:
            easygui.msgbox('Bigger', "", image = "topic_11/gt.png")
        elif out > number:
            easygui.msgbox('less', "", image = "topic_11/lt.png")
        else:
            easygui.msgbox('Ти вгадав число!', "win", image = "topic_11/eq.png")
games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()