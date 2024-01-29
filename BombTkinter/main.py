from tkinter import *

bombhealth = 100
score = 0
pressReturn = True
file_path = "scores.txt"  # Шлях до файлу для зберігання скорів
all_scores = []  # Створити список для зберігання всіх скорів

def start(event):
    global pressReturn, bombhealth, score
    if not pressReturn:
        pass
    else:
        bombhealth = 100
        score = 0
        label.config(text="")
        update_display()
        update_point()
        update_bombhealth()
        display_highest_score()
        pressReturn = False

def update_display():
    global score, bombhealth

    if bombhealth > 50:
        bomb_label.config(image=normal_photo)
    elif 0 < bombhealth <= 50:
        bomb_label.config(image=no_photo)
    elif bombhealth <= 0:
        bomb_label.config(image=bang_photo)

    fuse_label.config(text="Fuse = " + str(bombhealth))
    score_label.config(text="Score = " + str(score))
    fuse_label.after(100, update_display)

def update_bombhealth():
    global bombhealth
    bombhealth -= 5
    if is_alive():
        fuse_label.after(400, update_bombhealth)

def update_point():
    global score
    score += 1
    all_scores.append(score)  # Додати поточний бал до списку всіх скорів
    save_score(score)  # Зберегти скор у файл
    if is_alive():
        score_label.after(3000, update_point)

def click():
    global bombhealth
    if is_alive():
        bombhealth += 1

def is_alive():
    global bombhealth, pressReturn
    if bombhealth <= 0:
        label.config(text="BANG BANG BANG!!!")
        pressReturn = True
        display_highest_score()
        return False
    else:
        return True

def save_score(score):
    with open(file_path, "a") as file:  # Відкрити файл для запису
        file.write(str(score) + "\n")  # Записати скор у файл

def display_highest_score():
    global all_scores
    all_scores = read_scores_from_file(file_path)
    highest_score = max(all_scores) if all_scores else 0
    labelscore.config(text="Highest Score: " + str(highest_score))

def read_scores_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            scores = [int(score.strip()) for score in file.readlines() if score.strip()]
            return scores
    except FileNotFoundError:
        return []


root = Tk()
root.title("Bang Bang")
root.geometry("500x550")

label = Label(root, text="Press [Enter] to start the game", font=('ComicSans MS', 12), bg="LightGrey")
label.pack()

labelscore = Label(root, text="", font=('ComicSans MS', 12), bg="LightGrey")
labelscore.pack()

fuse_label = Label(root, text="Fuse: " + str(bombhealth), font=('ComicSans MS', 12))
fuse_label.pack()

score_label = Label(root, text="Score: " + str(score), font=('ComicSans MS', 12))
score_label.pack()

no_photo = PhotoImage(file="img/bomb_no.gif")
normal_photo = PhotoImage(file="img/bomb_normal.gif")
bang_photo = PhotoImage(file="img/pow.gif")

bomb_label = Label(root, image=no_photo)
bomb_label.pack()

click_button = Button(root, text="Click me", font=('ComicSans MS', 12), bg="#000000", fg="#ffffff", command=click,
                      width=15)
click_button.pack()

root.bind('<Return>', start)

root.mainloop()



