from tkinter import *
import random

secret_number = random.randrange (0,100)
print(secret_number)
counter = 7
guess = 0
def check_guess():
    global guess,canvas_text, canvas
    if  guess<0 or guess >100: 
            canvas_text = 'Read the intructions!\n Only integers from 0-100!'
            create_canvas()
    else:
        input_guess()

def input_guess(): 
    global guess, counter, secret_number ,canvas_text, canvas
    counter = counter -1
    
    if guess > secret_number and counter > 0 and guess <=100 and guess >=0:
        canvas_text= 'Remaining guesses:\t' + str(counter) + '\nYou guessed:\t' + str(guess) +'\nThe secret number is smaller!'
        create_canvas()
    if guess < secret_number and counter > 0 and guess <=100 and guess >=0: 
        canvas_text= 'Remaining guesses:\t' + str(counter) + '\nYou guessed:\t' + str(guess) +'\nThe secret number is larger!'
        create_canvas()
    if guess == secret_number and counter >= 0 and guess <= 100 and guess >=0:
        canvas_text= 'Remaining guesseses:\t' + str(counter) + '\nThe secret number is:\t ' + str(secret_number)+'\nYou guessed: \t' + str(guess) +'\n You win!'
        create_canvas()
    if guess > secret_number and counter == 1 and guess <= 100 and guess >=0:
        canvas_text= 'You only have 1 guess left!' +'\nYou guessed:\t' + str(guess) +'\nThe secret number is smaller!'
        create_canvas()
    if guess < secret_number and counter == 1 and guess <= 100 and guess >=0:
        canvas_text= 'You only have 1 guess left!' +'\nYou guessed:\t' + str(guess) +'\nThe secret number is larger!'
        create_canvas()
    if guess != secret_number and counter == 0 and guess <= 100 and guess >=0:
        canvas_text= ' Game Over!\n '+ 'The secret number was '+ str(secret_number)+ ' \n Nice try.\n '
        create_canvas()
        
def new_game():
    global counter, secret_number, canvas_text, canvas
    counter = 7
    secret_number = random.randrange (0,100)
    canvas_text =' New game! \n Try integers from 0 to 100 \n You have 7 guesses'
    create_canvas()

tk = Tk()
frame = Frame(tk)
frame.pack()
label = Label(frame, text = 'Enter an integer from 0-100\n' ,font = 'TNR 15', fg = 'purple')
label.pack()
entry = Entry(frame, font = 'bold 20')
entry.pack()

canvas = Canvas(frame, width = 300, height = 200, bg = 'light pink')
canvas.pack()
def create_canvas():
    global canvas_text, canvas
    canvas.delete(ALL)
    canvas.create_text(150,100, text = canvas_text, fill = 'purple', font = 'TNR 12')
button1 = Button(frame, text = 'Enter', command = check_guess, width = 20 ,font = 'TNR 10')
button1.pack()
button2 = Button(frame, text = 'Play Again', command = new_game,width = 20 ,font = 'TNR 10')
button2.pack()
button3 = Button(frame, text = 'Exit', command = tk.destroy, width = 20 ,font = 'TNR 10')
button3.pack()

