from tkinter import *
import math
from pygame import mixer
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
clock = None

reps = 0
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(clock)
    canvas.itemconfig(tomato_text, text="00:00")
    global reps
    reps = 0
    tick.config(text="")
    timer.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    mixer.init()
    sound = mixer.Sound("suspend-sound-113941.mp3")


    if reps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="Break", foreground=RED, background=YELLOW)
        sound.play()
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Break", foreground=PINK, background=YELLOW)
        sound.play()
    else:
        countdown(work_sec)
        timer.config(text="Work", foreground=GREEN, background=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_minute = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(tomato_text, text=f"{count_minute}:{count_sec}")
    if count > 0:
        global clock
        clock = window.after(1000, countdown, count -1)
    else:
        start_timer()
        mark = ""
        for _ in range (math.floor(reps / 2)):
            mark += "✓"
            tick.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

# label
timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), foreground=GREEN, background=YELLOW)
timer.grid(column=1, row=0)

# start button
start = Button(text="start", command=start_timer)
start.grid(column=0, row=2)

# reset button
reset = Button(text="reset", command=reset_timer)
reset.grid(column=2, row=2)

# green tick
tick = Label(text="", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 20))
tick.grid(column=1, row=3)

#set up the image, background colour and print the counter over the top.
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
tomato_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()